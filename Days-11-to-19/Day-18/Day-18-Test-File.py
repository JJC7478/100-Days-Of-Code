from re import A, S
from turtle import Turtle, Screen
import random
#to alias a module: 
#   import turtle as t


tim = Turtle()
tim.shape("arrow")
tim.color("cyan")

# for n in range(4):
#     tim.forward(100)
#     tim.right(90)

# for n in range(10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# triangle = 120 degrees
# square = 90 degrees
# pentagon = 72 degrees
# hexagon = 60 degrees
# heptagon =


# n = 2
# for x in range(3,11):
#     n += 1
#     angle = 360/n
#     shape_making = True
#     if n == 11:
#         break
#     while shape_making:
#         for p in range(1, n+1):
#             tim.forward(100)
#             tim.right(angle)
#             if p == n:
#                 shape_making = False
    
# is_walking = True
# while is_walking:
#     tim.pensize(10)
#     tim.speed(5)
#     for n in range(100):
#         red = random.random() 
#         green = random.random() 
#         blue = random.random() 
#         tim.color(red, green, blue)
#         dice = random.randint(1,2)
#         if dice == 1:
#             tim.left(90)
#         elif dice == 2:
#             tim.right(90)
#         dice_1 = random.randint(1,2)
#         if dice_1 == 1:
#             tim.forward(25)
#         elif dice_1 == 2:
#             tim.backward(25)


#Tuples
my_tuple = (1, 3, 8)
# tuples cannot be altered compared to other data values
#e.g., my_tuple[2] = 12

def draw_spirograph(size):
    for n in range(int(360/size)):
        tim.speed(0)
        tim.setheading(tim.heading() + size)
        red = random.random() 
        green = random.random() 
        blue = random.random() 
        tim.color(red, green, blue)
        tim.circle(50)

draw_spirograph(10)
















screen = Screen()
screen.exitonclick()