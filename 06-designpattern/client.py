"""
Client used to communicate with other clients across a server
"""


import socket
import sys
import threading

from crypt import YetAnotherDraggyEncryption, Caesar, Encrypt


class Client:
    """
    Client used to communicate with other clients across a server
    """
    def __init__(self, host="localhost", port=5500, debug=True):
        """
        A simple client connecting to a local server
        :param host: Host to connect to
        :param port: Port used to connect to the server
        """
        # Define host and port
        self.host = host
        self.port = port
        self.debug = debug
        # Create client socket and connect to a server
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect((self.host, self.port))
        # Set encryption method
        self.__crypt = YetAnotherDraggyEncryption(  # Encrypt using yet another draggy encryption
            Caesar(  # Encrypt using Caesar
                Encrypt()  # Decorated Encrypt instance
            )
        )
        # Use a nickname
        self.nick = input("Enter a nickname: ")
        # Split data reception and input handling
        thread_listen = threading.Thread(target=self.recv)
        thread_speak = threading.Thread(target=self.send)
        # Start reception
        thread_listen.start()
        # Start speaking
        thread_speak.start()
        # Join threads before closing the process
        thread_listen.join()
        thread_speak.join()
        # Notify user
        print("Disconnected!")

    def recv(self):
        """
        Receives messages while the socket is still open

        :return: None
        """
        while 1:
            try:
                data = self.__client.recv(4096).decode()
                # Handle invalid data
                if not data:
                    break
                # Print data to stdout if in debug mode
                if self.debug:
                    print("Got unencrypted data: %s\n>>> " % data)
                    print("Decrypted data to: %s\n>>> " % self.__crypt.decrypt(data))
            # Handle socket errors
            except OSError as os_err:
                # Log error in debug mode
                if self.debug:
                    print("Error while listening: %s" % os_err)
                # Break loop
                break
        # Close socket when not listening
        self.__client.close()

    def send(self):
        """
        Lets the user send messages while the server is still open

        :return: None
        """
        while 1:
            try:
                data = input("\n>>> ")
                # Allow clean exit
                if data == "QUIT":
                    self.__client.send("QUIT".encode())
                    return
                # Log encrypted message in debug mode
                if self.debug:
                    print("Sending data: %s\n>>> " % data)
                    print("Sending encrypted data: %s\n>>> " % self.__crypt.encrypt(data))
                # Build message
                msg = self.nick + ": " + data
                # Send encrypted data to the server
                self.__client.send(self.__crypt.encrypt(msg).encode())
            # Handle socket errors
            except OSError as os_err:
                if self.debug:
                    print("Error while speaking: %s" % os_err)
                break


if __name__ == "__main__":
    if len(sys.argv) > 3:
        Client(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) > 2:
        Client(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        Client(sys.argv[1])
    else:
        Client()
