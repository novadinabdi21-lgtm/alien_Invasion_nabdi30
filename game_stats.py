"""
Purpose: Contains the GameStats class used to track game statistics
such as remaining ships and game progress.

Starter Code: Python Crash Course by Eric Matthes

Author: Novadin Abdi
"""

class GameStats:
    """Track statistics for Alien Invasion.(me)"""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.score = 0
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game.(me)"""
        self.ships_left = self.settings.ship_limit
        self.score = 0