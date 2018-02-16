import datetime
import sys
import threading
import time

import pygame

FONT_SIZE = 100
# Colors
TEXT = (211, 216, 215)
BACKGROUND = (25, 37, 50)
PRIMARY = (35, 90, 133)

resolution = (800, 400)


class Clock:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("A clock")

        self.screen = pygame.display.set_mode(resolution)
        self.font = pygame.font.SysFont("Noto Sans Mono", FONT_SIZE)

        self.closed = 0

        event_loop = threading.Thread(target=self.event_loop)
        event_loop.start()

        threading.Thread(target=self.draw_loop).start()

        event_loop.join()
        sys.exit()

    def draw_loop(self):
        while not self.closed:
            # Stop time for a constant frame rate
            start_time = time.time()

            self.screen.fill(BACKGROUND)
            self.draw_digital()

            pygame.time.delay(int(100 - time.time() + start_time))
            pygame.display.flip()

    def event_loop(self):
        while not self.closed:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                self.closed = 1

    def draw_digital(self):
        text = str(datetime.datetime.now().time())[:-7]
        # Center text: http://www.poketcode.com/en/pygame/text/index.html
        screen_rect = self.screen.get_rect()
        text_surface = self.font.render(text, 1, TEXT)
        text_rect = text_surface.get_rect()
        text_rect.center = screen_rect.center
        # Get display size
        width, height = pygame.display.get_surface().get_size()
        # (x position, y position, width, height)
        rect = (width * 0.1, height * 0.1, width * 0.8, height * 0.8)
        pygame.draw.rect(self.screen, PRIMARY, rect)

        self.screen.blit(text_surface, text_rect)

    """

        key_event = pygame.key.get_pressed()

    def draw(self):
        pygame.draw.ellipse(self.screen, self.clockMarginColor)

    def draw_foreground(self):
        if self.mode == 1:
            pygame.draw.ellipse(self.screen)

    def drawCursor(self, color, width, length, position, scale, start=0):
        start = (start if not start else self.window.center)

    def drawDigital(self):
        basicfont = pygame.font.SysFont("")
    """


if __name__ == "__main__":
    Clock()
