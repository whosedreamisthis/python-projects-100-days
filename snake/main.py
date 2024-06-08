from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.title('snake game')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')




game_is_on = True

while game_is_on:

    time.sleep(0.1)
    snake.move()

    if snake.is_at_edge():
        game_is_on = False
        scoreboard.game_over()

    if snake.head.distance(food) < 15:
        scoreboard.increment_score()
        print('num none num')
        food.move()
        snake.extend()

    for segment in snake.turtles:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





    screen.update()

screen.exitonclick()