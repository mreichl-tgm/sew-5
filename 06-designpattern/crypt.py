"""
Provides classes to encrypt and decrypt a string using the decorator pattern
"""


class Encrypt:
    """
    Base class for encrypting strings with encrypt decorators
    """
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
    """
    Base class for all encrypt decorators
    """
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


class Caesar(EncryptDecorator):
    """
    Encrypts and decrypts a string using the caesar encryption algorithm :)
    """
    KEY = "secret"

    def encrypt(self, data):
        """
        Encrypts a string using caesar encryption
        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Call decorated encrypt
        msg = self.decorated.encrypt(data)
        # Encrypt the message using caesar encryption
        encrypted = []
        for i, char in enumerate(msg):
            key_char = ord(self.KEY[i % len(self.KEY)])
            msg_char = ord(char)
            encrypted.append(chr((msg_char + key_char) % 127))
        # Return the result
        return ''.join(encrypted)

    def decrypt(self, data):
        """
        Decrypts a string using caesar decryption
        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Decrypt using caesar encryption
        decrypted = []
        for i, char in enumerate(data):
            key_char = ord(self.KEY[i % len(self.KEY)])
            enc_char = ord(char)
            decrypted.append(chr((enc_char - key_char) % 127))

        msg = ''.join(decrypted)
        # Return decorated encrypt
        return self.decorated.decrypt(msg)


class YetAnotherDraggyEncryption(EncryptDecorator):
    """
    Encrypts and decrypts a string using yet another draggy encryption algorithm
    """
    def encrypt(self, data):
        """
        Encrypts a string using caesar encryption
        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Call decorated encrypt
        msg = self.decorated.encrypt(data)
        # Decrypt using yet another draggy encryption
        encrypted = []
        for char in msg:
            encrypted += chr(int(str(ord(char))[::-1]))

        return ''.join(encrypted)

    def decrypt(self, data):
        """
        Decrypts a string using caesar decryption
        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Decrypt using yet another draggy encryption
        decrypted = []
        for char in data:
            decrypted += chr(int(str(ord(char))[::-1]))

        msg = ''.join(decrypted)
        # Return decorated decrypt
        return self.decorated.decrypt(msg)
