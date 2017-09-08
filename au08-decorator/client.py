import socket
import threading

from decorators import *


class Client:
    def __init__(self, host="localhost", port=5500):
        """
        A simple client connecting to a local server
        :param host: Host to connect to
        :param port: Port used to connect to the server
        """
        # Define host and port
        self.HOST = host
        self.PORT = port
        # Create client socket and connect to a server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        # Set encryption method
        self.crypt = EncodeBase64(  # Encrypt using Base64
            DecodeBase64(           # Decrypt using Base64
                Coder()             # Original Coder class
            )
        )
        # Start listen and speak in 2 different threads to allow both, sending and receiving at the same time
        threading.Thread(target=self.receive).start()
        threading.Thread(target=self.send).start()

    def receive(self):
        """
        Continuously receives data from the socket
        """
        while 1:
            try:
                data = self.crypt.decode(self.client.recv(4096))
                # Check if the client has received valid data
                if not data:
                    break
            except OSError:
                break
            # Print the received message in html tags
            print(data)
        # Close the client socket if the loop is broken
        self.client.close()

    def send(self):
        """
        Sends messages whenever the client inputs text
        """
        while 1:
            try:
                msg = input('')
                self.client.send(self.crypt.encode(msg))
                # Shut down if the client wants to quit
                if msg.upper() == 'QUIT':
                    return
            # Error on send
            except OSError:
                return
            # Error on input
            except EOFError:
                return


if __name__ == '__main__':
    client = Client()
