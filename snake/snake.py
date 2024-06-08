from turtle import Turtle

TURTLE_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment(-i * TURTLE_SIZE, 0)

    def add_segment(self, x, y):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()

        turtle.goto(x, y)
        self.turtles.append(turtle)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            if i > 0:
                new_x = self.turtles[i - 1].xcor()
                new_y = self.turtles[i - 1].ycor()
                self.turtles[i].goto(new_x, new_y)

        self.head.forward(20)

    def extend(self):
        position = self.turtles[-1].position()
        self.add_segment(position[0], position[1])

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

    def is_at_edge(self):
        for turtle in self.turtles:
            pos = turtle.position()
            if pos[0] > 280 or \
                    pos[0] < -280 or \
                    pos[1] > 300 or \
                    pos[1] < -300:
                return True
        return False
