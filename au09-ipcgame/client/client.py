import socket
import sys


def receive(client):
    """
    This method receives the servers data and converts it into a readable map using a list of strings.
    Because in Python a string is also an iterable, the lists index can be used as a coordinate system.

    All fields and objects are identified by different letters:
        FieldType.GRASS     => 'G'
        FieldType.LAKE      => 'L'
        FieldType.FOREST    => 'F'
        FieldType.MOUNTAIN  => 'M'
        FieldType.CASTLE1   => 'C'
        FieldType.CASTLE2   => 'C'
        self.bomb[0]        => 'B'
        self.bomb[1]        => 'B'
        undefined           => ' '

    Using this information a string can be converted to this:
    fields = [[GGFGG], [LGCLF], [GGGLF], [GLBFF], [GGGGL]]

    And be used as a map like this:
    |---|-----------|---
    |   | 0 1 2 3 4 | x
    |---|-----------|---
    | 0 | G G F G G
    | 1 | L G C L F
    | 2 | G G G L F
    | 3 | G L B F F
    | 4 | G G G G L
    |---|
    | y |

    :param client: Socket
    :return: list
    """
    # Update the clients turn and log it
    Client.turn += 1
    print("\nTURN >> ", Client.turn)
    # Receive data from the input stream
    data = client.recv(1024).decode()
    # The data_fields variable will receive the input as rows of strings
    data_fields = []
    # Because most fields are separated by either a whitespace or the bomb, the received fields have to be filtered.
    # The new field list will then be returned as the clients map.
    fields = []
    # If the client did not receive anything the value of data will be null, which means the connection has been closed.
    # In this case the function should return without passing anything.
    if not data:
        print("Connection closed")
        return
    # The data received from the server can be decoded into a string. A valid string has either 18, 50 or 98 fields,
    # which is equal the number of fields separated by either whitespaces or bombs.
    # The string has a length of:
    # 18 letters inside a forest
    if len(data) == 18:
        data_fields += [data[0:6]]
        data_fields += [data[6:12]]
        data_fields += [data[12:18]]
    # 50 letters on grass
    elif len(data) == 50:
        data_fields += [data[0:10]]
        data_fields += [data[10:20]]
        data_fields += [data[20:30]]
        data_fields += [data[30:40]]
        data_fields += [data[40:50]]
    # and 98 letters on mountains
    elif len(data) == 98:
        data_fields += [data[0:14]]
        data_fields += [data[14:28]]
        data_fields += [data[28:42]]
        data_fields += [data[42:56]]
        data_fields += [data[56:70]]
        data_fields += [data[70:84]]
        data_fields += [data[84:98]]
    # If the string does not match any of those it shall also return nothing and print an exception.
    else:
        print("Could not read:", data)
        return
    # Now that all data is converted into fields, those fields have to be filtered.
    # This happens by replacing all whitespaces and all fields after bombs with an empty string.
    for row in data_fields:
        row = row.replace(" ", "")
        for col, c in enumerate(row):
            if c == "B":
                row = row[:col - 1] + c + row[col + 1:]
        fields.append(row)
    # If the function does not run into an error, the fields will be returned
    return fields


class Direction:
    """
    To easily manage different connections on a coordinate system the direction class provides 4 directions.
    Each direction has both a command and a vector [x, y].
    """
    UP = {"cmd": "up", "vec": [-1, 0]}
    RIGHT = {"cmd": "right", "vec": [0, 1]}
    DOWN = {"cmd": "down", "vec": [1, 0]}
    LEFT = {"cmd": "left", "vec": [0, -1]}


class Client:
    # Constants and static variables
    SPAWN = [0, 0]
    turn = 0

    def __init__(self, host="localhost", port=5050):
        """
        The client connects to the given host using the given port and plays the game.
        """
        # Set host and port
        self.HOST = host
        self.PORT = port
        # Initialize values for locations
        self.fields = None
        self.castle = None
        self.bomb = None
        self.has_bomb = False
        # Position relative to the players spawn
        self.rel_pos = [0, 0]
        # Socket initialization
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.HOST, self.PORT))
            # The server requires a name to function
            username = input("Name: ")
            self.client.send(username.encode())
        # In case the connection fails the client has to shut down
        except IOError:
            print("Connection failed!")
            return
        # The first handshake ensures a stable connection
        data = self.client.recv(1024).decode()
        # Check for connectivity and return if no data is received
        if not data or not data == "OK":
            self.client.close()
            return
        # Start the searching process
        self.search()

    def receive(self):
        """
        Receives data for the player and scans it. If no data is received the program is shut down.
        """
        # Receive new fields
        self.fields = receive(self.client)
        # If no data is received shut down the program
        if not self.fields:
            print("Client disconnected!")
            sys.exit(0)
        # Scan the environment
        self.scan()

    def check(self, field):
        """
        Checks whether or not the player can walk onto this field

        :param field: list
        :return: bool
        """
        # The player's position is always the middle row and column
        pos = int(len(self.fields) / 2)
        # The index of the field the player is moving towards is equal the direction's vector's values added to the
        # coordinates of the player's position.
        # If this field holds the letter "L" it is a lake and therefore not passable.
        if self.fields[pos + field["vec"][0]][pos + field["vec"][1]] == "L":
            return False
        return True

    def scan(self):
        """
        Scan the environment for bombs and castles.
        If the bomb has been found the player shall move towards it.
        If both the bomb and the castle have been found the player moves to the castle.

        :return:
        """
        pos = int(len(self.fields) / 2)
        # For each row in the given fields
        for y in range(len(self.fields)):
            # And for each of these row's columns
            for x, col in enumerate(self.fields[y]):
                # The field's relative position is saved so it can later be found if needed
                field = [
                    self.rel_pos[0] + y - pos,  # Do not ask why but only this one time you have to mix up x and y
                    self.rel_pos[1] + x - pos   # Tell me if you know why this happens...
                ]
                # Because the territory repeats the relative positions have to be adjusted
                if field[0] > 9:
                    field[0] -= 10
                if field[0] < 0:
                    field[0] += 10
                if field[1] > 9:
                    field[1] -= 10
                if field[1] < 0:
                    field[1] += 10
                # Check if the player has found the bomb and save its location
                if not self.bomb and col == "B":
                    self.bomb = field
                    print("The bomb was found at")
                    print("-> Absolute Position:", [x, y])
                    print("-> Relative Position:", self.bomb)
                # Check if the player has found a castle different from the one he spawned at and save its location
                if not self.castle and col == "C" and field != Client.SPAWN:
                    self.castle = field
                    print("Enemies castle was found!")
                    print("-> Absolute Position:", [x, y])
                    print("-> Relative Position:", self.castle)

    def move_to(self, field):
        """
        Moves towards a given relative direction by comparing it with the player's relative position

        :param field: list
        """
        # Look for the field while the player is not standing right on it
        while self.rel_pos != field:
            self.receive()
            # Check if the player has to move to the right
            if self.rel_pos[1] < field[1]:
                self.move(Direction.RIGHT)
            # else check left
            elif self.rel_pos[1] > field[1]:
                self.move(Direction.LEFT)
            # else check upwards
            elif self.rel_pos[0] > field[0]:
                self.move(Direction.UP)
            # else check downwards
            elif self.rel_pos[0] < field[0]:
                self.move(Direction.DOWN)
        # Log success
        print("Target", field, "found!")

    def move(self, direction):
        """
        Moves into a given direction while checking for lakes

        :param direction: Direction
        """
        # Check if the chosen direction is clear
        if self.check(direction):
            # Send the directions command to the server
            self.client.send(direction["cmd"].encode())
            # Increase the relative position by the direction's vector's values.
            self.rel_pos[0] += direction["vec"][0]
            self.rel_pos[1] += direction["vec"][1]
            # Because the territory repeats the relative positions have to be adjusted
            if self.rel_pos[0] > 9:
                self.rel_pos[0] -= 10
            if self.rel_pos[0] < 0:
                self.rel_pos[0] += 10
            if self.rel_pos[1] > 9:
                self.rel_pos[1] -= 10
            if self.rel_pos[1] < 0:
                self.rel_pos[1] += 10
            # Log the direction the player moved towards
            print(direction["cmd"])
            print("I am at:")
            print("-> Relative Position:", self.rel_pos)
        # If the direction is blocked by a lake, the player shall try to avoid it
        else:
            print("Lake ahead!")
            self.avoid(direction)

    def search(self):
        """
        Search the environment for bombs and castles while receiving data from the server.

        :return:
        """
        while 1:
            # the player iterates over each row in the environment by moving right for
            # every field in a row and then moving down.
            for col in range(8):
                # If the player has found the bomb through a scan
                if self.bomb and not self.has_bomb:
                    self.move_to(self.bomb)
                    # If the player is at the bombs location he shall try to find the enemy castle
                    self.has_bomb = True
                    print("The bomb has been obtained!")
                # Check if the player has found both castle and bomb and if so move towards it
                elif self.castle and self.has_bomb:
                    print("Both bomb and castle were found!")
                    self.move_to(self.castle)
                # In case nothing happened just move right
                else:
                    # Receive fields
                    self.receive()
                    # Move right
                    self.move(Direction.RIGHT)
            # If the loop is done the player should move to the next row.
            # Because the player can see at least on field ahead, moving down two fields works just the same.
            for i in range(2):
                # Receive fields
                self.receive()
                # Otherwise the player can move down
                self.move(Direction.DOWN)

    def avoid(self, direction):
        """
        Avoid an obstacle located on the given direction

        :param direction:
        """
        # Saves another direction the player can use get around the lake
        alternative = None
        # Saves the opposite direction the player used so he can get back to his old path
        reverse = None
        # If the player is moving vertically, which implies that the x vector is 0, he can either walk up or down
        if direction["vec"][0] == 0:
            # Check if the player can walk upwards
            if self.check(Direction.UP):
                alternative = Direction.UP
                reverse = Direction.DOWN
            # Check if the player can walk downwards
            if self.check(Direction.DOWN):
                alternative = Direction.DOWN
                reverse = Direction.UP
        # If the x vector is other than 0 the player is moving horizontally and shall either walk left or right
        else:
            # Check if the player can walk left
            if self.check(Direction.LEFT):
                alternative = Direction.LEFT
                reverse = Direction.RIGHT
            # Check if the player can walk right
            if self.check(Direction.RIGHT):
                alternative = Direction.RIGHT
                reverse = Direction.LEFT
        # Now the player knows where to go and walk in this direction
        self.move(alternative)
        # He then has to walk two fields in the original direction to get past the obstacle
        for i in range(2):
            self.receive()
            self.move(direction)
        # After that he just walks back to the road
        self.receive()
        self.move(reverse)


if __name__ == "__main__":
    # Set default values for host and port, in case the user did not give any arguments
    _host = "localhost"
    _port = 5050
    # If the number of arguments is greater than 1 (more than just the name of the python file),
    # the argument at index 1 will be the host.
    if len(sys.argv) > 1:
        _host = sys.argv[1]
    else:
        print("Falling back to default host:", _host)
    # The third argument at index 2 if given will be the port.
    # The port number should be a number so it might throw a ValueError.
    if len(sys.argv) > 2:
        try:
            _port = int(sys.argv[2])
        except ValueError:
            print("No valid port!")
            print("Falling back to default port: 5050")
    # After checking the arguments a new instance of the client class can be created using the given host and port.
    Client(host=_host, port=_port)
