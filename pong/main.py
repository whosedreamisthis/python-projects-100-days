from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(r_paddle.go_up, 'Up')

screen.onkeypress(l_paddle.go_down, 's')
screen.onkeypress(l_paddle.go_up, 'w')

game_is_on = True
# scoreboard.display()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 50 and \
            ball.xcor() < -320:
        ball.bounce_x()
        print("made contact")

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.increment_left_score()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.increment_right_score()


screen.exitonclick()
