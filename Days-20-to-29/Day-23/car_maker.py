from turtle import Turtle
import random

SHAPE = "square"
COLOR_LIST = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan"]
PACE = 5
HEADING = 180

class Car_Maker(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(SHAPE)
            new_car.penup()
            new_car.color(random.choice(COLOR_LIST))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-220,220))
            new_car.setheading(HEADING)
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.forward(PACE)