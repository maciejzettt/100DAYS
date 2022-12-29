from turtlefunctions import *


pen = t.Turtle()
canvas = t.Screen()
canvas.colormode(255)
pen.speed("fastest")
pen.width(2)

CIRCLE_RADIUS = 100
NUMBER_OF_CIRCLES = 60

draw_spirograph(pen, CIRCLE_RADIUS, NUMBER_OF_CIRCLES)

canvas.exitonclick()
