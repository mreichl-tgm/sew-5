import socket
import sys
import threading

from crypt import Base64, AES, Encrypt


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
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect((self.HOST, self.PORT))
        # Set encryption method
        self.CRYPT = Base64(  # Encrypt using Base64
            AES(  # Encrypt using AES
                Encrypt()  # Decorated Encrypt instance
            )
        )
        # Helper variable to close threads if necessary
        self.open = True
        # Split data reception and input handling
        thread_listen = threading.Thread(target=self.recv)
        thread_speak = threading.Thread(target=self.send)

        thread_listen.start()
        thread_speak.start()
        # Join threads before closing the process
        thread_listen.join()
        thread_speak.join()

    def recv(self):
        while self.open:
            try:
                data = self.__client.recv(4096).decode()
                # Handle invalid data
                if not data:
                    break
                # Print data to stdout
                print(self.CRYPT.decrypt(data))
            # Handle socket errors
            except OSError as os_err:
                print("Error while listening: %s" % os_err)
                break
        # Close socket when not listening
        self.__client.close()

    def send(self):
        while self.open:
            try:
                data = input(">>> ")
                # Allow clean exit
                if data == "QUIT":
                    self.close()
                # Send encrypted data to the server
                self.__client.send(self.CRYPT.encrypt(data)).encode()
            # Handle socket errors
            except OSError as os_err:
                print("Error while speaking: %s" % os_err)
                break

    def close(self):
        """
        Public method used to disconnect the client from the server
        """
        self.__client.send("QUIT".encode())
        self.open = False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            Client(sys.argv[1], sys.argv[2])
        else:
            Client(sys.argv[1])
    else:
        Client()
