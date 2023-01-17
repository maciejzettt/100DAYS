import time
from random import randint
from turtle import TurtleScreen

from gamecomponent import GameFieldComponent

STEP_DISTANCE = 8


class PongBall(GameFieldComponent):

    def __init__(self, screen: TurtleScreen):
        super().__init__()
        self.screen = screen
        self.shape('circle')
        self.color('lightgrey')
        self.speed(0)
        self.penup()
        self._quarter_heading = 0
        self._random_start()

    def _random_start(self):
        origins = [20, 110, 200, 290]
        starting_quarter = randint(0, 3)
        quarter_offset = randint(0, 50)
        starting_angle = origins[starting_quarter] + quarter_offset
        self.setheading(starting_angle)
        self._quarter_heading = starting_quarter

    def restart(self):
        self.setposition(0, 0)
        self._random_start()
        time.sleep(2)

    def step(self) -> None:
        self.forward(STEP_DISTANCE)
        if self.collides_with_horizontal_walls():
            print('Horizontal wall collision.')
            self.bounce_horizontal_walls()
        self.screen.update()

    def bounce_paddle(self) -> None:
        if self._quarter_heading == 0:
            self.setheading(180 - self.heading())
            self._quarter_heading = 1
        elif self._quarter_heading == 1:
            self.setheading(180 - self.heading())
            self._quarter_heading = 0
        elif self._quarter_heading == 2:
            self.setheading(360 + 180 - self.heading())
            self._quarter_heading = 3
        else:
            self.setheading(360 + 180 - self.heading())
            self._quarter_heading = 2

    def collides_with_horizontal_walls(self) -> bool:
        x_min = - self.screen.window_width() / 2
        x_max = self.screen.window_width() / 2
        y_min = - self.screen.window_height() / 2 + 10
        y_max = self.screen.window_height() / 2 - 10
        x_touchpoint = self.xcor()
        if self._quarter_heading == 0 or self._quarter_heading == 1:
            y_touchpoint = self.ycor() + 10
            if x_min <= x_touchpoint <= x_max and y_touchpoint >= y_max:
                return True
        if self._quarter_heading == 2 or self._quarter_heading == 3:
            y_touchpoint = self.ycor() - 10
            if x_min <= x_touchpoint <= x_max and y_touchpoint <= y_min:
                return True
        return False

    def exited_field(self) -> object:
        x_min = - self.screen.window_width() / 2 + 10
        x_max = self.screen.window_width() / 2 - 10
        y_min = - self.screen.window_height() / 2
        y_max = self.screen.window_height() / 2
        y_touchpoint = self.ycor()
        if self._quarter_heading == 0 or self._quarter_heading == 3:
            x_touchpoint = self.xcor() + 10
            if y_min <= y_touchpoint <= y_max and x_touchpoint >= x_max:
                return 'A'
        if self._quarter_heading == 1 or self._quarter_heading == 2:
            x_touchpoint = self.xcor() - 10
            if y_min <= y_touchpoint <= y_max and x_touchpoint <= x_min:
                return 'B'
        return False

    def bounce_horizontal_walls(self) -> None:
        new_heading_quarters = [3, 2, 1, 0]
        self.setheading(360 - self.heading())
        self._quarter_heading = new_heading_quarters[self._quarter_heading]

    def is_valid(self) -> bool:
        return True

    def get_quarter_heading(self):
        return self._quarter_heading
