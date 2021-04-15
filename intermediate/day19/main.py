# Building a turtle race
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for i in range(0, len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[i])
    turtle.color(colors[i])

screen.exitonclick()
