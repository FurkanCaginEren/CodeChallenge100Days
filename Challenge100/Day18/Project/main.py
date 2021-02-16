###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

# import colorgram
# import os

# here = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(here, 'image.jpg')

# rgb_colors = []
# colors = colorgram.extract(filename, 30)

# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
from turtle import Turtle
from turtle import Screen
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86),
              (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# left bottom -450 -350 top -450 350
# right bottom 450 -350 top 450 350


turtle = Turtle()
screen = Screen()
turtle.penup()
screen.colormode(255)
turtle.speed("fastest")

x = -450
y = -350

for _ in range(15):
    turtle.setpos(x, y)
    turtle.dot(40, random.choice(color_list))

    for _ in range(18):

        turtle.forward(50)
        turtle.dot(40, random.choice(color_list))
    y += 50

screen.exitonclick()
