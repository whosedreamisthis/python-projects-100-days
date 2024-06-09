from turtle import Turtle


class Car(Turtle):

    def __init__(self,color, y):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        # self.setheading(0)
        self.penup()

        self.goto(300, y)

    def move(self, move_amount):
        self.backward(move_amount)

    def atEdge(self):
        return self.xcor() < -300
