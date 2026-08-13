"""
Purpose: Contains the Scoreboard class that displays the score,
high score, and remaining lives.

Starter Code: Python Crash Course by Eric Matthes

Author: Novadin Abdi
"""

import pygame.font


class Scoreboard:
    """A class to report scoring information. (me)"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes. (me)"""
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
        """Turn the score into a rendered image. (me)"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image. (me)"""
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_ships(self):
        """Prepare images showing the remaining lives. (me)"""
        self.ship_images = []

        for ship_number in range(self.stats.ships_left):
            ship = self.ai_game.ship.image
            self.ship_images.append(ship)

    def show_score(self):
        """Draw the score, high score, and remaining lives. (me)"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        for ship_number, ship_image in enumerate(self.ship_images):
            x_position = 20 + ship_number * (ship_image.get_width() + 10)
            y_position = self.screen_rect.bottom - ship_image.get_height() - 20
            self.screen.blit(ship_image, (x_position, y_position))