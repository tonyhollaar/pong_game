
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # setup object , without pen drawing from middle and no cursor
        self.color("white")  # with white color
        self.penup()
        self.hideturtle()

        # set score to 0 for each player
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        # erase what used to be there e.g. previous score before writing new score
        self.clear()

        # define coordinates for left-sided score
        self.goto(-100, 200)
        # write the score on the screen for left-sided player
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

        # define coordinates for right-sided score
        self.goto(100, 200)
        # write the score on the screen for right-sided player
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()