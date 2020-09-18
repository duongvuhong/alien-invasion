"""ship.py"""

import pygame
from pygame.sprite import Group

from settings import Settings
from bullet import Bullet

class Ship(pygame.sprite.Sprite):
    """Ship class"""

    def __init__(self, screen):
        super().__init__()

        self.__bullets = Group()

        self.__screen = screen
        self.__screen_rect = self.__screen.get_rect()

        # Init a ship at bottom center.
        self.__ship_image = pygame.image.load(Settings.ship_image)
        self.__ship_rect = self.__ship_image.get_rect()
        self.__ship_rect.centerx = self.__screen_rect.centerx
        self.__ship_rect.bottom = self.__screen_rect.bottom

        self.__center = float(self.__ship_rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.__ship_rect.right < self.__screen_rect.right:
            self.__center += Settings.ship_speed_factor
        if self.moving_left and self.__ship_rect.left > 0:
            self.__center -= Settings.ship_speed_factor

        # Update rect object from self.center.
        self.__ship_rect.centerx = self.__center

        self.__bullets.update()

    def blitme(self):
        """Draw the ship at its current location."""
        self.__screen.blit(self.__ship_image, self.__ship_rect)

        for bullet in self.__bullets.sprites():
            bullet.draw_bullet()

    def fire(self):
        """Fire a bullet"""
        if len(self.__bullets) < Settings.bullets_allowed:
            print("Fire")
            self.__bullets.add(Bullet(self.__screen, self.__ship_rect))
