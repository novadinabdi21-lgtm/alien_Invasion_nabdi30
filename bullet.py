"""
Purpose: Contains the Bullet class that manages bullets movement,
 and drawing for the player's ship.

Starter Code: Python Crash Course by Eric Matthes

Author: Novadin Abdi
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create the bullet image.(me)
        self.image = pygame.Surface(
            (self.settings.bullet_width, self.settings.bullet_height)
        )
        self.image.fill(self.color)

        # Create a bullet rect at (0, 0) and then set correct position.(me)
        self.rect = self.image.get_rect()
        self.rect.midleft = ai_game.ship.rect.midright

        # Store the bullet's position as a float.(me)
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen.(me)"""
        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed

        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)