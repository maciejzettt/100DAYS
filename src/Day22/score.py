from gamecomponent import GameFieldComponent
from turtle import TurtleScreen
from gameover import GameOver


FONT = ("Courier", 40, "bold")


class PongScore(GameFieldComponent):

    def __init__(self, screen: TurtleScreen, player_binding: str, x_pos: int):
        super().__init__()
        self._screen = screen
        self._y_pos = screen.window_height() / 2 - 60
        self._x_pos = x_pos
        self._player = player_binding
        self._score = 0
        self.penup()
        self.speed(0)
        self.pencolor('white')
        self.hideturtle()
        self.goto(self._x_pos, self._y_pos)
        self.update_message()

    def increase_score(self, amount: int):
        self._score += amount

    def update_message(self):
        self.clear()
        self.write(arg=self._score, align="center", font=FONT)

    def step(self) -> None:
        self.update_message()
        if self._score == 10:
            print(f"Player {self._player} has won!")
            raise GameOver('')

    def is_valid(self) -> bool:
        return True

    def score(self) -> int:
        return self._score
