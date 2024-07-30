# rock_paper_scissors.py
#rock paper scissors game is created by using python and for that we have to import some libraries.
#it is created by using gui interface.

import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QMessageBox

class RockPaperScissors(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Rock-Paper-Scissors")
        self.setGeometry(300, 300, 300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Choose Rock, Paper, or Scissors:")
        self.layout.addWidget(self.label)

        self.choiceField = QLineEdit()
        self.layout.addWidget(self.choiceField)

        self.playButton = QPushButton("Play")
        self.playButton.clicked.connect(self.playGame)
        self.layout.addWidget(self.playButton)

        self.resultLabel = QLabel("")
        self.layout.addWidget(self.resultLabel)

        self.scoreLabel = QLabel("Score: User 0, Computer 0")
        self.layout.addWidget(self.scoreLabel)

        self.userScore = 0
        self.computerScore = 0

    def playGame(self):
        userChoice = self.choiceField.text().lower()
        if userChoice not in ["rock", "paper", "scissors"]:
            QMessageBox.critical(self, "Error", "Invalid choice. Please enter Rock, Paper, or Scissors.")
            return

        computerChoice = random.choice(["rock", "paper", "scissors"])

        if userChoice == computerChoice:
            result = "It's a tie!"
        elif (userChoice == "rock" and computerChoice == "scissors") or \
             (userChoice == "scissors" and computerChoice == "paper") or \
             (userChoice == "paper" and computerChoice == "rock"):
            result = "You win!"
            self.userScore += 1
        else:
            result = "You lose!"
            self.computerScore += 1

        self.resultLabel.setText(f"You chose: {userChoice}\nComputer chose: {computerChoice}\n{result}")
        self.scoreLabel.setText(f"Score: User {self.userScore}, Computer {self.computerScore}")

        self.choiceField.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = RockPaperScissors()
    game.show()
    sys.exit(app.exec_())