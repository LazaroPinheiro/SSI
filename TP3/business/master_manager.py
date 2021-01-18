import re

from services.sms_sender import sms_sender
from services.token_generator import token_generator
from business.user_manager import user_manager
from models.user import user


@staticmethod
def validatePhoneNumber(phoneNumber):
    return bool(re.match("^(?:351|)9(1|2|3|6)\d{7}$", phoneNumber))


class master_manager:

    def __init__(self, configurations):
        self.token_generator = token_generator(configurations["token_generator"]["token_size"])
        self.sms_sender = sms_sender(configurations["sms_sender"]["sourceName"],
                                     configurations["sms_sender"]["nexmo"]["key"],
                                     configurations["sms_sender"]["nexmo"]["secret"])
        self.user_manager = user_manager(configurations["user_manager"]["pathUsers"])

    def addNewUser(self, username, phoneNumber):
        number = phoneNumber.replace('+', '', 1)
        if validatePhoneNumber(number):
            u = user(username, phoneNumber)
            self.user_manager.addNewUser(u)
        else:
            raise Exception('Invalid PhoneNumber')

