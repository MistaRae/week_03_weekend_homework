import unittest
from modules.game import Game
from modules import game
from modules.player import Player


class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game("Rock, Paper, Scissors")
        self.mark = Player("Mark", "Rock")
        self.jill = Player("Jill", "Paper")
        self.chris = Player("Chris", "Scissors")

    def test_game_instance_variables(self):
      
        self.assertEqual("Rock, Paper, Scissors", self.game.name)

    def test_game_recognizes_draw(self):
        self.assertEqual(None, game.play(self.mark,self.mark))

    def test_game_rock_beats_scissors(self):
        self.assertEqual(self.mark, game.play(self.chris,self.mark))

    def test_game_rock_beats_scissors_reversed(self):
        self.assertEqual(self.mark, game.play(self.mark,self.chris))
        
    def test_game_paper_beats_rock(self):
        self.assertEqual(self.jill, game.play(self.jill,self.mark))
    
    def test_game_paper_beats_rock_reversed(self):
        self.assertEqual(self.jill, game.play(self.mark,self.jill))

    def test_game_scissors_beats_paper(self):
        self.assertEqual(self.chris, game.play(self.chris,self.jill))
    
    def test_game_scissors_beats_paper_reversed(self):
        self.assertEqual(self.chris, game.play(self.jill,self.chris))