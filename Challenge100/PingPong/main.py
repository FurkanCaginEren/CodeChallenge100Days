from turtle import Screen
from sticks import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
### Screen Setup ###

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("PingPong")
screen.tracer(0)

### Screen Setup ###

player1 = Paddle((-550, 0))
player2 = Paddle((550, 0))
ball = Ball()
sboard = Scoreboard()
screen.update()


screen.listen()

screen.onkeypress(player2.up, "Up")
screen.onkey(player2.down, "Down")
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)

    ball.move()

    screen.update()
    # Detect Collision up wall

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Detect Collison  paddle
    if (ball.distance(player2) < 50 and ball.xcor() > 530) or (ball.distance(player1) < 50 and ball.xcor() < -530):
        ball.bounce_x()
    # Detect Pass R Player
    if ball.xcor() > 580:
        ball.reset()
        sboard.l_point()
    # Detect Pass L Player

    if ball.xcor() < -580:
        ball.reset()
        sboard.r_point()

screen.exitonclick()
