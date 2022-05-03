from turtle import Turtle
import random

SHAPE = "square"
COLOR_LIST = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan"]
PACE = 2
HEADING = 180

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(random.choice(COLOR_LIST))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randint(-220,220), random.randint(-220,220))
        self.setheading(HEADING)
    
    def drive(self):
        self.forward(PACE)