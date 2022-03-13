student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

#Scores 91-100 == "Outstanding"
#Scores 81-90 == "Exceeds Expectations"
#Scores 71-80 == "Acceptable"
#Scores <=79 == "Fail"

for scores in student_scores:
    student_grades[scores] = student_scores[scores]
    if student_grades[scores] >= 91 and student_grades[scores] <= 100:
        student_grades[scores] = "Outstanding"
    elif student_grades[scores] >= 81 and student_grades[scores] <= 90:
        student_grades[scores] = "Exceeds Expectations"
    elif student_grades[scores] >= 71 and student_grades[scores] <= 80:
        student_grades[scores] = "Acceptable"
    else:
        student_grades[scores] = "Fail"
    

print(student_grades)