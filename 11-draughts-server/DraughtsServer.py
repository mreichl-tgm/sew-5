"""
======================
||  DraughtsServer  ||
======================
A socket server providing commands to interact with a draughts game.
A single server may only serve exactly 2 clients.

@author     Markus Re1 <markus@re1.at>
@version    2018-04-02
"""

from argparse import ArgumentParser
from socketserver import TCPServer, BaseRequestHandler


class DraughtsHandler(BaseRequestHandler):
    """
    Handles all interaction with the draughts game
    by receiving, processing and responding to client requests.
    """
    name = "Client"

    def handle(self):
        """ Main method for socket interaction. """
        # Get name
        self.name = self.request.recv(1024).strip()

        print("{} wrote:".format(self.client_address[0]))

        # Just send back the same data
        self.request.sendall(BOARD)
        # Announce the winner
        self.request.sendall("{} wins!".format(self.name))

    def finish(self):
        """ Clean up after the socket is closed """
        self.request.sendall("{} disconnected!".format(self.name))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--host", help="host address to connect to (default=localhost)")
    parser.add_argument("-p", "--port", help="port to connect to (default=5050)")
    parser.add_argument("-g", "--german", help="use german draughts rules", action="store_true")
    # Check for arguments
    args = parser.parse_args()
    # Adjust variables to given arguments
    HOST = args.host or "localhost"
    PORT = args.port or 5050
    # Save locale to adjust game rules
    SIZE = 8 if args.german else 10
    ROWS = 3 if args.german else 4
    BOARD = [
        # Place tiles for player 1
        ROWS * [[1, 0][i % 2] for i in range(SIZE)],
        # Place other tiles
        (SIZE - 2 * ROWS) * [0],
        # Place tiles for player 2
        ROWS * [[1, 0][i % 2] for i in range(SIZE)]
    ]
    # Start an serve a TCP socket server which accepts clients using DraughtsHandler instances
    with TCPServer((HOST, PORT), DraughtsHandler) as server:
        print("Server running on {}:{}".format(HOST, PORT))
        server.serve_forever()
