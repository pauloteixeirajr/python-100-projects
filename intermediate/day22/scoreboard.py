from turtle import Turtle

FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p2_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.p1_score, align="center", font=FONT)

    def p1_point(self):
        self.p1_score += 1
        self.update_board()

    def p2_point(self):
        self.p2_score += 1
        self.update_board()
