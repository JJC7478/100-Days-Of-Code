from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for n in question_data:
    question_text = n["text"]
    question_answer = n["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

q_brain = QuizBrain(question_bank)

while q_brain.still_has_questions():
    q_brain.next_question()

print("You've finished the quiz!")
print(f"Your final score is {q_brain.score}/{q_brain.question_number}.")
input()






