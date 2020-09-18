"""alien.py"""

import pygame

ALIEN_IMAGE = 'images/alien.png'

class Alien(pygame.sprite.Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, screen):
        """Initialize the alien, and set its starting position."""
        super().__init__()

        self.__screen = screen

    def ___check_edges(self):
        """Return True if alien is at edge of screen."""

    def update(self):
        """Move the alien right or left."""

    def blitme(self):
        """Draw the alien at its current location."""
