import turtle as t
import random as rnd
from turtlefunctions import *


canvas = t.Screen()
pen = t.Turtle()
canvas.colormode(255)
pen.width(2)

STARTING_POLYGON_SIDES = 3
FINAL_POLYGON_SIDES = 30
SIDE_LENGTH = 30

assert STARTING_POLYGON_SIDES < FINAL_POLYGON_SIDES

for num_sides in range(STARTING_POLYGON_SIDES, FINAL_POLYGON_SIDES + 1):
    pen.pencolor(rnd.randint(1, 255), rnd.randint(1, 255), rnd.randint(1, 255))
    draw_polygon(pen, num_sides, SIDE_LENGTH)

canvas.exitonclick()

