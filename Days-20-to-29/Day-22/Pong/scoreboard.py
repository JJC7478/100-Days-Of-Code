from turtle import Turtle

COLOR = "white"
MOVE = False
ALIGN = "center"
FONT = ("Arial", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(position)
        self.score = 0
        self.write(arg=f"{self.score}", move=MOVE, align=ALIGN, font=FONT)
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", move=MOVE, align=ALIGN, font=FONT)