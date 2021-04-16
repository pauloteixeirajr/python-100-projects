from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_board()

    def update_board(self):
        self.write(f"Level {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_board()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
