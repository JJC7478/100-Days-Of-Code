from turtle import Turtle, forward

SHAPE = "turtle"
COLOR = "black"
POSITION = (0,-220)

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.setheading(90)
        self.goto(position)
    
    def up(self):
        self.forward(20)


    