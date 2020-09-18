"""alien_invasion.py"""
import sys

import pygame

from ship import Ship
from settings import Settings

class AlienInvasion():
    """Alien Invasion class"""

    def __init__(self, screen):
        self.__screen = screen
        self.__ship = Ship(screen)

    def __check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.__ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.__ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.__ship.fire()
        elif event.key == pygame.K_q:
            self.quit()

    def __check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.__ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.__ship.moving_left = False

    def __check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                self.__check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.__check_keyup_events(event)

        self.__ship.update()

    def __update_screen(self):
        self.__screen.fill(Settings.bg_color)

        self.__ship.blitme()

        pygame.display.flip()

    def run(self):
        """Game main loop"""
        print("DEBUG: Alien Invasion is running")

        while True:
            self.__check_event()
            self.__update_screen()

    def quit(self):
        """Quit game"""
        sys.exit()
