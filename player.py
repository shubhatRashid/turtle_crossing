
from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.left(90)
        self.starting_position()

    def move(self):
        self.forward(20)

    def starting_position(self):
        self.goto(0, -250)


