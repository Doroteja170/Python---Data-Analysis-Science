import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
carmanager=CarManager()
scoreboard=Scoreboard
screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
counter=0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move_car()

    for car in carmanager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    if player.finish_line():
        player.starting_pos()
        carmanager.level_up()

screen.exitonclick()