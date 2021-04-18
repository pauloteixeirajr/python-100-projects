from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Question",
            width=280,
            font=FONT,
            fill=THEME_COLOR
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Labels
        self.score_lbl = Label(text="Score: 0/0", bg=THEME_COLOR, fg="white")
        self.score_lbl.grid(row=0, column=1)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(
            image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(
            image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_lbl.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
