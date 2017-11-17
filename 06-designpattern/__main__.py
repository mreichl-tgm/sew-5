import multiprocessing
import time

from client import Client
from server import Server

if __name__ == "__main__":
    # Test server
    server = multiprocessing.Process(target=Server)
    server.run()
    # Wait for process to start
    time.sleep(1)
    # Test process 1
    client1 = multiprocessing.Process(target=Client)
    client1.run()
    # Wait for process to start
    time.sleep(1)
    # Test process 2
    client2 = multiprocessing.Process(target=Client)
    client2.run()
