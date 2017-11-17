import socket

from encrypt import Base64, AES


def encrypt(data):
    return Base64(AES(data)).encrypt()


def decrypt(data):
    return Base64(AES(data)).decrypt()


class Client:
    def __init__(self, host="localhost", port=5500):
        """
        A simple client connecting to a local server
        :param host: Host to connect to
        :param port: Port used to connect to the server
        """
        self.HOST = host
        self.PORT = port

        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_socket.connect((self.HOST, self.PORT))

    def run(self):
        """
        Receives messages for eternity as long as the socket receives valid data
        """
        while 1:
            try:
                data = self.__client_socket.recv(4096)
                if data:
                    print(decrypt(data))
                else:
                    break
            except OSError as os_err:
                print("RECEIVER >> Socket Error: %s" % os_err)
                break

        self.__client_socket.close()

    def close(self):
        """
        Public method used to disconnect the client from the server
        """
        self.__client_socket.send("QUIT".encode())

    def send(self, data):
        """
        Public method used to send a message to the server
        :param data: str
        """
        self.__client_socket.send(encrypt(data))
