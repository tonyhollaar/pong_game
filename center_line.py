# center_line.py
from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, -300)
        self.setheading(90)
        self.pensize(5)
        self.draw_line()

    def draw_line(self):
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)