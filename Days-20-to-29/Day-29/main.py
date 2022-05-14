from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("My Password Manager")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

#Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

#Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#Email/Username Label
eu_label = Label(text="Email/Username:")
eu_label.grid(column=0, row=2)

#Password Label
pw_label = Label(text="Password: ")
pw_label.grid(column=0, row=3)













window.mainloop()

