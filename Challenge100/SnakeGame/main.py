from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# def move_east(snake):
#     snake.setheading(0)


# def move_nort(snake):
#     snake.setheading(90)


# def move_west(snake):
#     snake.setheading(180)


# def move_south(snake):
#     snake.setheading(270)


##############  SCREEN  #################
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

##############  SCREEN  #################


snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision with food

    if snake.head.distance(food) < 15:
        score.point()
        snake.extend()
        food.refresh()
# Detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()


# Detect collison with Tail
    for i in snake.snake_list[1:]:

        if snake.head.distance(i) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
