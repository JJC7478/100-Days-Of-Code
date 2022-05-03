from turtle import Turtle
import random

SHAPE = "square"
COLOR_LIST = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan"]
STARTING_PACE = 5
INCREMENT = 5
HEADING = 180
STOP = 0

class Car_Maker(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
    
    def starting_cars(self):
        random_chance = random.randint(1,8)
        if random_chance == 1:
            new_car = Turtle(SHAPE)
            new_car.penup()
            new_car.color(random.choice(COLOR_LIST))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(random.randint(-220,220), random.randint(-220,220))
            new_car.setheading(HEADING)
            self.all_cars.append(new_car)
            self.pace = STARTING_PACE
    
    def create_car(self):
        random_chance = random.randint(1,8)
        if random_chance == 1:
            new_car = Turtle(SHAPE)
            new_car.penup()
            new_car.color(random.choice(COLOR_LIST))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-220,220))
            new_car.setheading(HEADING)
            self.all_cars.append(new_car)
            self.pace = STARTING_PACE

    def drive(self):
        for car in self.all_cars:
            car.forward(self.pace)

    def drive_faster(self):
        self.pace += INCREMENT
    
