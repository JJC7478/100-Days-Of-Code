from tkinter import *
from tkinter import messagebox
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
        self.true_button = Button(image=self.check_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        #False Button
        self.cross_img = PhotoImage(file="Quizzler-App/images/false.png")
        self.false_button = Button(image=self.cross_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        #Score Label
        self.score = 0
        self.score_label = Label(
            text=f"Score: 0", 
            bg=THEME_COLOR, 
            fg="white", 
            font=("Arial", 20, "bold")
            )

        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            messagebox.showinfo(
                title="Congratulations, you finished the game!", 
                message=f"Your final score is: {self.score}/{len(self.quiz.question_list)}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        
    
    def answer_true(self):
        user_answer = "True"
        is_correct = self.quiz.check_answer(user_answer=user_answer)
        self.is_right(is_correct)
        
    
    def answer_false(self):
        user_answer = "False"
        is_correct = self.quiz.check_answer(user_answer=user_answer)
        self.is_right(is_correct)
    
    def is_right(self, correct: bool):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if correct == True:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(2000, self.get_next_question)
        self.window.after_cancel(self.get_next_question)

