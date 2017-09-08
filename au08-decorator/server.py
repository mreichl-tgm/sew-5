import socket
import threading

from decorators import *


class Server:
    def __init__(self, host="localhost", port=5500):
        """
        The socket server responsible for client communication.
        :param port: Port used for the server
        :param host: Host used for the server
        """
        super().__init__()
        # Define host, port and and client list
        self.HOST = host
        self.PORT = port
        self.CLIENTS = []
        # Create the server socket, bind it to HOST and PORT, start listening
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()
        # Log success
        print("Server running on %s: %s)" % (self.HOST, self.PORT))
        # Set encryption method
        self.crypt = EncodeBase64(  # Encrypt using Base64
            DecodeBase64(           # Decrypt using Base64
                Coder()             # Original Coder class
            )
        )
        # Accept clients, add them to the client list and start a client_handler using their socket.
        try:
            while 1:
                print("Waiting...")
                # Accept a client connection
                (client, address) = self.server_socket.accept()
                self.CLIENTS.append(client)
                # Start a new handler thread for each client
                handler = threading.Thread(target=self.client_handler, args=(client,))
                handler.start()
                # Log connected clients
                print('Client connected at', address)
                self.broadcast(client, self.crypt.encode('Client connected at' + str(address)))
        except socket.error:
            print('Server was closed!')
            return

    def client_handler(self, sock):
        """
        Receives and handles data from the client.
        If the socket runs into an error it is also removed from the client list.

        :param sock: socket
        """
        while 1:
            try:
                data = sock.recv(4096)
                # Check if the client sends valid data
                if not data:
                    break
                # Send the received content to all other clients
                self.broadcast(sock, data)
            except socket.error:
                break
        # Close the client's socket and remove it from the client list
        print("Client disconnected!")
        sock.close()
        self.CLIENTS.remove(sock)

    def broadcast(self, sock, msg):
        """
        Send a message to all clients other than the server socket and the client socket from which the data
        is received.
        :param sock: socket
        :param msg: str
        """
        for s in self.CLIENTS:
            if s != self.server_socket and s != sock:
                s.send(msg)


if __name__ == '__main__':
    server = Server()
