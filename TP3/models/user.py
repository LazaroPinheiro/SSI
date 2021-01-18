class user:
    def __init__(self, username, phoneNumber):
        self.username = username
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f'{self.username}:{self.phoneNumber}\n'.format(self=self)
