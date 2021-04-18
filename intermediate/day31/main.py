import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
try:
    WORDS_DF = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    WORDS_DF = pandas.read_csv("./data/french_words.csv")
WORDS_LIST = WORDS_DF.to_dict(orient="records")
CURRENT_CARD = None
FLIP_TIMER = None


# Get Random French Word
def next_card():
    global CURRENT_CARD, FLIP_TIMER
    if FLIP_TIMER:
        window.after_cancel(FLIP_TIMER)
    CURRENT_CARD = random.choice(WORDS_LIST)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=CURRENT_CARD["French"], fill="black")
    FLIP_TIMER = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=CURRENT_CARD["English"], fill="white")


def is_known():
    WORDS_LIST.remove(CURRENT_CARD)
    data = pandas.DataFrame(WORDS_LIST)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263)
title_text = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)

canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(
    image=wrong_image,
    highlightthickness=0,
    command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(
    image=right_image,
    highlightthickness=0,
    command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
