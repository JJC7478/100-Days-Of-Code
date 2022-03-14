student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height+= height

total_number = 0
for number in student_heights:
     total_number +=1

average_height = (total_height/total_number)
print(round(average_height))