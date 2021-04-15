# Snake Game
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

positions = [(0, 0), (-20, 0), (-40, 0)]

for pos in positions:
    seg = Turtle(shape="square")
    seg.color("white")
    seg.goto(pos)


screen.exitonclick()
