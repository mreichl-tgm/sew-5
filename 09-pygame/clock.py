import sys
import time
import math

import pygame

from datetime import datetime

# Fonts
font_family = "Noto Sans Mono"
font_size = 16
font_size_title = 100
# Colors
color_text = (211, 216, 215)
color_background = (255, 255, 255)
color_primary = (35, 90, 133)
# Default resolution
analog_resolution = (1000, 800)
digital_resolution = (800, 400)


class Clock:
    # Contents
    caption = "Just a clock"
    # Mode
    clock_mode = 0  # 0: Analog, 1: Digital
    time_mode = 0  # 0: Second, 1: Microsecond

    def __init__(self):
        """
        Create a new clock instance, initialize pygame and start the game loop
        """
        pygame.init()  # Init PyGame libraries
        pygame.display.set_caption(self.caption)

        # Get initial mode and adjust window resolution
        if self.clock_mode == 1:  # Set resolution to digital if set by model
            self.screen = pygame.display.set_mode(digital_resolution)
        else:  # Set resolution to analog for any other case
            self.screen = pygame.display.set_mode(analog_resolution)
        # Set initial fonts
        self.font = pygame.font.SysFont(font_family, font_size)
        self.font_title = pygame.font.SysFont(font_family, font_size_title)
        # Start the event and draw loop
        # Currently merged because of pygame not giving information about correct threading on linux..
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break

            key_event = pygame.key.get_pressed()
            if key_event[pygame.K_ESCAPE]:  # `ESC` pressed
                break
            if key_event[pygame.K_a]:  # `A` pressed
                # Switch to analog mode
                self.clock_mode = 0
                self.screen = pygame.display.set_mode(analog_resolution)
            if key_event[pygame.K_d]:  # `D` pressed
                # Switch to digital mode
                self.clock_mode = 1
                self.screen = pygame.display.set_mode(digital_resolution)
            if key_event[pygame.K_p]:  # `P` pressed
                # Switch time_mode
                self.time_mode = 0 if self.time_mode else 1
            # Stop time for a constant frame rate
            start_time = time.time()
            # Draw current mode
            if self.clock_mode == 0:
                self.draw_analog()
            elif self.clock_mode == 1:
                self.draw_digital()
            else:  # React to invalid mode
                self.clock_mode = 0

            pygame.time.delay(int(100 - time.time() + start_time))
            pygame.display.update()
        # Exit after event loop is finished
        sys.exit()

    def draw_analog(self):
        """
        Draw the analog clock
        """
        # Get display size
        width, height = pygame.display.get_surface().get_size()
        center = (int(width * .5), int(height * .5))
        radius = int(width * .25)
        # (x position, y position, width, height)
        rect = (0, 0, width, height)
        pygame.draw.rect(self.screen, color_primary, rect)
        # Actual analog clock
        pygame.draw.circle(self.screen, color_text, center, radius, 2)
        pygame.draw.circle(self.screen, color_text, center, 8, 8)
        # Get line positions
        now = datetime.now() if self.time_mode else time.time()
        second = now.second if self.time_mode else now % 60
        minute = now.minute if self.time_mode else now % 3600 / 60
        hour = now.hour if self.time_mode else now % 216000 / 3600 + 1
        # Calculate positions
        second_x = int(math.cos(second * 3.14 / 30 - 3.14 / 2) * radius * .9 + center[0])
        second_y = int(math.sin(second * 3.14 / 30 - 3.14 / 2) * radius * .9 + center[1])
        minute_x = int(math.cos(minute * 3.14 / 30 - 3.14 / 2) * radius * .7 + center[0])
        minute_y = int(math.sin(minute * 3.14 / 30 - 3.14 / 2) * radius * .7 + center[1])
        hour_x = int(math.cos((hour * 30 + minute / 2) * 3.14 / 180 - 3.14 / 2) * radius * .5 + center[0])
        hour_y = int(math.sin((hour * 30 + minute / 2) * 3.14 / 180 - 3.14 / 2) * radius * .5 + center[1])
        # Draw lines
        pygame.draw.line(self.screen, color_text, center, (second_x, second_y), 4)
        pygame.draw.line(self.screen, color_text, center, (minute_x, minute_y), 6)
        pygame.draw.line(self.screen, color_text, center, (hour_x, hour_y), 8)
        # Draw marks for hours, minutes
        # Hours
        for hi in range(0, 12):
            pygame.draw.line(self.screen, color_text,
                             (center[0] + radius * .9 * math.cos(math.radians(30 * hi)),
                              (center[1] + radius * .9 * math.sin(math.radians(30 * hi)))),
                             (center[0] + radius * 1.1 * math.cos(math.radians(30 * hi)),
                              (center[1] + radius * 1.1 * math.sin(math.radians(30 * hi)))), 4)
        # Minutes
        for mi in range(0, 60):
            pygame.draw.line(self.screen, color_text,
                             (center[0] + radius * .95 * math.cos(math.radians(6 * mi)),
                              (center[1] + radius * .95 * math.sin(math.radians(6 * mi)))),
                             (center[0] + radius * 1.05 * math.cos(math.radians(6 * mi)),
                              (center[1] + radius * 1.05 * math.sin(math.radians(6 * mi)))))
        # Draw hour indicators
        hour_surface_3 = self.font.render("3", 1, color_text)
        hour_rect_3 = hour_surface_3.get_rect()
        hour_rect_3.x = center[0] + radius * 1.25
        hour_rect_3.y = center[1] - hour_rect_3.height / 2
        self.screen.blit(hour_surface_3, hour_rect_3)

        hour_surface_6 = self.font.render("6", 1, color_text)
        hour_rect_6 = hour_surface_6.get_rect()
        hour_rect_6.x = center[0] - hour_rect_6.width / 2
        hour_rect_6.y = center[1] + radius * 1.25 - hour_rect_6.height / 2
        self.screen.blit(hour_surface_6, hour_rect_6)

        hour_surface_9 = self.font.render("9", 1, color_text)
        hour_rect_9 = hour_surface_9.get_rect()
        hour_rect_9.x = center[0] - radius * 1.25 - hour_rect_9.width
        hour_rect_9.y = center[1] - hour_rect_9.height / 2
        self.screen.blit(hour_surface_9, hour_rect_9)

        hour_surface_12 = self.font.render("12", 1, color_text)
        hour_rect_12 = hour_surface_12.get_rect()
        hour_rect_12.x = center[0] - hour_rect_12.width / 2
        hour_rect_12.y = center[1] - radius * 1.25 - hour_rect_12.height / 2
        self.screen.blit(hour_surface_12, hour_rect_12)

        # Print key command list
        keys_text = "Press 'D' for digital clock."
        keys_surface = self.font.render(keys_text, 1, color_text)
        keys_rect = keys_surface.get_rect()
        keys_rect.x = width * .1
        keys_rect.y = height * .1
        self.screen.blit(keys_surface, keys_rect)
        # Print mode command list
        mode_text = "Press 'P' to smooth seconds."
        mode_surface = self.font.render(mode_text, 1, color_text)
        mode_rect = keys_surface.get_rect()
        mode_rect.x = width * .1
        mode_rect.y = height * .1 + 2 * font_size
        self.screen.blit(mode_surface, mode_rect)

    def draw_digital(self):
        """
        Draw the digital clock using the settings defined in self
        """
        # self.screen = pygame.display.set_mode(self.digital_resolution)
        # Get reference to screen rect
        screen_rect = self.screen.get_rect()
        # Print time
        time_text = str(datetime.now().time())[:-7]
        time_surface = self.font_title.render(time_text, 1, color_text)
        time_rect = time_surface.get_rect()
        time_rect.center = screen_rect.center
        # Get display size
        width, height = pygame.display.get_surface().get_size()
        # (x position, y position, width, height)
        rect = (0, 0, width, height)
        pygame.draw.rect(self.screen, color_primary, rect)
        self.screen.blit(time_surface, time_rect)
        # Print key command list
        keys_text = "Press 'A' for analog clock"
        keys_surface = self.font.render(keys_text, 1, color_text)
        keys_rect = keys_surface.get_rect()
        keys_rect.x = width * 0.1
        keys_rect.y = height * 0.1
        self.screen.blit(keys_surface, keys_rect)


if __name__ == "__main__":
    Clock()
