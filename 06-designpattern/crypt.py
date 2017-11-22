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
        print("Caesar encrypt: " + msg)
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
        print("Caesar decrypt: " + data)
        decrypted = []
        for i, char in enumerate(data):
            key_char = ord(self.key[i % len(self.key)])
            enc_char = ord(char)
            decrypted.append(chr((enc_char - key_char) % 127))

        msg = ''.join(decrypted)

        return self.decorated.decrypt(msg)


class YetAnotherDraggyEncryption(EncryptDecorator):
    def __init__(self, wrapper: Encrypt):
        super().__init__(wrapper)

    def encrypt(self, data):
        """
        Encrypts a string using caesar encryption
        :param data: str
        :rtype: str
        :return: Result of the decorated instance
        """
        # Call decorated encrypt
        msg = self.decorated.encrypt(data)
        print("Draggy encrypt: " + msg)
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
        # Call decorated encrypt
        print("Draggy decrypt: " + data)
        decrypted = []
        for char in data:
            decrypted += chr(int(str(ord(char))[::-1]))

        msg = ''.join(decrypted)

        return self.decorated.decrypt(msg)
