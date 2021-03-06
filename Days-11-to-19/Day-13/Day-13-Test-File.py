############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): #i never reaches 20; switch end of range to 21
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) #there is no 6th index as the indecies for dice_imgs go from 0-5
#                         #change end parameter of randint to 5 and start parameter to 0
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: #inputting 1994 produces nothing as it does not produce True for each statement
#                                 #should be year > 1980 and year <= 1994
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") #Must turn input into int
# if age > 18:
#     print("You can drive at age {age}.") #Include f for f-string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page == int(input("Number of words per page: ")) #Using '==' instead of '='
# #Use '=' for assignment
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) #need to indent this line so it becomes part of for loop
#   print(b_list)

# mutate([1,2,3,5,8,13])