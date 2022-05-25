from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Question Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280, 
            text="This is a question", 
            font=(FONT)
            )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #True Button
        self.check_img = PhotoImage(file="Quizzler-App/images/true.png")
        self.true_button = Button(image=self.check_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        #False Button
        self.cross_img = PhotoImage(file="Quizzler-App/images/false.png")
        self.false_button = Button(image=self.cross_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        #Score Label
        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}", 
            bg=THEME_COLOR, 
            fg="white", 
            font=("Arial", 20, "bold")
            )

        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
