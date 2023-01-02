from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.fillcolor('blue')
        self.pencolor('lightgrey')
        self.speed(0)
        self._move_to_random_place()

    def _move_to_random_place(self):
        pos_x = randint(-13, 13) * 20
        pos_y = randint(-13, 13) * 20
        self.goto(pos_x, pos_y)

    def refresh(self):
        self._move_to_random_place()
