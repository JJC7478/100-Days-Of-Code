import turtle as t
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from border import Border

#Creates 800x600 black screen
screen = t.Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard((400,260))
l_scoreboard = Scoreboard((-400, 260))
border = Border((0,-400))

#Draws middle border
while border.ycor()< 400:
    border.draw_border()

screen.update()

screen.listen()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True
while game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect wall collision
    if ball.current_y > 290 or ball.current_y < -290:
        ball.bounce_y()

    #Detect paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.increase_speed()
    elif l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()
        
    
    #Detect right out of bounds

    if ball.current_x > 400:
        ball.reset_position()
        ball.reset_speed()
        ball.bounce_x()
        l_scoreboard.add_score()

    #Detect left out of bounds
    if ball.current_x < -400:
        ball.reset_position()
        ball.reset_speed()
        ball.bounce_x()
        r_scoreboard.add_score()

















screen.exitonclick()