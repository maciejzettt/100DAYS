import turtle as t


class PongPaddle(t.Turtle):

    def __init__(self, screen: t.TurtleScreen, player):
        super().__init__()
        self._screen = screen
        self.shape('square')
        self.color('white')
        self._player = player
        self.resizemode('user')
        self.shapesize(4.0, 1.0, 1.0)
        self.speed(0)
        self.penup()
        self._paddle_set()

    def _paddle_set(self):
        basic_x_position = self._screen.window_width() / 2 - 30
        if self._player.upper() == 'A':
            self.goto(-basic_x_position, 0)
        else:
            self.goto(basic_x_position, 0)

