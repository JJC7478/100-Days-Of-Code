from turtle import Turtle
SPEED = "fastest"
SHAPE = "square"
COLOR = "white"
S_WID = 5
S_LEN = 1


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed(SPEED)
        self.shape(SHAPE)
        self.color(COLOR)
        self.resizemode("user")
        self.shapesize(stretch_wid=S_WID, stretch_len=S_LEN)
        self.goto(position)
    

    def up(self):
        """Moves paddle up when pressing up arrow"""
        new_y = self.ycor()
        if self.ycor() < 280:
            self.goto(self.xcor(), new_y + 20)
    
    def down(self):
        """Moves paddle down when pressing down arrow"""
        new_y = self.ycor()
        if self.ycor() > -280:
            self.goto(self.xcor(), new_y - 20)
