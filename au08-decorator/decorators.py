import base64


class Coder:
    def encode(self, msg):
        """
        Default encode method for Coder class

        :param msg: str
        """
        return msg

    def decode(self, msg):
        """
        Default decode method for Coder class

        :param msg: str
        """
        return msg


class CoderDecorator(Coder):
    def __init__(self, decorated):
        self.decorated = decorated

    def encode(self, msg):
        """
        Calls the default encode method in case it is not implemented

        :param msg: str
        """
        return self.decorated.encode(msg)

    def decode(self, msg):
        """
        Calls the default decode method in case it is not implemented

        :param msg: str
        """
        return self.decorated.decode(msg)


class EncodeBase64(CoderDecorator):
    def encode(self, msg):
        """
        Encodes a string using base64

        :param self: instance
        :param msg: str
        """
        return base64.b64encode(
            # Call decorated encode
            self.decorated.encode(msg.encode())
        )


class DecodeBase64(CoderDecorator):
    def decode(self, msg):
        """
        Decodes a string using base64

        :param self: instance
        :param msg: str
        """
        return base64.b64decode(
            # Call decorated decode
            self.decorated.decode(msg)
        ).decode()
