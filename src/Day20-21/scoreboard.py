from turtle import Turtle

FONT_GAMEOVER = ("Courier", 20, "bold")
FONT = ("Courier", 15, "normal")
HS_FILE = 'data.txt'


class Scoreboard(Turtle):

    def __init__(self, y_position: int):
        super().__init__()
        try:
            with open(HS_FILE, mode='r') as file:
                self._high_score = int(file.read())
        except FileNotFoundError:
            self._high_score = 0
        self._y_position = y_position
        self._score = 0
        self.penup()
        self.speed(0)
        self.pencolor('white')
        self.hideturtle()
        self.goto(0, y_position)
        self.update_message()

    def reset(self):
        if self._score > self._high_score:
            self._high_score = self._score
        self._score = 0
        self.pencolor('white')
        self.goto(0, self._y_position)
        self.update_message()
        self.store_results()

    def increase_score(self, amount: int):
        self._score += amount
        self.update_message()

    def update_message(self):
        self.clear()
        self.write(arg=f"Score: {self._score}. High score: {self._high_score}", align="center", font=FONT)

    def game_over_message(self):
        self.update_message()
        self.goto(0, 0)
        self.pencolor("yellow")
        self.write(arg="Game Over", align="center", font=FONT_GAMEOVER)

    def store_results(self):
        with open(HS_FILE, mode='w') as file:
            file.write(str(self._high_score))
