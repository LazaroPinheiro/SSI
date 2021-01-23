import re


class user:
    def __init__(self, username, phoneNumber):
        self.username = username
        self.phoneNumber = phoneNumber
        self.__formatPhoneNumber()

    def __formatPhoneNumber(self):
        if bool(re.match("^3519(1|2|3|6)\d{7}$", self.phoneNumber)):
            print("Valid")
        elif bool(re.match("^9(1|2|3|6)\d{7}$", self.phoneNumber)):
            self.phoneNumber = "351" + self.phoneNumber
        else:
            raise ValueError("Invalid phone number!")

    def __str__(self):
        return f'{self.username}:{self.phoneNumber}\n'.format(self=self)
