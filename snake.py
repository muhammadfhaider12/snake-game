from turtle import Turtle

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOIVNG_DISTANCE = 10


class Snake:

    def __init__(self):
        self.snake_segment = []
        self.create_snake()
        self.snake_head = self.snake_segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.goto(position)
        self.snake_segment.append(segment)


    def extend_segment(self):
        self.add_segment(self.snake_segment[-1].position())
    def move(self):
        for pos in range(len(self.snake_segment) - 1, 0, -1):
            x_corr = self.snake_segment[pos - 1].xcor()
            y_corr = self.snake_segment[pos - 1].ycor()
            self.snake_segment[pos].goto(x_corr, y_corr)
        self.snake_head.forward(MOIVNG_DISTANCE)

    def up(self):
        self.snake_head.setheading(90)

    def down(self):
        self.snake_head.setheading(270)

    def left(self):
        self.snake_head.setheading(180)

    def right(self):
        self.snake_head.setheading(0)
