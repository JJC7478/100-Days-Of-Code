from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
#--------------------------- Word Generation ----------------------------------------#
word_list = pandas.read_csv("Flashy-App/data/french_words.csv")
french_words = word_list.to_dict(orient="records")

def next_word():
    word_choice = random.choice(french_words)
    french_word = word_choice["French"]
    english_word = word_choice["English"]

    canvas.itemconfig(word_text, text=f"{french_word}")
    window.after(3000, switch_side)

#---------------------------- Card Switch -------------------------------------------#
def switch_side():
    canvas.itemconfig(card_img, image= back_img)
    canvas.itemconfig(language_text, text="English", fill="white")


#---------------------------------- UI ----------------------------------------------#
#Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Flashcard Image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="Flashy-App/images/card_front.png")
back_img = PhotoImage(file="Flashy-App/images/card_back.png")
card_img = canvas.create_image(400,263, image=front_img)
language_text = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400,263, text="Sample", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Wrong Button
wrong_img = PhotoImage(file="Flashy-App/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)

#Right Button
right_img = PhotoImage(file="Flashy-App/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_word)
right_button.grid(column=1, row=1)





window.mainloop()