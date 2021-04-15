# Building a turtle race
import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for i in range(0, len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[i])
    turtle.color(colors[i])
    turtles.append(turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            break
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
