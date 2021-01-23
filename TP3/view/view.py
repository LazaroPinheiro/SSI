class view:

    def __init__(self):
        print(
            "###########################################\n" +
            "##     FUSE - FILE SYSTEM CONTROLLER     ##\n" +
            "###########################################\n\n"
        )

    @staticmethod
    def getUserName():
        return input(
            "Please type your user name.\n" +
            "Username:"
        )

    @staticmethod
    def getToken(phoneNumber):
        return input(
            f"Please insert the token send to phone number : {phoneNumber}.\n\n" +
            "Token:"
        )

    @staticmethod
    def timedOut():
        print(
            "»»»»»»»»»»»»»»»«««««««««««««««\n" +
            "»»         WARNING          ««\n" +
            "» Timed Out! Session expired «\n" +
            "»»»»»»»»»»»»»»»«««««««««««««««\n\n"
        )
