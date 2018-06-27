"""
======================
||  DraughtsClient  ||
======================
Template for a client to be used with the DraughtsServer module.

@author     Markus Re1 <markus@re1.at>
@version    2018-04-02
"""

from argparse import ArgumentParser
from socket import SOCK_STREAM, socket, AF_INET

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--host", help="host address to connect to (default=localhost)")
    parser.add_argument("-p", "--port", help="port to connect to (default=5050)")
    parser.add_argument("-n", "--name", help="name to use during the game")
    # Check for arguments
    args = parser.parse_args()
    # Adjust variables to given arguments
    HOST = args.host or "localhost"
    PORT = args.port or 5050
    NAME = args.name or input("Enter your name: ")
    # Create a socket connection (SOCK_STREAM means a TCP socket)
    with socket(AF_INET, SOCK_STREAM) as sock:
        # Connect to server and send name
        sock.connect((HOST, PORT))
        sock.sendall(bytes(NAME, "utf-8"))
        # Print success
        print("Connected to {}:{} as {}".format(HOST, PORT, NAME))
        # Check first response
        response = str(sock.recv(1024), "utf-8")

        request = input("Your turn: ")
        sock.sendall(bytes(request, "utf-8"))
        # Receive data from the server and shut down
        response = str(sock.recv(1024), "utf-8")
