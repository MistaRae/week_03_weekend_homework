import unittest
from modules.game import Game
from modules.player import Player


class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game("Rock, Paper, Scissors")
        self.mark = Player("Mark", "Rock")
        self.jill = Player("Jill", "Paper")
        self.chris = Player("Chris", "Scissors")

    def test_game_instance_variables(self):
      
        self.assertEqual("Rock, Paper, Scissors", self.game.name)

    def test_game_recognises_draw(self):
        self.assertEqual("the winning player is: None", self.game.play(self.mark,self.mark))
        