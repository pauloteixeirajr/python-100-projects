import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
WORDS_DF = pandas.read_csv("./data/french_words.csv")
WORDS_LIST = WORDS_DF.to_dict(orient="records")


# Get Random French Word
def next_card():
    random_card = random.choice(WORDS_LIST)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=random_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
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
    command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
