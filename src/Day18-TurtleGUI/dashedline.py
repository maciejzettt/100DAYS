import turtle as t


canvas = t.Screen()
canvas.screensize(600, 100, "white")
drawing_turtle = t.Turtle()
screen_width = canvas.canvwidth
turtle_position_x = 0
print(screen_width)

while turtle_position_x < screen_width:
    drawing_turtle.forward(10)
    drawing_turtle.penup()
    drawing_turtle.forward(10)
    drawing_turtle.pendown()

canvas.exitonclick()
