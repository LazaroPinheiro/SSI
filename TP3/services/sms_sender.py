import nexmo


class sms_sender:
    def __init__(self, key, secret, sourceName):
        self.key = key
        self.secret = secret
        self.sourceName = sourceName

    def send_message(self, user, token):
        client = nexmo.Client(key=self.key, secret=self.secret)

        responseData = client.send_message({
            'from': str(self.sourceName),
            'to': str(user.phoneNumber),
            'text': 'O seu token é : {}!'.format(token)
        })

        response = responseData['messages'][0]

        if response['status'] == '0':
            # print('Sent message', response['message-id'])

            # print('Remaining balance is', response['remaining-balance'])
            return True
        else:
            # print('Error:', response['error-text'])
            return False
