"""
Main script to test a server with two clients in one click
"""


import multiprocessing
import time

from client import Client
from server import Server

if __name__ == "__main__":
    # Test server
    multiprocessing.Process(target=Server).run()
    # Wait for process to start
    time.sleep(1)
    # Test process 1
    multiprocessing.Process(target=Client).run()
    # Wait for process to start
    time.sleep(1)
    # Test process 2
    multiprocessing.Process(target=Client).run()
