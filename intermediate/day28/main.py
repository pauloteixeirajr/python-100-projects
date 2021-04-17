from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_sec)
        title_lbl.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_sec)
        title_lbl.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_lbl.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60

    if min < 10:
        min = f"0{min}"

    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_lbl = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_lbl.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="#fff",
    font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(row=2, column=2)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

# Keep the screen open
window.mainloop()
