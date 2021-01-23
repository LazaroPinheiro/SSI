class PhoneNumberInvalidException(Exception):

    def __init__(self, phoneNumber, message="User phone number invalid."):
        self.phoneNumber = phoneNumber
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.phoneNumber} -> {self.message}'
