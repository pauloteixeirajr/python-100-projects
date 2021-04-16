from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.title("PyPong")
screen.setup(width=800, height=600)
screen.tracer(0)

player1 = Paddle(350)
player2 = Paddle(-350)

screen.listen()
screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
