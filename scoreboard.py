
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.hideturtle()
        self.penup ()
        self.level_of_game = 0

    def game_over(self):
        self.write(arg="GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level_of_game += 1
        self.goto(-290, 270)
        self.write(arg=f"level : {self.level_of_game}", align="left", font=("Courier", 12, "normal") )