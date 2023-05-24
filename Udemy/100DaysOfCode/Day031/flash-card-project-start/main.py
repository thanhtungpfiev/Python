import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
WORDS_TO_LEARN = "data/words_to_learn.csv"

# Handle data
try:
    data = pandas.read_csv(WORDS_TO_LEARN).to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

my_timer = ''


def update_card(key, new_data):
    if key == 'English':
        canvas.itemconfig(canvas_image, image=card_back_img)
        canvas.itemconfig(title_text, fill="white")
        canvas.itemconfig(word_text, fill="white")
    else:
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(title_text, fill="black")
        canvas.itemconfig(word_text, fill="black")

    canvas.itemconfig(title_text, text=key)
    canvas.itemconfig(word_text, text=new_data[key])


def next_card(type_button):
    global my_timer
    if my_timer != '':
        window.after_cancel(my_timer)
    new_data = random.choice(data)
    key = 'French'
    update_card(key, new_data)
    my_timer = window.after(3000, flip_card, new_data)
    if type_button == 'right':
        data.remove(new_data)
        pandas.DataFrame(data).to_csv(WORDS_TO_LEARN, index=False)


def flip_card(new_data):
    window.after_cancel(my_timer)
    key = 'English'
    update_card(key, new_data)


# Setup UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda: next_card('wrong'))
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=lambda: next_card('right'))
right_button.grid(row=1, column=1)

next_card('')

window.mainloop()
