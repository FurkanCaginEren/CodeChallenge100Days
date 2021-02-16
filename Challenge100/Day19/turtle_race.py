from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
x = -230
y = -125
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False


def setup_race(x, y):
    for i in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.setpos(x, y)
        y += 50
        turtle_list.append(new_turtle)


setup_race(x, y)

user_bet = screen.textinput(title="Make your bets Game Ready",
                            prompt="Enter Winner Color")


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winnner_color = turtle.pencolor()
            is_race_on = False
            if user_bet == winnner_color:
                print(f"Winner was {winnner_color} color you win!")
            else:
                print(f"Winner was {winnner_color} color you lost!")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
