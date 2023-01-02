from turtle import Turtle

FONT_GAMEOVER = ("Courier", 20, "bold")
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self, y_position: int):
        super().__init__()
        self._y_position = y_position
        self._score = 0
        self.penup()
        self.speed(0)
        self.pencolor('white')
        self.hideturtle()
        self.goto(0, y_position)
        self.update_message()

    def increase_score(self, amount: int):
        self._score += amount
        self.update_message()

    def update_message(self):
        self.clear()
        self.write(arg=f"Score: {self._score}", align="center", font=FONT)

    def game_over_message(self):
        self.update_message()
        self.goto(0, 0)
        self.pencolor("yellow")
        self.write(arg="Game Over", align="center", font=FONT_GAMEOVER)
