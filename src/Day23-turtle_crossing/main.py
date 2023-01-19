import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    chance = randint(0, 8)
    time.sleep(0.05)
    screen.update()
    car_manager.move_cars()
    if chance == 0:
        car_manager.create_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish():
        player.go_to_start()
        car_manager.increase_speed()
        score.increase_level()

screen.exitonclick()