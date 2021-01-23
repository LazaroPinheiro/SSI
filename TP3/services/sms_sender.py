import nexmo


class sms_sender:
    def __init__(self, key, secret, sourceName):
        self.key = key
        self.secret = secret
        self.sourceName = sourceName

    def send_message(self, user, token):
        try:
            client = nexmo.Client(key=self.key, secret=self.secret)
            client.send_message(
                {'from': self.sourceName, 'to': user.phoneNumber, 'text': 'O seu token é : {}!'.format(token)})
            return True
        except:
            return False
