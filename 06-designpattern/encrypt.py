import base64
from abc import ABC, abstractmethod

from Crypto.Cipher.AES import new, MODE_OPENPGP


class Encrypt(ABC):
    @abstractmethod
    def encrypt(self):
        """ Abstract method to encrypt an object """

    @abstractmethod
    def decrypt(self):
        """ Abstract method to encrypt an object """


class EncryptDecorator(Encrypt):
    """ Inheriting classes decorate wrapped objects """

    def __init__(self, wrapper):
        """
        Takes an object and saves it for the decorating classes
        :param wrapper: Object to en- or decrypt
        """
        self.wrapper = wrapper

    def encrypt(self):
        """
        Returns the wrapped object without encryption
        :return: Wrapped object
        """
        return self.wrapper

    def decrypt(self):
        """
        Returns the wrapped object without decryption
        :return: Wrapped object
        """
        return self.wrapper


class Base64(EncryptDecorator):
    def __init__(self, wrapper):
        super().__init__(wrapper)

    def encrypt(self):
        return base64.b64encode(self.wrapper.encrypt())

    def decrypt(self):
        return base64.b64decode(self.wrapper.decrypt())


class AES(EncryptDecorator):
    def __init__(self, wrapper):
        super().__init__(wrapper)

        self.SUITE = new("default", MODE_OPENPGP)

    def encrypt(self):
        self.wrapper = self.SUITE.encrypt(self.wrapper.encrypt())

    def decrypt(self):
        self.wrapper = self.SUITE.decrypt(self.wrapper.decrypt())
