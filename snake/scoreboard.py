from turtle import Turtle
import turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        turtle.penup()
    def display(self):
        turtle.clear()
        style = ('Courier', 15, 'normal')
        turtle.color('white')
        turtle.goto(0, -280)
        turtle.write(f"Score: {self.score}", False, align="center",font=style)
        turtle.hideturtle()


    def increment_score(self):
        self.score += 1
        print(f"new score is {self.score}")


