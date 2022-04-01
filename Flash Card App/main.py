from tkinter import *
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOUR = "#B1DDC6"


def start_game():
    check = messagebox.askyesno("Game Start!", "Shall we start the game?")
    if check:
        new_animal()
    else:
        exit(0)


def new_animal():
    if len(english_list) == 0:
        messagebox.showinfo("You Won!", "You have completely memorized the entire list!\nGood job!")
        exit(0)
    else:
        global katakana
        global romaji
        global english
        number = random.randint(0, len(english_list) - 1)
        katakana = katakana_list[number]
        romaji = romaji_list[number]
        english = english_list[number]
        canvas.itemconfig(english_text, text="")
        canvas.itemconfig(katakana_text, text=katakana)
        canvas.itemconfig(romaji_text, text=romaji)
        canvas.itemconfig(flash_card, image=card_back_img)
        canvas.after(3000, show_answer)


def correct_guess():
    global romaji_list
    global katakana_list
    global english_list
    romaji_list.remove(romaji)
    english_list.remove(english)
    katakana_list.remove(katakana)
    new_animal()


def show_answer():
    canvas.itemconfig(flash_card, image=card_front_img)
    canvas.itemconfig(english_text, text=english)
    canvas.itemconfig(romaji_text, text="")
    canvas.itemconfig(katakana_text, text="")
    canvas.after_cancel(show_answer)


window = Tk()
window.minsize(width=300, height=300)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)
window.title("Japanese Animals")

# Creating database
database = pandas.read_csv("Japanese_Animals.csv")
katakana_list = database["Katakana"].to_list()
romaji_list = database["Romaji"].to_list()
english_list = database["Meaning"].to_list()
katakana = ""
romaji = ""
english = ""

# Creating Images
card_back_img = PhotoImage(file="card_back.png")
card_front_img = PhotoImage(file="card_front.png")
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOUR, highlightthickness=0)
flash_card = canvas.create_image(400, 263, image=card_back_img)
katakana_text = canvas.create_text(400, 150, text="Katakana", font=("Ariel", 40, "italic"))
romaji_text = canvas.create_text(400, 263, text="Romaji", font=("Ariel", 60, "bold"))
english_text = canvas.create_text(400, 250, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right = Button(image=right_img, highlightthickness=0, bd=0, command=correct_guess)
right.grid(row=1, column=1)
wrong = Button(image=wrong_img, highlightthickness=0, bd=0, command=new_animal)
wrong.grid(row=1, column=0)

start_game()


window.mainloop()
