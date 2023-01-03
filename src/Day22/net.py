import turtle as t


class PongNet(t.Turtle):

    def __init__(self, screen: t.TurtleScreen):
        super().__init__()
        self._screen = screen
        self.color('white')
        self.width(4)
        self.penup()
        self.hideturtle()

    def draw_net(self,):
        screen_height = self._screen.window_height()
        initial_y_position = -screen_height / 2
        final_y_position = screen_height / 2
        step_size = screen_height / 40
        self.speed(0)
        self.goto(0, initial_y_position)
        self.setheading(90)

        position = initial_y_position
        while position < final_y_position:
            self.pendown()
            self.forward(step_size)
            self.penup()
            self.forward(step_size)
            position += step_size * 2

        self.penup()
