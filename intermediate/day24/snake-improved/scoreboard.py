from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.load_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def load_highscore(self):
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def save_highscore(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGN,
            font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()

        self.score = 0
        self.update_scoreboard()
