from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Question",
            font=FONT,
            fill=THEME_COLOR
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Labels
        self.score_lbl = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_lbl.grid(row=0, column=1)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()
