import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Handle data
data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


def next_card():
    new_data = random.choice(data)
    key = 'French'
    on_change_text(key, new_data[key])


def on_change_text(title_arg, word_arg):
    canvas.itemconfig(title_text, text=title_arg)
    canvas.itemconfig(word_text, text=word_arg)


# Setup UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
