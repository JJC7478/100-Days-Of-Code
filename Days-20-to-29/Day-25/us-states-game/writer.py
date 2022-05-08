from turtle import Turtle, position

MOVE = False
ALIGN = "center"
FONT = ("Arial", 12, "bold")

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
    
    def write_state(self, position, state):
        self.goto(position)
        self.write(arg=state, move=MOVE, align=ALIGN, font=FONT)
