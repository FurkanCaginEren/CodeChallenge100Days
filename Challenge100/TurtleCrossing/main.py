import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
##SCREEN##
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
##SCREEN##

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()

screen.onkeypress(player.move, "w")

game_is_on = True
loop = 0

while game_is_on:
    loop += 1
    time.sleep(0.1)
    screen.update()

    # Create car and move car
    car_manager.create_car()
    car_manager.move_cars()

    # Detection player with Wall

    if player.ycor() > 280:
        car_manager.speed_up()
        scoreboard.point()
        player.reset()

    # Detection player with Car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
