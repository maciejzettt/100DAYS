import turtle


main_turtle = turtle.Turtle()

for _ in range(4):
    main_turtle.forward(100)
    main_turtle.right(90)


canvas = turtle.Screen()
canvas.exitonclick()


