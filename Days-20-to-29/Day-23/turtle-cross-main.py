import turtle as t
import time
from player import Player
import random
from car import Car

screen = t.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.tracer(0)

torta = Player((0,-220))
cars = []
for _ in range(40):
    new_car = Car()
    cars.append(new_car)

screen.update()

screen.listen()
screen.onkeypress(torta.up,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    


















screen.exitonclick()