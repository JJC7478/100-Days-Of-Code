from turtle import Turtle, Screen
#to alias a module: 
#   import turtle as t


tim = Turtle()
tim.shape("arrow")
tim.color("cyan")

# for n in range(4):
#     tim.forward(100)
#     tim.right(90)

for n in range(10):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)























screen = Screen()
screen.exitonclick()