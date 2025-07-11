from turtle import Turtle,Screen
import random
import colorgram

colors=colorgram.extract('picture.jpg',6)


t=Turtle()
t.shape("turtle")
screen=Screen()

screen.colormode(255)
def random_color():
    # r = random.randint(0,255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)
    
    color = random.choice(colors)
    r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
    return (r, g, b)


t.shapesize(stretch_wid=0.5, stretch_len=0.5)

t.hideturtle()

start_x = -270
start_y = -260

for row in range(10):
    y = start_y + row * 50
    t.penup()
    t.goto(start_x, y)
    t.pendown()
    for col in range(14):
        t.dot(30, random_color())
        t.penup()
        t.forward(40)


screen.exitonclick()