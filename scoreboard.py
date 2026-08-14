"""
Purpose: Contains the Scoreboard class that displays the score,
high score, and remaining lives.

Starter Code: Python Crash Course by Eric Matthes

Author: Novadin Abdi
"""

import pygame.font


class Scoreboard:
    """A class to report scoring information and remaining lives."""

    def __init__(self, ai_game):
        """Initialize the scoreboard."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_ships(self):
        """Turn the remaining lives into a rendered image."""
        ships_str = f"Lives: {self.stats.ships_left}"
        self.ships_image = self.font.render(
            ships_str, True, self.text_color)

        self.ships_rect = self.ships_image.get_rect()
        self.ships_rect.left = 20
        self.ships_rect.top = 20

    def show_score(self):
        """Draw the score, high score, and remaining lives."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.ships_image, self.ships_rect)