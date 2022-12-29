import random
import colorgram.colorgram
import turtle as t

DOT_RADIUS = 30
DOT_SPACING = 60
NUM_ROWS = 10
NUM_COLUMNS = 10
NUM_COLOURS = 20
SAMPLE_FILE = 'hirst.jpg'

print(f"Sampling colours from {SAMPLE_FILE}...")
colours = [colour.rgb for colour in colorgram.extract(SAMPLE_FILE, NUM_COLOURS) if colour.hsl.l < 247]
print("Sampling complete.")

pen = t.Turtle()
canvas = t.Screen()
canvas.colormode(255)
pen.penup()
pen.speed(0)


def move_to_start():
    pen.back(DOT_SPACING * NUM_COLUMNS / 2)
    pen.right(90)
    pen.forward(DOT_SPACING * NUM_ROWS / 2)
    pen.left(90)


def move_row_up():
    pen.left(90)
    pen.forward(DOT_SPACING)
    pen.left(90)
    pen.forward(DOT_SPACING * NUM_COLUMNS)
    pen.right(180)


def draw_row(columns: int):
    for _ in range(columns):
        pen.dot(DOT_RADIUS, random.choice(colours))
        pen.forward(DOT_SPACING)


pen.hideturtle()
move_to_start()

for _ in range(NUM_ROWS):
    draw_row(NUM_COLUMNS)
    move_row_up()

canvas.exitonclick()
