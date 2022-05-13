from re import L
import tkinter
import turtle as t

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

#Padding gives more space for widgets
window.config(padx=20, pady=20)

def button_clicked():
    my_label.config(text=input.get())

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

#Two ways of changing label text
my_label["text"] = "New Text"
my_label.config(text= "New Text", padx=100, pady=100)

#Pack stacks each widget next to each other in a vaugely logical format

# my_label.pack()

#Place places a widget in a specific coordinate of the screen

# my_label.place(x=200, y=0)

#Grid creates rows and columns based on the number of widgets and puts a widget on a specified row and column
my_label.grid(column=0, row=0)

#Button

button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=2)

#New Button
new_button = tkinter.Button(text="Click Me Too", command=button_clicked)
new_button.grid(column=2, row=1)

#Entry

input = tkinter.Entry()
# input.pack()
input.grid(column=3, row=3)

window.mainloop()