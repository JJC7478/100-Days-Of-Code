import random
import pandas
#List comprehension

#Lists

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]

#Strings

# name = "JohnJonah"
# new_name = [letter for letter in name]

#Ranges

# new_range = [number * 2 for number in range(1,5)]
# print(new_range)

#Conditional list comprehension

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_names = [name for name in names if len(name) > 4]
# upper_names = [name.upper() for name in names if len(name) > 4]
# print(upper_names)

#Dictionary Comprehension

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {name: random.randint(1,100) for name in names}
# passed_students = {name: "passed" for (name, score) in student_scores.items() if score >= 65}
# print(passed_students)

#Looping through dictionaries

# for (name,status) in passed_students.items():
#     print(status)

#Loop over pandas dataframe

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 78, 98]
# }

# student_data_frame = pandas.DataFrame(student_dict)

# for (key,value) in student_data_frame.items():
#     print(key)
#     print(value)

#Loop through rows of dataframe

# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
