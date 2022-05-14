from subprocess import check_call
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
count_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(count_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        work_time = long_break_sec
        timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        work_time = short_break_sec
        timer.config(text="Short Break", fg=PINK)
    else:
        work_time = work_sec
        timer.config(text="Work", fg=GREEN)
    
    countdown(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global count_timer

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        count_timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks = ""
            for _ in range(int(reps/2)):
                checkmarks += CHECKMARK
            checkmark.config(text=checkmarks)
        
# ---------------------------- UI SETUP ------------------------------- #
FONT = (FONT_NAME, 35, "bold")

#Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


#Tomato Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white", font=FONT)
canvas.grid(column=1, row=1)


#Timer Label
timer = Label(text="Timer", font=FONT, fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

#Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

#Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

#Checkmark Label
checkmark = Label(font=(FONT_NAME, 12, "bold"),fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=4)

window.mainloop()