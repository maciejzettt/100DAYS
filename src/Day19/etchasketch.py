from turtle import Turtle, Screen

turtle = Turtle()
canvas = Screen()
turtle.width(2)


def move_forwards():
    turtle.forward(5)


def move_backwards():
    turtle.back(5)


def turn_ccw():
    turtle.left(6)


def turn_cw():
    turtle.right(6)


def clear_drawing():
    turtle.clear()
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()


canvas.listen()
canvas.onkey(key='w', fun=move_forwards)
canvas.onkey(key='s', fun=move_backwards)
canvas.onkey(key='a', fun=turn_ccw)
canvas.onkey(key='d', fun=turn_cw)
canvas.onkey(key='c', fun=clear_drawing)
canvas.exitonclick()
