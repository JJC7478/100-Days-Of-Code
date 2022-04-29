import turtle as t
import time
from paddle import Paddle

#Creates 800x600 black screen
screen = t.Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.update()

screen.listen()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True
while game_on:
    screen.update()





















screen.exitonclick()