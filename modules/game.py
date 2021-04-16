class Game:

    def __init__(self, name):
        self.name = name


    def play(self, player_1, player_2):
        match_drawn = None
        if player_1.gesture == player_2.gesture:
            return f"the winning player is: {match_drawn}"
        if player_1.gesture == "Rock" and player_2.gesture == "scissors":
            return f"{player_1.name} wins by playing {player_1.gesture}!"