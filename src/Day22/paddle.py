import collections
import turtle as t

from Day22.ball import PongBall
from gamecomponent import GameFieldComponent


STEP_DISTANCE = 20
CoordsRange = collections.namedtuple("CoordsRange", "lower upper")


class PongPaddle(GameFieldComponent):

    def __init__(self, screen: t.TurtleScreen, player_binding):
        super().__init__()
        self._screen = screen
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color('white')
        self._player = player_binding.upper()
        self.resizemode('user')
        self.shapesize(1.0, 4.0, 1.0)
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
        y_range = self.get_y_range()
        y_max = self.screen.window_height() / 2
        if y_range.upper <= y_max:
            self.forward(STEP_DISTANCE)
            self._screen.update()

    def move_down(self):
        y_range = self.get_y_range()
        y_min = -self.screen.window_height() / 2
        if y_range.lower >= y_min:
            self.back(STEP_DISTANCE)
            self._screen.update()

    def detect_ball_collision(self, ball: PongBall) -> bool:
        y_range = self.get_y_range()
        ball_center_x = ball.xcor()
        ball_center_y = ball.ycor()
        ball_qheading = ball.get_quarter_heading()
        ball_touchpoint_y = ball_center_y
        ball_touchpoint_x = ball_center_x + (-10 if self._player == 'A' else 10)
        if y_range.lower <= ball_touchpoint_y <= y_range.upper:
            if self._player == 'A' and ball_touchpoint_x <= self.get_x_surface_coord() \
                    and ball_qheading in [1, 2]:
                return True
            elif self._player != 'A' and ball_touchpoint_x >= self.get_x_surface_coord() \
                    and ball_qheading in [0, 3]:
                return True
            else:
                return False
        else:
            return False

    def get_y_range(self) -> CoordsRange:
        center_y = self.ycor()
        lower_y = center_y - 40
        upper_y = center_y + 40
        coords = CoordsRange(lower_y, upper_y)
        return coords

    def get_x_surface_coord(self) -> float:
        center_x = self.xcor()
        surface_x = center_x + (10 if self._player == 'A' else -10)
        return surface_x

    def step(self) -> None:
        pass

    def is_valid(self) -> bool:
        return True

