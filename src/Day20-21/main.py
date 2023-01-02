import time
from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
snake = Snake(3, screen)
snake.head_segment_highlight()
food = Food()
scoreboard = Scoreboard(280)
scoreboard.increase_score(0)

game_is_on = True
while game_is_on:
    snake.loop_step()
    if snake.check_food_collision(food):
        snake.add_new_segment()
        scoreboard.increase_score(1)
        food.refresh()
    game_is_on = snake.not_colliding()
    time.sleep(0.1)
scoreboard.game_over_message()

screen.exitonclick()
