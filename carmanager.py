import random
from turtle import Turtle

colors = ["red", "green", "yellow", "blue", "black"]
traffic = []


class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.penup()
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(stretch_len=2)
        self.goto(400, random.randrange(-220, 250, 30))
        traffic.append(self)

    def traffic_movement(self):
        for vehicle in traffic:
            vehicle.backward(self.speed)

