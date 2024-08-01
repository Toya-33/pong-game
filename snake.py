from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segment[len(self.segment)-1].position())

    def refresh(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def add_segment(self, position):
        timmy = Turtle()
        timmy.shape("square")
        timmy.penup()
        timmy.goto(position)
        self.segment.append(timmy)

    def move(self):
        for i in range(len(self.segment)-1, 0, -1):
            x = self.segment[i-1].xcor()
            y = self.segment[i-1].ycor()
            self.segment[i].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
