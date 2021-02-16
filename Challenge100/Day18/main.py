from turtle import Turtle
from turtle import Screen
import random
import colorgram


def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dash_lines(turtle):
    x = 0
    while x < 10:
        turtle.forward(5)
        turtle.pu()
        turtle.forward(5)
        turtle.pd()
        x += 1


def draw_multi_shape(turtle):
    n = 3
    while n < 11:
        for _ in range(n):
            turtle.forward(100)
            turtle.right(360/n)
        n += 1
        r = round(random.randrange(0, 255))
        g = round(random.randrange(0, 255))
        b = round(random.randrange(0, 255))
        turtle.pencolor(r, g, b)


def random_color():
    r = round(random.randrange(0, 255))
    g = round(random.randrange(0, 255))
    b = round(random.randrange(0, 255))
    color = (r, g, b)
    return color


def random_walk(turtle):
    direction_angle = [0, 90, 180, 270, ]
    x = 0
    timmy.pensize(10)
    while x < 1000:
        turtle.speed("fastest")
        choice_angle = random.choice(direction_angle)
        turtle.setheading(choice_angle)
        turtle.forward(10)
        turtle.color(random_color())
        x += 1


def draw_spirograph(size_of_gap, turtle):
    turtle.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


round(1.4756, 2)
screen = Screen()
timmy = Turtle()
timmy.color("red")

screen.colormode(255)


# draw_square(timmy)
# draw_dash_lines(timmy)
# draw_multi_shape(timmy)
# random_walk(timmy)
draw_spirograph(5, timmy)

screen.exitonclick()
