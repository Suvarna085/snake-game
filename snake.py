from pickle import FALSE
from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITION:
            self.add_segment(positions)


    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
            for segment in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segment - 1].xcor()
                new_y = self.segments[segment - 1].ycor()
                self.segments[segment].goto(new_x, new_y)
            self.segments[0].forward(MOVE_FORWARD)

    def up(self):
            if self.head.heading() != DOWN:
                self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left_snake(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right_snake(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
