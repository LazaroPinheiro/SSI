import time


class view:

    def __init__(self):
        self.welcomeMessage = "###########################################\n" \
                              "##     FUSE - FILE SYSTEM CONTROLLER     ##\n" \
                              "###########################################"
        self.__printWelcomeMessage()

    def __printWelcomeMessage(self):
        print("\033c")
        print(self.welcomeMessage)

    @staticmethod
    def getUserName():
        return input(
            "\n\nPlease type your username.\n" +
            "Username:"
        )

    @staticmethod
    def getToken(phoneNumber):
        return input(
            f"\n\nPlease insert the token send to phone number : {phoneNumber}.\n" +
            "Token:"
        )

    def timedOut(self):
        print("\033c")
        print(
            "\n\n»»»»»»»»»»»»»»»«««««««««««««««\n" +
            "»»         WARNING          ««\n" +
            "» Timed Out! Session expired «\n" +
            "»»»»»»»»»»»»»»»«««««««««««««««\n\n"
        )
        time.sleep(2)
        print("\033c")
        self.__printWelcomeMessage()

    def accessConceded(self, filePath):
        print("\033c")
        print('\n\nAccess Conceded to file with path: ' + filePath + ' ;\n\n')
        time.sleep(1)
        print("\033c")
        self.__printWelcomeMessage()

    def accessDenied(self):
        print("\033c")
        print("\n\nThe token inserted is invalid.\n\n")
        time.sleep(1)
        print("\033c")
        self.__printWelcomeMessage()

    def usernameAbsent(self, username):
        print("\033c")
        print("\n\nUsername: " + username + " doesn't exists\n"
                                            "Please contact system administrator!\n")
        time.sleep(2)
        print("\033c")
        self.__printWelcomeMessage()

    @staticmethod
    def usersFileAbsent():
        print("\n\nSomething went Wrong.\nPlease contact system administrator!\n")

    def invalidPhoneNumber(self):
        print("\033c")
        print("\n\nYour phone number is invalid.\nPlease contact system administrator!\n")
        time.sleep(2)
        print("\033c")
        self.__printWelcomeMessage()

    def errorSendingSMS(self):
        print("\033c")
        print("\n\nSomething went wrong sending token to you.\nPlease try again later!\n")
        time.sleep(2)
        print("\033c")
        self.__printWelcomeMessage()
