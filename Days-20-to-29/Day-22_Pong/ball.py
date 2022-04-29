from turtle import Turtle

SHAPE = "circle"
COLOR = "white"
DEFAULT_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = DEFAULT_SPEED
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.current_x = new_x
        self.current_y = new_y
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
    
    def increase_speed(self):
        self.move_speed *= 0.9
            

    def reset_speed(self):
        self.move_speed = DEFAULT_SPEED
