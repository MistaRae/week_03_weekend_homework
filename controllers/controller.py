from flask import Flask, render_template
from app import app
from modules.game import Game, play
from modules import games
from modules import player

@app.route ("/")
def home():
    return "Welcome to Rock, Paper Scissors!"

@app.route("/<player_1>/<player_2>")
def game(player_1, player_2):
    return game.play(player_1, player_2)