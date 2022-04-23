import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

color_list = ["red", "green", "blue", "orange", "yellow", "purple"]
turtle_list = []
y_positions = [-100, -50, 0, 50, 100, 150]

for turtle in range(0,6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color_list[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=(y_positions[turtle]))
    turtle_list.append(new_turtle)


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            exit_screen = screen.textinput(title="Race finished!", prompt=f"The {turtle.pencolor()} turtle won! Type in any key to exit: ")
            is_race_on = False








screen.exitonclick()