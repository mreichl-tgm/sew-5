import random
import sys
import threading
import time


class Snowflake(threading.Thread):
    cols = 10
    rows = 10
    fallen = 0

    def __init__(self, x):
        super().__init__()

        self.x = x if x else 0
        self.y = 0

    def run(self):
        while self.y < Snowflake.rows:
            self.y += 1
            # Change column
            if self.x <= 0:
                self.x += 1
            elif self.x >= Snowflake.cols - 1:
                self.x -= 1
            else:
                self.x += random.randint(-1, 1)
            # Wait a second
            time.sleep(1)

        with threading.Lock():
            Snowflake.fallen += 1


if __name__ == "__main__":
    def display():
        footer = "=" * Snowflake.cols

        while True:
            grid = [[" " for col in range(Snowflake.cols)] for row in range(Snowflake.rows + 1)]

            for t in threads:
                grid[t.y][t.x] = "*"

            for row in grid:
                row_string = ""
                for col in row:
                    row_string += str(col)

                print("# " + row_string + " #")

            print("# " + footer + " # Fallen: " + str(Snowflake.fallen))

            time.sleep(1)


    threads = []
    # Create 10 snowflakes by default
    snowflakes = 10

    if len(sys.argv) > 1:
        snowflakes = sys.argv[1]

    for i in range(snowflakes):
        snowflake = Snowflake(random.randint(0, Snowflake.cols - 1))

        threads.append(snowflake)
    # Start display thread and make it a daemon
    display_thread = threading.Thread(target=display)
    display_thread.daemon = True
    display_thread.start()

    for thread in threads:
        time.sleep(1)
        thread.start()

    for thread in threads:
        thread.join()
