import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_positions = [(0,0), (-20,0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = t.Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(5)
















screen.exitonclick()