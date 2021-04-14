# Turtle Graphics, Tuples and Importing Modules
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
# Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dashed line
for i in range(20):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()


screen = Screen()
screen.exitonclick()
