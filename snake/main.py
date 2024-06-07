from turtle import Screen, Turtle
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.tracer(0)
snake = Snake()

screen.title('snake game')
screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.25)
    snake.move()

    if snake.is_at_edge():
        game_is_on = False
screen.exitonclick()