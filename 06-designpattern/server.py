"""
Socket server providing a communication interface for client sockets
"""


import socket
import sys
import threading


class Server:
    """
    Socket server providing a communication interface for client sockets

    """
    def __init__(self, host="localhost", port=5500):
        """
        A python Server using sockets
        :param port: Port used for the server
        :param host: Host used for the server
        """
        # Defining Host, Port and Client List
        self.host = host
        self.port = port
        self.__clients = []
        # Create server socket, bind it to host and port, start listening
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((self.host, self.port))
        self.__server.listen(10)
        # Log success
        print("Server running on %s: %s)" % (self.host, self.port))
        # Count connected sockets to set ids
        counter = 0
        # Accept clients, add them to the client list and start a client_handler using their socket
        try:
            while 1:
                print("Waiting...")
                # Accept a client connection
                (client_socket, address) = self.__server.accept()
                self.__clients.append(client_socket)
                # Start a new handler thread for each client
                handler = threading.Thread(target=self.client_handler,
                                           args=(client_socket, counter))
                handler.start()
                # Log connected clients
                print('Client connected at', address)
                # Increase counter
                counter += 1
        # Except a socket error which results in a closed server
        except socket.error:
            # Close clients if possible
            for client in self.__clients:
                client.close()
            # Terminate process with exit code 1
            sys.exit("Server was closed due to %s!" % socket.error)

    def client_handler(self, sock, client_id):
        """
        Receives and handles data from the client.
        If the socket runs into an error it is also removed from the client list.

        :param sock: Clients socket
        :param client_id: Clients ID
        """
        while 1:
            try:
                data = sock.recv(4096)
                # Check if the client sends valid data or wants to quit
                if not data or data.decode().upper() == "QUIT":
                    break
                # Log data
                print(data)
                # Broadcast valid data
                self.broadcast(sock, data)
            except socket.error:
                # Log error
                print("Client%s ran into an error: %s" % (client_id, socket.error))
                break

        # Log disconnect
        print("Client%s is offline" % client_id)
        # Close socket if not already closed
        sock.close()
        # Remove socket
        self.__clients.remove(sock)

    def broadcast(self, sock, data):
        """
        Broadcast data to all other clients
        """
        for client_socket in self.__clients:
            # Exclude server and sending client
            if client_socket is sock:
                continue
            # Send data
            client_socket.send(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        Server(sys.argv[1])
    elif len(sys.argv) > 2:
        Server(sys.argv[1], sys.argv[2])
    else:
        Server()
