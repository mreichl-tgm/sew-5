import random
import sys
import threading
import time


class Snowflake(threading.Thread):
    cols = 20
    rows = 10
    fallen = 0
    lock = threading.Lock()

    def __init__(self, x, e=None):
        super().__init__()

        self.x = x if x else 0
        self.y = 0
        self.e = e

    def run(self):
        # Check if event exists and block while it is not set
        while self.e and not self.e.isSet():
            pass

        while self.y < Snowflake.rows - 2:
            self.y += 1
            # Bounce from walls
            if self.x <= 0:
                self.x += 1
            elif self.x >= Snowflake.cols - 1:
                self.x -= 1

            x = random.randint(-1, 1)
            if x == 0:  # Fall down if not falling to any site
                self.y += 1
            else:       # Else move in any direction
                self.x += x
            # Wait a second
            time.sleep(0.5)

        with Snowflake.lock:
            Snowflake.fallen += 1


if __name__ == "__main__":
    threads = []
    # Create 10 snowflakes by default
    snowflakes = 20
    event = threading.Event()

    def display():
        footer = "=" * Snowflake.cols

        while len(threads) > 0:
            grid = []           # Make grid
            for row in range(Snowflake.rows):
                row = []        # Make rows
                for col in range(Snowflake.cols):
                    row += " "  # Make cols
                grid.append(row)

            for t in threads:
                grid[t.y][t.x] = "*"

            for row in grid:
                row_string = ""
                for col in row:
                    row_string += str(col)

                print("# " + row_string + " #")

            print("# " + footer + " # Fallen: " + str(Snowflake.fallen))

            time.sleep(0.5)


    if len(sys.argv) > 1:
        snowflakes = sys.argv[1]

    for i in range(snowflakes):
        snowflake = Snowflake(random.randint(0, Snowflake.cols - 1))
        threads.append(snowflake)
    # Start display thread and make it a daemon
    display_thread = threading.Thread(target=display)
    display_thread.start()

    for thread in threads:
        thread.start()

    time.sleep(1)
    event.set()

    for thread in threads:
        thread.join()

    time.sleep(1)
    threads = []
