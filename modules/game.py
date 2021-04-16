from modules.player import Player

class Game:

    def __init__(self, name):
        self.name = name


def play(player_1, player_2):
        match_drawn = None
        if player_1.gesture == player_2.gesture:
            return f"the winning player is: {match_drawn}"
        if player_1.gesture == "Rock" and player_2.gesture == "Scissors":
            return f"{player_1.name} wins by playing {player_1.gesture}!"
        if player_1.gesture == "Scissors" and player_2.gesture == "Rock":
            return f"{player_2.name} wins by playing {player_2.gesture}!"

        if player_1.gesture == "Paper" and player_2.gesture == "Rock":
            return f"{player_1.name} wins by playing {player_1.gesture}!"
        if player_1.gesture == "Rock" and player_2.gesture == "Paper":
            return f"{player_2.name} wins by playing {player_2.gesture}!"

        if player_1.gesture == "Scissors" and player_2.gesture == "Paper":
            return f"{player_1.name} wins by playing {player_1.gesture}!"
        if player_1.gesture == "Paper" and player_2.gesture == "Scissors":
            return f"{player_2.name} wins by playing {player_2.gesture}!"
        