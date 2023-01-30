import time
from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard

# SETTING UP THE SCREEN

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

# CREATING THE PLAYER OBJECT SCOREBOARD

scoreboard = Scoreboard()
scoreboard.level_up()
player = Player ()
screen.onkeypress (player.move, "Up")

traffic = []
speed = 10
i = 4
game_is_on = True
while game_is_on:

    # CREATING THE TRAFFIC ON ROAD
    i += 1
    if i % 5 == 0:
        carManager = CarManager (speed)
        carManager.traffic_movement ()
        traffic.append (carManager)

    # CHECKING IF TURTLE HAS PASSED A LEVEL

    if player.ycor () > 250:
        speed += 5
        player.starting_position ()
        scoreboard.level_up()

    # DETECTING THE PLAYERS COLLUSION WITH CARS
    for cars in traffic:
        if player.distance (cars) < 15:
            game_is_on = False
            gameshow = Scoreboard()
            gameshow.game_over()


    carManager.traffic_movement ()
    time.sleep (0.1)
    screen.update ()

screen.exitonclick()
