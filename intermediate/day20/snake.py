from turtle import Turtle
from typing import List

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self) -> None:
        self.segments: List[Turtle] = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            seg = Turtle(shape="square")
            seg.penup()
            seg.color("white")
            seg.goto(pos)
            self.segments.append(seg)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)
