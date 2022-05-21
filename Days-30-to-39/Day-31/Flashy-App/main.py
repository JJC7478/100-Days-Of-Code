from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
#--------------------------- Word Generation ----------------------------------------#
try:
    word_list = pandas.read_csv("Flash-App/data/words_to_learn.csv")
except FileNotFoundError:
    word_list = pandas.read_csv("Flashy-App/data/french_words.csv")
    french_words = word_list.to_dict(orient="records")
else:
    french_words = word_list.to_dict(orient="records")
finally:
    current_card = {}
    words_to_learn = []

def next_word():
    global current_card, card_counter
    window.after_cancel(card_counter)
    current_card = random.choice(french_words)
    french_word = current_card["French"]

    canvas.itemconfig(card_img, image=front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{french_word}", fill="black")
    card_counter = window.after(3000, switch_side)
    

#---------------------------- Card Switch -------------------------------------------#
def switch_side():
    canvas.itemconfig(card_img, image= back_img)
    canvas.itemconfig(language_text, text="English", fill="white")

    try:
        english_word = current_card["English"]
    except KeyError:
        english_word = "English Word"
    canvas.itemconfig(word_text, text=f"{english_word}", fill="white")

#---------------------------- Word Removal ------------------------------------------#
def remove_word():
    past_card = current_card
    next_word()
    try:
        french_words.remove(past_card)
    except ValueError:
        pass

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
word_text = canvas.create_text(400,263, text="French Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

card_counter = window.after(3000, switch_side)

#Unknown Button
cross_img = PhotoImage(file="Flashy-App/images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_word)
unknown_button.grid(column=0, row=1)

#Known Button
check_img = PhotoImage(file="Flashy-App/images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=remove_word)
known_button.grid(column=1, row=1)

window.mainloop()
#-------------------------- Words to Learn CSV -------------------------------------#

words_to_learn = french_words
df = pandas.DataFrame(words_to_learn)
df.to_csv("Flashy-App/data/words_to_learn.csv", index=False)
print(df)
