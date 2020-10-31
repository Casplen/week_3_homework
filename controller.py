from app import app
from app.models.game import Game 
from app.models.player import Player
from app.models.rockpaperscissors import *

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<choice1>/<choice2>')
def game(choice1, choice2):
    player1.choice = choice1
    player2.choice = choice2
    rock_paper_scissors.play()
    return rock_paper_scissors.get_winner()



