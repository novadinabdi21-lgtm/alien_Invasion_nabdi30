"""
Purpose: Contains the GameStats class used to track game statistics
such as remaining ships and game progress.

Starter Code: Python Crash Course by Eric Matthes

Author: Novadin Abdi
"""

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit