BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
from tkinter import messagebox

words_to_revise=pd.read_csv('data/french_words.csv')



def i_know():
    global random_number,words_to_revise
    words_to_revise=words_to_revise.drop(words_to_revise.index[random_number],axis=0)
    next_card()

def next_card():
    if len(words_to_revise)==0:
        messagebox.showinfo(title="Congratulations", message="you have learned every word")
    window.after(3000,flip_card)
    
    global french_word,english_word,random_number
    try:
        random_number=random.randint(0,len(words_to_revise))
        french_word=words_to_revise.iloc[random_number][0]
        english_word=words_to_revise.iloc[random_number][1]
    except:
        random_number=0
        french_word=words_to_revise.iloc[random_number][0]
        english_word=words_to_revise.iloc[random_number][1]

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    flip_card


window=Tk()
window.title("Flash Card")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0,command=i_know)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()