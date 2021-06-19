from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Functionality

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

card = {}

def next_card():
    global card
    global flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card["English"], fill="white")


def is_known():
    to_learn.remove(card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("French Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


# UI

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)


card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file="./images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front)

language_text = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

cross = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

tick = PhotoImage(file="./images/right.png")
known_button = Button(image=tick, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()