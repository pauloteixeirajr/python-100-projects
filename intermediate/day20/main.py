# Snake Game
import time
from turtle import Screen, Turtle
from typing import List

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
segments: List[Turtle] = []

for pos in positions:
    seg = Turtle(shape="square")
    seg.penup()
    seg.color("white")
    seg.goto(pos)
    segments.append(seg)
    screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x=new_x, y=new_y)
    segments[0].forward(20)


screen.exitonclick()
