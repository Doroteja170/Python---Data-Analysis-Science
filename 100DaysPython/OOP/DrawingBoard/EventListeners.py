from turtle import Turtle,Screen

t=Turtle()
t.color("green")
screen=Screen()

def move_forwards():
    t.forward(10)
def move_back():
    t.backward(10)
def counter_clockwise():
    t.left(10)
def clockwise():
    t.right(10)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()