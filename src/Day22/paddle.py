import turtle as t
from gamecomponent import GameFieldComponent


STEP_DISTANCE = 8


class PongPaddle(GameFieldComponent):

    def __init__(self, screen: t.TurtleScreen, player_binding):
        super().__init__()
        self._screen = screen
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self._player = player_binding
        self.resizemode('user')
        self.shapesize(1.0, 4.0, 1.0)
        self.penup()
        self.setheading(90)
        self._paddle_set()

    def _paddle_set(self):
        basic_x_position = self._screen.window_width() / 2 - 30
        if self._player.upper() == 'A':
            self.goto(-basic_x_position, 0)
        else:
            self.goto(basic_x_position, 0)
        self.showturtle()

    def move_up(self):
        self.forward(STEP_DISTANCE)
        self._screen.update()

    def move_down(self):
        self.back(STEP_DISTANCE)
        self._screen.update()

    def step(self) -> None:
        pass

    def is_valid(self) -> bool:
        return True

