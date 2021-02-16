from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    """Cordinates"""

    def __init__(self, Cordinates):
        super().__init__()

        self.goto(Cordinates)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.setheading(UP)
        self.penup()

    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
