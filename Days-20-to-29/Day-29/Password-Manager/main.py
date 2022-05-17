from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pw_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    random_letters = [choice(letters) for letter in range(randint(8, 10))]
    random_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    random_numbers = [choice(numbers) for number in range(randint(2, 4))]

    char_list = [random_letters, random_symbols, random_numbers]
    char_list = [char for sublist in char_list for char in sublist]

    shuffle(char_list)

    password = "".join(char_list)

    pw_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_entry.get()
    email = eu_entry.get()
    password = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing Fields", message="You left one or more fields blank. Please fill them in before proceeding.")
    else:
        try:
            with open("data.json", mode="r") as df:
                #Reading old data
                data = json.load(df)
        except FileNotFoundError:
            with open("data.json", "w") as df:
                json.dump(new_data, df, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as df:
                #Saving updated data
                json.dump(new_data, df, indent=4)
        finally:
            web_entry.delete(0,END)
            pw_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("My Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="Password-Manager/logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

#Generate Password Button
pw_button = Button(text="Generate Password", command=generate_password)
pw_button.grid(column=2, row=3, sticky="EW")


#Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

#Website Text Entry
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
web_entry.focus()

#Email/Username Text Entry
eu_entry = Entry(width=35)
eu_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
eu_entry.insert(0, string="johnjonahc@gmail.com")

#Password entry
pw_entry = Entry(width=32)
pw_entry.grid(column=1, row=3, sticky="W")


#Website Label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

#Email/Username Label
eu_label = Label(text="Email/Username:")
eu_label.grid(column=0, row=2)

#Password Label
pw_label = Label(text="Password: ")
pw_label.grid(column=0, row=3)













window.mainloop()

