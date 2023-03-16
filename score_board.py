from turtle import Turtle
import os

HOME_DIRECTORY = os.path.expanduser('~')
GAME_DIRECTORY = os.path.join(HOME_DIRECTORY, 'Documents', 'data.txt')


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        try:
            with open(GAME_DIRECTORY, mode="r") as File:
                self.high_score = int(File.read())
        except:
            with open(GAME_DIRECTORY, mode="w") as File:
                File.write("0")
            with open(GAME_DIRECTORY, mode="r") as File:
                self.high_score = int(File.read())
        self.hideturtle()
        self.color("white")
        self.score_board_font = ("Typo Round", 15, 'bold')

    def increase_score(self):
        self.score += 1
        if self.score > int(self.high_score):
            with open(GAME_DIRECTORY, mode="w") as File:
                File.write(str(self.score))
        self.show_score_board()

    def show_score_board(self):
        with open(GAME_DIRECTORY, mode="r") as file:
            self.high_score = file.read()
        self.goto(0, 270)
        self.clear()
        self.write(f"Your Score: {self.score}. High Score: {self.high_score}",
                   align="center", font=self.score_board_font)

    def show_final_score(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=self.score_board_font)

    def reset(self):
        if self.score > int(self.high_score):
            with open(GAME_DIRECTORY, mode="w") as File:
                File.write(str(self.score))
        self.score = 0
        self.show_score_board()
