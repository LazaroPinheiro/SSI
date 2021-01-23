import errno
import os
import signal

from fuse import FuseOSError, Operations

from business.user_manager import user_manager
from exceptions.phoneNumberInvalidException import PhoneNumberInvalidException
from exceptions.userDoestExistsException import UserDoestExistsException
from services.sms_sender import sms_sender
from services.token_generator import token_generator
from view.view import view


def handler(signum, frame):
    raise TimeoutError('Timeout exceeded')


class FuseController(Operations):

    def __init__(self, root, configurations):
        self.root = root
        self.view = view()

        try:
            self.user_manager = user_manager(configurations.pathUsersFile)
        except FileNotFoundError:
            self.view.usersFileAbsent()
            exit(1)

        self.token_generator = token_generator(configurations.token_size)
        self.sms_sender = sms_sender(configurations.sourceName, configurations.nexmo_key,
                                     configurations.nexmo_secret)
        self.timeout_time = configurations.timeout_time

    # Helpers
    # =======

    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(self.root, partial)
        return path

    # Filesystem Methods
    # ==================

    def access(self, path, mode):
        full_path = self._full_path(path)
        if not os.access(full_path, mode):
            raise FuseOSError(errno.EACCES)

    def chmod(self, path, mode):
        full_path = self._full_path(path)
        return os.chmod(full_path, mode)

    def chown(self, path, uid, gid):
        full_path = self._full_path(path)
        return os.chown(full_path, uid, gid)

    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        st = os.lstat(full_path)
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                                                        'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size',
                                                        'st_uid'))

    def readdir(self, path, fh):
        full_path = self._full_path(path)

        dirents = ['.', '..']
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        for r in dirents:
            yield r

    def readlink(self, path):
        pathname = os.readlink(self._full_path(path))
        if pathname.startswith("/"):
            # Path name is absolute, sanitize it.
            return os.path.relpath(pathname, self.root)
        else:
            return pathname

    def mknod(self, path, mode, dev):
        return os.mknod(self._full_path(path), mode, dev)

    def rmdir(self, path):
        full_path = self._full_path(path)
        return os.rmdir(full_path)

    def mkdir(self, path, mode):
        return os.mkdir(self._full_path(path), mode)

    def statfs(self, path):
        full_path = self._full_path(path)
        stv = os.statvfs(full_path)
        return dict((key, getattr(stv, key)) for key in ('f_bavail', 'f_bfree',
                                                         'f_blocks', 'f_bsize', 'f_favail', 'f_ffree', 'f_files',
                                                         'f_flag',
                                                         'f_frsize', 'f_namemax'))

    def unlink(self, path):
        return os.unlink(self._full_path(path))

    def symlink(self, name, target):
        return os.symlink(target, self._full_path(name))

    def rename(self, old, new):
        return os.rename(self._full_path(old), self._full_path(new))

    def link(self, target, name):
        return os.link(self._full_path(name), self._full_path(target))

    def utimens(self, path, times=None):
        return os.utime(self._full_path(path), times)

    # File Methods
    # ============

    def open(self, path, flags):
        full_path = self._full_path(path)

        username = view.getUserName()

        try:
            user = self.user_manager.getUser(username)

            generatedToken = self.token_generator.get_random_string()

            print(generatedToken)

            success = True  # self.sms_sender.send_message(user, generatedToken)

            if success:

                try:
                    signal.signal(signal.SIGALRM, handler)
                    signal.alarm(self.timeout_time)
                    insertedToken = self.view.getToken(user.phoneNumber)
                    signal.alarm(0)

                    if str(insertedToken) == generatedToken:
                        self.view.accessConceded(full_path)
                        return os.open(full_path, flags)
                    else:
                        self.view.accessDenied()
                        return 0
                except TimeoutError:
                    self.view.timedOut()
                    return 0
            else:
                self.view.errorSendingEmail()
                return 0

        except UserDoestExistsException:
            self.view.usernameAbsent(username)
            return 0
        except PhoneNumberInvalidException:
            self.view.invalidPhoneNumber()
            return 0

    def create(self, path, mode, fi=None):
        full_path = self._full_path(path)
        return os.open(full_path, os.O_WRONLY | os.O_CREAT, mode)

    def read(self, path, length, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def write(self, path, buf, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.write(fh, buf)

    def truncate(self, path, length, fh=None):
        full_path = self._full_path(path)
        with open(full_path, 'r+') as f:
            f.truncate(length)

    def flush(self, path, fh):
        return os.fsync(fh)

    def release(self, path, fh):
        return os.close(fh)

    def fsync(self, path, fdatasync, fh):
        return self.flush(path, fh)
