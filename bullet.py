"""bullet.py"""

import pygame

from settings import Settings

class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, screen, ship_rect):
        """Create a bullet object, at the ship's current position."""
        super().__init__()

        self.__screen = screen

        self.__bullet_rect = pygame.Rect(0, 0, Settings.bullet_width, Settings.bullet_height)
        self.__bullet_rect.centerx = ship_rect.centerx
        self.__bullet_rect.top = ship_rect.top

        # Store a decimal value for the bullet's position.
        self.y = float(self.__bullet_rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= Settings.bullet_speed_factor
        self.__bullet_rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.__screen, Settings.bullet_color, self.__bullet_rect)
