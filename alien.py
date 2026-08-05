"""
Purpose: Contains the Alien class that controls individual aliens,
 movement, and out detection.

Starter Code: Python Crash Course by Eric Matthes

Author: Novadin Abdi
"""

import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen. (me)
        self.rect.x = self.screen.get_rect().right - (2 * self.rect.width)
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.(me)
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien toward the left side of the screen. (me)"""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x