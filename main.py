"""main.py"""

import os

import pygame

from settings import Settings
from alien_invasion import AlienInvasion as AI

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (3200, 100)

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption("Alien Invasion")

    screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
    alien_invasion = AI(screen)

    alien_invasion.run()
