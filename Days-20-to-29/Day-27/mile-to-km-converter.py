from tkinter import *

FONT = ("Arial", 12, "bold")
screen = Tk()
screen.title("Mile to Km Converter")
screen.minsize(width=300, height=300)

#Miles Entry
mile_entry = Entry(width=10)
mile_entry.insert(END, string="0")
mile_entry.grid(column=1, row=0)

#Miles Label
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)


# "is equal to" Label
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=2)

#Km conversion
km_output = Label(text=0, font=(FONT))
km_output.grid(column=1, row=2)

#Km label
km_label = Label(text="km", font=FONT)
km_label.grid(column=2,row=2)

#Calculate Button
def calculate():
    km = round((float(mile_entry.get()) * 1.609), 2)
    km_output["text"] = f"{km}"

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=3)






screen.mainloop()