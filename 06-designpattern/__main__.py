import multiprocessing

from client import Client
from server import Server

if __name__ == "__main__":
    server = multiprocessing.Process(target=Server)
    server.run()

    client1 = multiprocessing.Process(target=Client)
    client1.run()

    client2 = multiprocessing.Process(target=Client)
    client2.run()
