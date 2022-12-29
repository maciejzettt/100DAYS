from turtle import Turtle, Screen
from random import randint

is_race_on = False
winner = ''
screen = Screen()
screen.setup(width=800, height=400)

turtles_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
turtles_starting_y_pos = [-160, -100, -40, 20, 80, 140]
racing_turtles = list[Turtle]()

for turtle_index in range(6):
    turtle_temp = Turtle(shape='turtle')
    turtle_temp.color(turtles_colors[turtle_index])
    turtle_temp.penup()
    turtle_temp.goto(-350, turtles_starting_y_pos[turtle_index])
    racing_turtles.append(turtle_temp)

user_bet = screen.textinput(title='Who will win?', prompt='Enter your bet as a colour:')
while user_bet not in turtles_colors:
    user_bet = screen.textinput(title='Input Error: wrong color.', prompt='Enter your bet as a valid color:')
if user_bet in turtles_colors:
    is_race_on = True

while is_race_on:
    for turtle in racing_turtles:
        random_distance = randint(1, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 380:
            is_race_on = False
            winner = turtle.pencolor()
            break

print(f"The {winner} turtle has won!")
print(f"Your bet was {user_bet}, so you {'also win!' if user_bet == winner else 'lose.'}")

screen.exitonclick()
