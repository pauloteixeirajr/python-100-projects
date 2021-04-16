from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.level = 1

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.level += 1
        self.goto(STARTING_POSITION)

    def has_reached_finish(self):
        return self.ycor() > FINISH_LINE_Y
