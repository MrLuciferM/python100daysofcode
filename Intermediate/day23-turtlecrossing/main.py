import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect hit and run
    if car_manager.detect_collision(player):
        game_is_on = False
        scoreboard.game_over()

    # level up
    if player.crossed_road():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()