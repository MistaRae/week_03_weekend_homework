from modules.player import Player
from modules import players

class Game:

    def __init__(self, name):
        self.name = name


def play(player_1, player_2):    
        winner = None
     
        if player_1.gesture == "Rock" and player_2.gesture == "Scissors":
            winner = player_1
        if player_1.gesture == "Scissors" and player_2.gesture == "Rock":
            winner = player_2

        if player_1.gesture == "Paper" and player_2.gesture == "Rock":
            winner = player_1
        if player_1.gesture == "Rock" and player_2.gesture == "Paper":
            winner = player_2

        if player_1.gesture == "Scissors" and player_2.gesture == "Paper":
            winner = player_1
        if player_1.gesture == "Paper" and player_2.gesture == "Scissors":
            winner = player_2

        return winner

class Computer:
    def __init__(self, name, gesture):
        self.name = name
        self.gesture = gesture

    # if not winner:
    #     return "None"
    # return f"{winner.name} has won by playing {winner.gesture}"

# def play(player_1, player_2):    
#     match_drawn = None
#     if player_1.gesture == player_2.gesture:
#         return f"the winning player is: {match_drawn}"

#     if player_1.gesture == "Rock" and player_2.gesture == "Scissors":
#         return f"{player_1.name} wins by playing {player_1.gesture}!"
#     if player_1.gesture == "Scissors" and player_2.gesture == "Rock":
#         return f"{player_2.name} wins by playing {player_2.gesture}!"

#     if player_1.gesture == "Paper" and player_2.gesture == "Rock":
#         return f"{player_1.name} wins by playing {player_1.gesture}!"
#     if player_1.gesture == "Rock" and player_2.gesture == "Paper":
#         return f"{player_2.name} wins by playing {player_2.gesture}!"

#     if player_1.gesture == "Scissors" and player_2.gesture == "Paper":
#         return f"{player_1.name} wins by playing {player_1.gesture}!"
#     if player_1.gesture == "Paper" and player_2.gesture == "Scissors":
#         return f"{player_2.name} wins by playing {player_2.gesture}!"

# def play_2(gesture_1, Gesture_2):
#     if gesture1 == gesture_2:
#         return "draw"
#     if gesture_1