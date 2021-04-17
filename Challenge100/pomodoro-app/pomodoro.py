from tkinter import Tk, Canvas, PhotoImage, Button, Label
import time
import math
import os

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
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():

    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ,
def start_timer():
    global reps

    reps += 1
    if reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)

    elif reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        countdown(LONG_BREAK_MIN*60)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    # HOW TO SHOW COUNTDOWN MIN AND SEC
    count_sec = count % 60
    # Dynamic Typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    count_min = math.floor(count / 60)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#######################################
# creating absolute path with os module
image = os.path.abspath("pomodoro-app/tomato.png")
######################################
background_img = PhotoImage(file=image)

canvas.create_image(100, 112, image=background_img)

canvas.grid(row=1, column=2)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=3)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=2)

check_label = Label(bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 15, "bold"))
check_label.grid(row=3, column=2)

window.mainloop()
