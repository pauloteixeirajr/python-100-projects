import time
from turtle import Screen
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.title("PyPong")
screen.setup(width=800, height=600)
screen.tracer(0)

player1 = Paddle(350)
player2 = Paddle(-350)
ball = Ball()

screen.listen()
screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")
screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
