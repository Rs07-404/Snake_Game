from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape('square')
            new_segment.color('white')
            # new_segment.speed(50)
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_seg(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape('square')
        new_segment.color('white')
        self.segments.append(new_segment)

    def xcor(self):
        return self.head.xcor()

    def ycor(self):
        return self.head.ycor()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def increase_length(self):
        self.add_seg()

    def reset(self):
        global STARTING_POSITIONS
        for seg in self.segments:
            seg.clear()
            seg.goto(1000, 1000)
        del self.segments[0:]
        self.create_snake()
        print(self.xcor())
        self.head = self.segments[0]
        self.segments[0].forward(MOVE_DISTANCE)
