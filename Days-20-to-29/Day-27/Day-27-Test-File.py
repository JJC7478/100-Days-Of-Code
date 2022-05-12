import tkinter
import turtle as t


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text= "New Text")


#Button

button = tkinter.Button(text="Click Me")
button.pack()

window.mainloop()