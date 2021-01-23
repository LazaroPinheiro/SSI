class UserDoestExistsException(Exception):

    def __init__(self, username, message="User doesn't exists in users file."):
        self.username = username
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.username} -> {self.message}'
