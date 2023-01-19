from turtle import Turtle


class Player(Turtle):
    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(Player.MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor() >= Player.FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(Player.STARTING_POSITION)
