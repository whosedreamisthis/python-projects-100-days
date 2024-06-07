from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.tracer(0)
turtles=[]
TURTLE_SIZE = 20
for i in range(3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(-i * TURTLE_SIZE,0)
    turtles.append(turtle)

screen.title('snake game')
screen.update()
game_is_on = True

def is_turtle_at_edge():
    pos = turtle.position()
    if pos[0] > 260 or \
            pos[0] < -260 or \
            pos[1] > 260 or \
            pos[1] < -260:
        return True
    return False
while game_is_on:
    for turtle in turtles:
        turtle.forward(20)
        screen.update()
        time.sleep(0.005)
        if is_turtle_at_edge():
            game_is_on = False
screen.exitonclick()