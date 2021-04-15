from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
