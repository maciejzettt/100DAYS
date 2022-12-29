from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(30)


screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()
