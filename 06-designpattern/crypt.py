import base64

from Crypto.Cipher.AES import new, MODE_ECB


class Encrypt:
    def encrypt(self, data):
        """
        Default encrypt method

        :param data: str
        :rtype: str
        :return: data
        """
        return data

    def decrypt(self, data):
        """
        Default decrypt method

        :param data: str
        :rtype: str
        :return: data
        """
        return data


class EncryptDecorator(Encrypt):
    def __init__(self, decorated: Encrypt):
        """
        Takes an Encrypt instance and decorates it
        :param decorated: Instance to decorate
        """
        self.decorated = decorated

    def encrypt(self, data):
        """
        Calls the default encode method in case it is not implemented

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        return self.decorated.encrypt(data)

    def decrypt(self, data):
        """
        Calls the default decode method in case it is not implemented

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        return self.decorated.decrypt(data)


class Base64(EncryptDecorator):
    def __init__(self, wrapper: Encrypt):
        super().__init__(wrapper)

    def encrypt(self, data):
        """
        Encodes a string using base64

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        return base64.b64encode(
            # Call decorated encrypt
            self.decorated.encrypt(data)
        ).decode()

    def decrypt(self, data):
        """
        Decodes a string using base64

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        print("AES decrypted %s to: %s\n" % (data, self.decorated.decrypt(data)))
        return base64.b64decode(
            # Call decorated decrypt
            self.decorated.decrypt(data)
        )


class Caesar(EncryptDecorator):
    def __init__(self, wrapper: Encrypt):
        super().__init__(wrapper)

        self.SUITE = new('some default key', MODE_ECB)
        self.bs = 16

    @staticmethod
    def pad(s):
        print("Pad %s to %s" % (s, s + (16 - len(s) % 16) * chr(16 - len(s) % 16)))
        return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

    @staticmethod
    def cut(s):
        print("Cut %s to %s" % (s, s[0:-ord(s[-1])]))
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, data):
        """
        Encrypts a string using AES

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        return self.SUITE.encrypt(self.pad(  # AES encrypt and add padding
            self.decorated.encrypt(data)  # Call decorated encrypt
        ))

    def decrypt(self, data):
        """
        Decrypts a string using AES

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        print("Base64 decrypted %s to: %s\n" % (data, self.decorated.decrypt(data)))
        return self.cut(self.SUITE.decrypt(  # AES decrypt and cut
            self.decorated.decrypt(data)[16:]  # Call decorated decrypt
        ))
