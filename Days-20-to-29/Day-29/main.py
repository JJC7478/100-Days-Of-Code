from tkinter import *

from click import command


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    with open("data.txt", mode="a+") as df:
        df.seek(0)
        df.write(f"{web_entry.get()} | {eu_entry.get()} | {pw_entry.get()}\n")


# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("My Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

#Generate Password Button
pw_button = Button(text="Generate Password")
pw_button.grid(column=2, row=3, sticky="EW")


#Add Button
add_button = Button(text="Add", width=36, command=add_info)
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

