import base64


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
        # Call decorated encrypt
        msg = self.decorated.encrypt(data)
        return base64.b64encode(  # Encode base64
            msg.encode("utf-8")  # Encode string
        ).decode("utf-8")  # Decode string

    def decrypt(self, data):
        """
        Decodes a string using base64

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Call decorated decrypt
        msg = self.decorated.decrypt(data)

        print("Base64 decrypt: " + msg)
        return base64.b64decode(  # Decode base64
            msg
        ).decode("utf-8")  # Decode string


class Base85(EncryptDecorator):
    def __init__(self, wrapper: Encrypt):
        super().__init__(wrapper)

    def encrypt(self, data):
        """
        Encodes a string using base85

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Call decorated encrypt
        msg = self.decorated.encrypt(data)

        print("Base85 encrypt: " + msg)
        return base64.b85encode(  # Encode base85
            msg.encode("utf-8")  # Encode string
        ).decode("utf-8")  # Decode string

    def decrypt(self, data):
        """
        Decodes a string using base85

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Call decorated decrypt
        msg = self.decorated.decrypt(data)

        print("Base85 decrypt: " + msg)
        return base64.b85decode(  # Decode base85
            msg
        ).decode("utf-8")  # Decode string
