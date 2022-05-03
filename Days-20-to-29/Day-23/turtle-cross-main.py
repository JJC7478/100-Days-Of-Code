import turtle as t
import time
from level_counter import Level_Counter
from player import Player
import random
from car_maker import Car_Maker

TURTLE_START = (0,-240)

screen = t.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.tracer(0)

torta = Player(TURTLE_START)
car_maker = Car_Maker()
level_counter = Level_Counter((-280,230))

for _ in range(100):
    car_maker.starting_cars()


screen.update()

screen.listen()
screen.onkey(torta.up,"w")

game_is_on = True

while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_maker.create_car()
        car_maker.drive()

        #Level Finish
        if torta.ycor() > 220:
            #Game Win
            if level_counter.level == 3:
                level_counter.win_screen()
                game_is_on = False
            else:
                level_counter.next_level()
                torta.goto(TURTLE_START)
                car_maker.drive_faster()
        
        #Detect car collision
        for car in car_maker.all_cars:
            if torta.distance(car) < 20:
                level_counter.game_over()
                game_is_on = False




















screen.exitonclick()