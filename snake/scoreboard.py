from turtle import Turtle
import os
FONT = ('Courier', 15, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        if not os.path.exists("high_score.txt"):
            open("high_score.txt", 'w').close()

        with open("high_score.txt", "r+") as file:
            hs = file.read()
            if hs == "":
                self.high_score = 0
            else:
                hs_arr = hs.split(":")
                self.high_score = int(hs_arr[1])

        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)
        self.display()

    def display(self):
        self.clear()

        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./high_score.txt", "w") as file:
                file.write(f"high score: {self.high_score}")

        self.score = 0
        self.display()

    def increment_score(self):
        self.score += 1

        print(f"new score is {self.score}")
        self.display()
