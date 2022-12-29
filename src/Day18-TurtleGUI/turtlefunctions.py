import random as rnd
import turtle as t


def random_rgb_colour(component_colour_margin=0) -> tuple:
    r = rnd.randint(0 + component_colour_margin, 255 - component_colour_margin)
    g = rnd.randint(0 + component_colour_margin, 255 - component_colour_margin)
    b = rnd.randint(0 + component_colour_margin, 255 - component_colour_margin)
    return r, g, b


def random_right_angle_direction() -> int:
    direction_angle = 90 * rnd.randint(0, 3)
    return direction_angle


def random_free_direction() -> int:
    direction_angle = rnd.randint(0, 360)
    return direction_angle


def random_walk(turtle_object: t.Turtle, step_length: int) -> None:
    turtle_object.pencolor(random_rgb_colour(10))
    direction_angle = random_right_angle_direction()
    turtle_object.setheading(direction_angle)
    turtle_object.forward(step_length)
    print(f"Step: {direction_angle}")


def draw_polygon(turtle: t.Turtle, number_of_sides: int, side_len: int):
    for _ in range(number_of_sides):
        angle = 360 / number_of_sides
        turtle.forward(side_len)
        turtle.right(angle)


def draw_spirograph(turtle: t.Turtle, radius: int, number_of_circles: int):
    heading = 0
    heading_increment = 360 / number_of_circles
    for _ in range(number_of_circles):
        heading += heading_increment
        turtle.setheading(heading)
        turtle.pencolor(random_rgb_colour())
        turtle.circle(radius)
