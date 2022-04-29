from turtle import Turtle
import turtle

COLOR = "white"
SHAPE = "square"

class Border(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.hideturtle()
        self.goto(position)
        self.color(COLOR)
        self.setheading(90)
        self.pensize(10)
        
    
    def draw_border(self):
        self.pendown()
        self.forward(10)
        self.penup()
        self.forward(20)