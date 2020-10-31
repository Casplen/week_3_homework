from flask import render_template, request
from app import app
from app.models.game import Game 
from app.models.player import Player
from app.models.rockpaperscissors import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<choice1>/<choice2>')
def game(choice1, choice2):
    player1.choice = choice1
    player2.choice = choice2
    rock_paper_scissors.play()
    return render_template('game.html', game = rock_paper_scissors)

@app.route('/setnames', methods = ['POST'])
def setnames():
    player1.name = request.form['player_1_name']
    player2.name = request.form['player_2_name']
    return render_template('player1choice.html')

@app.route('/player1choice', methods = ['POST'])
def player1choice():
    player1.choice = request.form['player_1_choice']
    return render_template('player2choice.html')

@app.route('/player2choice', methods = ['POST'])
def player2choice():
    player2.choice = request.form['player_2_choice']
    rock_paper_scissors.play()
    return render_template('game.html', game = rock_paper_scissors)
    


