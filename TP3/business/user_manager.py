import os

from models.user import user


class user_manager:

    def __init__(self, usersFilePath):
        self.usersFilePath = usersFilePath
        if not os.path.exists(self.usersFilePath):
            with open(self.usersFilePath, 'w'): pass

    def addNewUser(self, username, phoneNumber):
        str_user = user(username, phoneNumber)
        n = open(self.usersFilePath, 'r').read().find(str_user)
        if n < 0:
            open(self.usersFilePath, 'a').write(str_user)
        else:
            raise Exception('User already exists!')

    def getUser(self, username):
        with open(self.usersFilePath, 'r') as usersFile:
            for line in usersFile:
                str_user = line.split(':')
                if str_user[0] == username:
                    return user(str_user[0], str_user[1])
        raise Exception('User doesn\'t exists!')
