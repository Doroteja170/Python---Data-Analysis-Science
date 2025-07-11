from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(500,400)

user_bet=screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")

turtles=[]
colors=["red","orange","blue","green","yellow"]
y_position=[-100,-50,0,50,100]
for index in range(0,5):
    t=Turtle(shape="turtle")
    t.color(colors[index])
    t.penup()
    t.goto(-230,y_position[index])
    turtles.append(t)

is_race_on=False
if user_bet:
    is_race_on=True

# turtle is 40w40h so end is going to be 250-(40/2)=230
while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning=turtle.pencolor()
            if winning==user_bet:
                print(f"You've won! The {winning} turtle is the winner!")
            else:
                print(f"You've lost! The {winning} turtle is the winner!")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()