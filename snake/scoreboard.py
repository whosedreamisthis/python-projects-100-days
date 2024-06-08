from turtle import Turtle

FONT = ('Courier', 15, 'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)
        self.display()

    def display(self):
        self.clear()

        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)


    def increment_score(self):
        self.score += 1
        print(f"new score is {self.score}")
        self.display()


