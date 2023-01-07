from gamecomponent import GameFieldComponent
from turtle import TurtleScreen
from random import randint, choice


STEP_DISTANCE = 8


class PongBall(GameFieldComponent):

    def __init__(self, screen: TurtleScreen):
        super().__init__()
        self.screen = screen
        self.shape('circle')
        self.color('lightgrey')
        self.speed(0)
        self.penup()
        self._random_start()

    def _random_start(self):
        origins = [15, 105, 195, 285]
        starting_angle = choice(origins) + randint(0, 60)
        self.setheading(starting_angle)

    def step(self) -> None:
        self.forward(STEP_DISTANCE)
        self.screen.update()

    def is_valid(self) -> bool:
        return True

