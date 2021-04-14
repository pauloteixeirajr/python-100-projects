# Turtle Graphics, Tuples and Importing Modules
from turtle import Turtle, Screen

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

colors = [
    "CornflowerBlue", "DarkOrchid", "IndianRed",
    "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]

# Drawing Different Shapes
for i in range(3, 11):
    angle = 360 / i
    timmy.color(colors[i - 3])
    for _ in range(i):
        timmy.forward(100)
        timmy.right(angle)

screen = Screen()
screen.exitonclick()
