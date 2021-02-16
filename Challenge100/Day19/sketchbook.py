from turtle import Turtle, Screen

eylul = Turtle()

screen = Screen()


def move_forwards():
    eylul.forward(10)


def move_backwards():
    eylul.backward(10)


def turn_right():
    eylul.right(10)


def turn_left():
    eylul.left(10)


def screen_clear():
    eylul.clear()
    eylul.penup()
    eylul.home()
    eylul.pendown


screen.listen()  # Starts event

screen.onkey(key="w", fun=move_forwards)  # Higher order funciton

screen.onkey(key="s", fun=move_backwards)

screen.onkey(key="a", fun=turn_left)

screen.onkey(key="d", fun=turn_right)

screen.onkey(key="c", fun=screen_clear)

screen.exitonclick()
