from turtle import Turtle
import food

RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:
    _SEGMENT_SIZE = 20
    _STEP_DISTANCE = _SEGMENT_SIZE
    _SEGMENT_SHAPE = 'square'
    _SCREEN_SIZE = 600

    def __init__(self, initial_num_segments: int, screen):
        self._initial_num_segments = initial_num_segments
        self._snake_body = list[Turtle]()
        self._heading = 0
        self._stored_heading = 0
        self._segments_count = 0
        self._screen = screen
        self._prepare_screen()
        self._initialize_segments(initial_num_segments)
        self._head = self._snake_body[0]
        self._screen.update()

    def reset(self):
        self._reset_snake_body()
        self._heading = 0
        self._stored_heading = 0
        self._segments_count = 0
        self._initialize_segments(self._initial_num_segments)
        self._head = self._snake_body[0]
        self._screen.update()

    def _initialize_segments(self, num_segments) -> None:
        for i in range(num_segments):
            turtle_segment = self._make_new_segment()
            self._snake_body.append(turtle_segment)

    def _make_new_segment(self):
        turtle_segment = Turtle(Snake._SEGMENT_SHAPE)
        turtle_segment.pencolor('lightgrey')
        turtle_segment.fillcolor('white')
        turtle_segment.penup()
        turtle_segment.goto(-Snake._SEGMENT_SIZE * self._segments_count, 0)
        self._segments_count += 1
        return turtle_segment

    def add_new_segment(self):
        position_of_last_segment = self._snake_body[-1].pos()
        new_segment = self._make_new_segment()
        new_segment.goto(position_of_last_segment)
        self._snake_body.append(new_segment)

    def _prepare_screen(self):
        self._screen.setup(Snake._SCREEN_SIZE, Snake._SCREEN_SIZE)
        self._screen.bgcolor('black')
        self._screen.title("Snake Game")
        self._screen.tracer(n=0)
        self._screen.listen()
        self._screen.onkey(self._change_heading_left, 'Left')
        self._screen.onkey(self._change_heading_right, 'Right')
        self._screen.onkey(self._change_heading_up, 'Up')
        self._screen.onkey(self._change_heading_down, 'Down')

    def _reset_snake_body(self):
        for segment in self._snake_body:
            segment.hideturtle()
        self._snake_body.clear()

    def loop_step(self) -> None:
        self._stored_heading = self._heading
        for segment_number in range((len(self._snake_body) - 1), 0, -1):
            previous_segment_position = self._snake_body[segment_number - 1].pos()
            self._snake_body[segment_number].goto(previous_segment_position)
        self._head.setheading(self._heading)
        self._head.forward(Snake._STEP_DISTANCE)
        self._screen.update()

    def not_colliding(self) -> bool:
        head_position = self._head.pos()
        head_x_pos = head_position[0]
        head_y_pos = head_position[1]
        head_heading = self._head.heading()
        screen_border = Snake._SCREEN_SIZE / 2 - Snake._SEGMENT_SIZE
        if (head_x_pos >= screen_border and head_heading == 0) or \
                (head_x_pos <= -screen_border and head_heading == 180) or \
                (head_y_pos >= screen_border and head_heading == 90) or \
                (head_y_pos <= -screen_border and head_heading == 270):
            return False
        for segment in self._snake_body[1:]:
            # print(head_position, " : ", self._snake_body[segment_num].pos())
            if segment.distance(head_position) < 19:
                return False
        return True

    def check_food_collision(self, food_piece: food.Food) -> bool:
        food_position = food_piece.pos()
        if self._head.distance(food_position) < 10:
            return True
        else:
            return False

    def head_segment_highlight(self):
        self._head.fillcolor('navajowhite')

    def head_segment_unhighlight(self):
        self._head.fillcolor('white')

    def _change_heading_left(self):
        if self._stored_heading != RIGHT:
            self._heading = LEFT

    def _change_heading_right(self):
        if self._stored_heading != LEFT:
            self._heading = RIGHT

    def _change_heading_up(self):
        if self._stored_heading != DOWN:
            self._heading = UP

    def _change_heading_down(self):
        if self._stored_heading != UP:
            self._heading = DOWN
