from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

#Event Listeners

screen.listen()

#Function as inputs, aka Higher Order Functions

screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()