from turtle import Turtle
class Snake:
    TURTLE_SIZE = 20
    def __init__(self):
        self.turtles = []

        for i in range(3):
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(-i * self.TURTLE_SIZE, 0)
            self.turtles.append(turtle)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            if i > 0:
                new_x = self.turtles[i - 1].xcor()
                new_y = self.turtles[i - 1].ycor()
                self.turtles[i].goto(new_x, new_y)

        self.turtles[0].forward(20)

    def is_at_edge(self):
        for turtle in self.turtles:
            pos = turtle.position()
            if pos[0] > 280 or \
                    pos[0] < -280 or \
                    pos[1] > 280 or \
                    pos[1] < -280:
                return True
        return False

