import turtle as t
import time

screen = t.Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle = t.Turtle()
paddle.penup()
paddle.speed("fastest")
paddle.shape("square")
paddle.color("white")
paddle.resizemode("user")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(x=350, y=0)


screen.update()

screen.listen()
def up():
    new_y = paddle.ycor()
    if paddle.ycor() < 280:
        paddle.goto(paddle.xcor(), new_y + 20)

def down():
    new_y = paddle.ycor()
    if paddle.ycor() > -280:
        paddle.goto(paddle.xcor(), new_y - 20)

screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")

game_on = True
while game_on:
    screen.update()





















screen.exitonclick()