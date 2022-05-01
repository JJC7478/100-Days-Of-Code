import turtle as t
import time
from player import Player

screen = t.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.tracer(0)

torta = Player((0,-220))

screen.update()

screen.listen()
screen.onkeypress(torta.up,"w")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

















screen.exitonclick()