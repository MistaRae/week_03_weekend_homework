from flask import Flask, render_template, request
from app import app
from modules.game import Game, play, Computer
from modules import games
from modules import player
from modules.player import Player
from modules.players import all_players
import random

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/welcome-page")
def welcome_page():
    return render_template("welcome-page.html", title="Rules")

@app.route("/<player_1>/<player_2>")
def play_game(player_1, player_2):
    challenger_1 = [player for player in all_players if player.name == player_1][0]
    challenger_2 = [player for player in all_players if player.name == player_2][0]
    return render_template("index.html", winner=play(challenger_1, challenger_2), title="winner")

@app.route("/PvP")
def get_user_input():
    return render_template("input.html", title="input")

@app.route("/PvP", methods=["POST"])
def play_against_player():
    challenger_1_name = request.form["player_1"]
    challenger_1_gesture = request.form["P1-gesture"]
    challenger_2_name = request.form["player_2"]
    challenger_2_gesture = request.form["P2-gesture"]
    challenger_1 = Player(challenger_1_name,challenger_1_gesture)
    challenger_2 = Player(challenger_2_name,challenger_2_gesture)
    return render_template("index.html", winner=play(challenger_1, challenger_2), title="Winner")

@app.route("/PvC")
def get_user_input_vs_computer():
    return render_template("vsComp.html", title="vsComp")

@app.route("/PvC",methods=["POST"])
def play_against_computer():
    # user input
    challenger_1_name = request.form["player_1"]
    challenger_1_gesture = request.form["P1-gesture"]
    challenger_1 = Player(challenger_1_name,challenger_1_gesture)
    # random computer selection
    gestures = ["Rock", "Paper", "Scissors"]
    computer_roll = random.choice(gestures)

    # computer_roll = random.randint(0,2) 
    # if computer_roll == 0:
    #     computer_roll = "Rock"
    # elif computer_roll == 1:
    #     computer_roll = "Paper"
    # computer_roll = "scissors"

    computer = Computer("Computer", computer_roll)

    return render_template("PvC.html", winner=play(challenger_1, computer), title="Winner")
