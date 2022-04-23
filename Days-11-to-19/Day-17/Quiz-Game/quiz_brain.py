#TODO Check if the answer was correct
#TODO Check if you're at end of quiz

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def next_question(self):
        q_list = self.questions_list
        current_question = q_list[self.question_number]
        current_text = current_question.text
        correct_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_text} True or False?: ")
        self.check_answer(user_answer, correct_answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct! Your score is {self.score}/{self.question_number}")
            input("Press Enter to continue")
        else:
            print(f"Wrong. Your score is {self.score}/{self.question_number}")
            input("Press Enter to continue")
    