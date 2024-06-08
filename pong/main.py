from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(r_paddle.go_up, 'Up')

screen.onkeypress(l_paddle.go_down, 's')
screen.onkeypress(l_paddle.go_up, 'w')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
