# utils/class_utils.py

class Encoder(object):
    @staticmethod
    def encode(s):
        return s[::-1]


class Decoder(object):
    @staticmethod
    def decode(self, s):
        return ''.join(reversed(list(s)))
