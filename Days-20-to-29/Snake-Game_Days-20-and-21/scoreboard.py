from importlib.resources import contents
import turtle as t
MOVE = False
ALIGNMENT = "center"
FONT = ('Impact', 18, 'bold')

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(0,270)
        self.color("white")
        self.score = 0
        with open("high_score.txt") as file:
            self.highscore = int(file.read())
        self.create_score()
        
    
    def create_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=MOVE, align=ALIGNMENT,font=FONT)
    
    def add_score(self):
        self.score += 1
        self.create_score()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="r+") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.create_score()

    # def game_over(self):
    #     self.clear()
    #     self.setposition(0,0)
    #     self.write(arg=f"Game Over! Your final score was: {self.score}", move=MOVE, align=ALIGNMENT,font=FONT)
