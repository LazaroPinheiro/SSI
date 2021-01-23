import os

from models.user import user


class user_manager:

    def __init__(self, usersFilePath):
        self.usersFilePath = usersFilePath
        if not os.path.exists(self.usersFilePath):
            raise FileNotFoundError("File doesn't exists!")
        else:
            os.chmod(self.usersFilePath, 000)

    def getUser(self, username):
        success = False

        os.chmod(self.usersFilePath, 400)

        with open(self.usersFilePath, 'r') as usersFile:
            for line in usersFile:
                str_user = line.split(':')
                if str_user[0] == username:
                    success = True

        os.chmod(self.usersFilePath, 000)
        if success:
            return user(str_user[0], str_user[1])
        else:
            raise Exception("User doesn't exists!")
