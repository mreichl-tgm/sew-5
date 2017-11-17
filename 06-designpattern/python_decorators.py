import base64

"""
Callable->Callable decorators:
Most common in Python and very flexible.
Used to change a functions return value by wrapping it up inside the decorator.
"""


def italic(f):
    """
    A decorator which embeds a functions result into html to make it italic

    :param f: callable
    """

    def wrapper(*args):
        return "<i>" + f(*args) + "</i>"

    return wrapper


def paragraph(f):
    """
    A decorator which embeds a functions result into html to make it italic

    :param f: callable
    """

    def wrapper(*args):
        return "<p>" + f(*args) + "</p>"

    return wrapper


@italic
@paragraph
def to_html(msg):
    """
    Takes a string and wraps it into html tags

    :param msg: str
    """
    return msg


"""
Callable->Class decorators:
The Python way to decorate classes.
"""


def encode_base64(c):
    """
    A decorator overriding a class's encode method to use base64 encryption

    :param c: class
    """

    def encode(self, msg):
        """
        Encodes a string using base64

        :param self: instance
        :param msg: str
        """
        return base64.b64encode(msg.encode())

    c.encode = encode

    return c


def decode_base64(c):
    """
    A decorator overriding a class's decode method to use base64 decryption

    :param c: class
    """

    def decode(self, msg):
        """
        Decodes a string using base64

        :param self: instance
        :param msg: str
        """
        return base64.b64decode(msg.decode()).decode()

    c.decode = decode

    return c
