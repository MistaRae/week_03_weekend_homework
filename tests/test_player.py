import unittest
from modules.player import Player 

class TestPlayer(unittest.TestCase):

    def test_instance_variables(self):
        self.player = Player("Mark", "Rock")
        self.assertEqual("Mark", self.player.name)