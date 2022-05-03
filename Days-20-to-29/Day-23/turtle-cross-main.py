import turtle as t
import time
from player import Player
import random
from car_maker import Car_Maker

screen = t.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.tracer(0)

torta = Player((0,-220))
car_maker = Car_Maker()


screen.update()

screen.listen()
screen.onkeypress(torta.up,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_maker.create_car()
    car_maker.drive()
    


















screen.exitonclick()