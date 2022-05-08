from turtle import Turtle, position

MOVE = False
ALIGN = "center"
FONT = ("Arial", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(arg=f"{self.score}/50", move=MOVE, align=ALIGN, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}/50", move=MOVE, align=ALIGN, font=FONT)