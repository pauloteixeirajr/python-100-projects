# Turtle Graphics, Tuples and Importing Modules
import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
timmy.shape("turtle")
# Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dashed line
# for i in range(20):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

# # Drawing Different Shapes
# for i in range(3, 11):
#     angle = 360 / i
#     timmy.color(colors[i - 3])
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(angle)

# Generate a random walk
directions = [0, 90, 180, 270]

timmy.pensize(10)
timmy.speed("fast")
colormode(255)


def random_color():
    """ Returns a random RGB color """

    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    return (R, G, B)


for _ in range(500):
    timmy.color(random_color())
    timmy.forward(50)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
