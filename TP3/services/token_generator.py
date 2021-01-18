import random
import string


class token_generator:
    def __init__(self, length):
        self.letters = string.ascii_letters
        self.length = length

    def get_random_string(self):
        result = ''.join(random.choice(self.letters) for i in range(self.length))
        return result
