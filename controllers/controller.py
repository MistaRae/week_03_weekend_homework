from flask import Flask, render_template
from app import app
from modules.game import Game, play
from modules import games
from modules import player
from modules.players import all_players

@app.route ("/")
def home():
    return "Welcome to Rock, Paper Scissors!"

@app.route("/<player_1>/<player_2>")
def play_game(player_1, player_2):
    challenger_1 = [player for player in all_players if player.name == player_1][0]
    challenger_2 = [player for player in all_players if player.name == player_2][0]
    return render_template("index.html", winner=play(challenger_1, challenger_2), title="winner")

    # return render_template("index.html", title="title", all_players="all_players")