from gamecomponent import GameFieldComponent
import turtle as t


class PongNet(GameFieldComponent):

    def __init__(self, screen: t.TurtleScreen):
        super().__init__()
        self._screen = screen
        self.color('white')
        self.width(4)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.draw_net()

    def draw_net(self,):
        screen_height = self._screen.window_height()
        initial_y_position = -screen_height / 2
        final_y_position = screen_height / 2
        step_size = screen_height / 40
        self.goto(0, initial_y_position)
        self.setheading(90)

        position = initial_y_position
        while position < final_y_position:
            self.pendown()
            self.forward(step_size - 2)
            self.penup()
            self.forward(step_size + 2)
            position += step_size * 2

        self.penup()

    def step(self) -> None:
        pass

    def is_valid(self) -> bool:
        return True
