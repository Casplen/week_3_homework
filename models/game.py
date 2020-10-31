from app.models.player import Player

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        if self.player1.choice == self.player2.choice:
            return None
        if self.player1.choice == "scissors":
            if self.player2.choice == "paper":
                return self.player1
            if self.player2.choice == "rock":
                return self.player2
        if self.player1.choice == "paper":
            if self.player2.choice == "scissors":
                return self.player2
            if self.player2.choice == "rock":
                return self.player1
        if self.player1.choice == "rock":
            if self.player2.choice == "paper":
                return self.player2
            if self.player2.choice == "scissors":
                return self.player1

    def get_winner(self):
        if self.play() == None:
            return "Tie!"
        if self.play() == self.player1:
            return f'{self.player1.name} wins by playing {self.player1.choice}.'
        if self.play() == self.player2:
            return f'{self.player2.name} wins by playing {self.player2.choice}.'