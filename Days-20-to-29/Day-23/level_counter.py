from turtle import Turtle
COLOR = "black"
MOVE = False
ALIGN = "left"
FONT = ("Arial", 20, "normal")
class Level_Counter(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color("black")
        self.level = 1
        self.write(arg=f"Level: {self.level}", move=MOVE, align=ALIGN, font=FONT)
        
    
    def write_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=MOVE, align=ALIGN, font=FONT)

    def next_level(self):
        self.level += 1
        if self.level > 3:
            self.level = 1
        self.write_level()
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", move=MOVE, align="center", font=FONT)

    def win_screen(self):
        self.goto(0,0)
        self.write(arg="You beat the game!", move=MOVE, align="center", font=FONT)