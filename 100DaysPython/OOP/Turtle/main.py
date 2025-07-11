from turtle import Turtle,Screen
import random

t=Turtle()
t.shape("arrow")
screen=Screen()
# for i in range(4):
#     t.right(90)
#     t.forward(100)
#
# for _ in range(10):
#     t.pendown()
#     t.forward(5)
#     t.penup()
#     t.forward(5)



# def draw_shape(num):
#     angel = 360 / num
#     for i in range(num):
#         t.forward(100)
#         t.right(angel)
#
# for size in range(3,11):
#     t.color(random.choice(color))
#     draw_shape(size)

screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

# directions = [0,90,180,270]
t.speed(10)
# t.pensize(8)
#
# for i in range(200):
#     t.color(random_color())
#     t.forward(30)
#     t.setheading(random.choice(directions))

# for _ in range(100):
#     t.color(random_color())
#     t.circle(80)
#     t.left(10)
