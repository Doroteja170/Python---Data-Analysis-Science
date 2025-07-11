from turtle import Screen
from PongGame.ball import Ball
from PongGame.paddle import Paddle
import time

from PongGame.scoreboard import Scoreboard

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball=Ball()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset()
        score.l_point()
        if score.l_score==3:
            game_on=False
            print("Left Player Won")

    if ball.xcor()<-380:
        ball.reset()
        score.r_point()
        if score.r_score==3:
            game_on=False
            print("Right Player Won")





screen.exitonclick()

