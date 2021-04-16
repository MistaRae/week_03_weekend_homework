import unittest
from modules.game import Game


class TestGame(unittest.TestCase):
    
    def test_game_instance_variables(self):
        self.game = Game("Rock, Paper, Scissors")
        self.assertEqual("Rock, Paper, Scissors", self.game.name)