from app.models.game import Game
from app.models.player import Player 

player1 = Player("Player 1", None)
player2 = Player("Player 2", None)

rock_paper_scissors = Game(player1, player2)