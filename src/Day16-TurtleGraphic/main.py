import turtle as t

turtle = t.Turtle()
arrow = t.Turtle()
turtle.shape('turtle')
turtle.color('RoyalBlue3')
canvas = t.Screen()
canvas.canvwidth = 600
canvas.canvheight = 600
arrow.right(90)
arrow.fd(50)
turtle.forward(100)
turtle.right(90)
turtle.fd(100)
canvas.exitonclick()
