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
            msg.encode("ASCII")  # Encode string
        ).decode("ASCII")  # Decode string

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
            msg.encode("ASCII")  # Encode string
        ).decode("ASCII")  # Decode string


class Caesar(EncryptDecorator):
    def __init__(self, wrapper: Encrypt):
        super().__init__(wrapper)
        self.key = "secret"

    def encrypt(self, data):
        """
        Encrypts a string using caesar encryption

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Call decorated encrypt
        msg = self.decorated.encrypt(data)
        print("Caesar encrypt: " + str(msg))
        encrypted = []
        for i, char in enumerate(msg):
            key_char = ord(self.key[i % len(self.key)])
            msg_char = ord(char)
            encrypted.append(chr((msg_char + key_char) % 127))

        return ''.join(encrypted)

    def decrypt(self, data):
        """
        Decrypts a string using caesar decryption

        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Call decorated encrypt
        msg = self.decorated.decrypt(data)
        print("Caesar decrypt: " + str(msg))
        decrypted = []
        for i, char in enumerate(msg):
            key_char = ord(self.key[i % len(self.key)])
            enc_char = ord(char)
            decrypted.append(chr((enc_char - key_char) % 127))

        return ''.join(decrypted)
