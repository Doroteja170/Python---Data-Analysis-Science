COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            car=Turtle("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            y_new = random.randint(-250, 250)
            car.goto(300, y_new)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT



