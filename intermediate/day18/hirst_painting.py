import random
import turtle as t


def random_color():
    """ Returns a random RGB color """

    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    return (R, G, B)


t.colormode(255)
tim = t.Turtle(shape="arrow")
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots = 100

for dot_count in range(1, number_dots + 1):
    tim.dot(20, random_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)

        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
