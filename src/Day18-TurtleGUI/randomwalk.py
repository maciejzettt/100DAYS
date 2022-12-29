from turtlefunctions import *


MAX_STEPS = 300

STEP_LENGTH = 20
pen = t.Turtle()
pen.speed(0)
pen.width(3)
canvas = t.Screen()
canvas.colormode(255)

for _ in range(MAX_STEPS):
    random_walk(pen, STEP_LENGTH)

canvas.exitonclick()
