from turtle import Turtle, Screen
import turtle
import pandas
from writer import Writer
from scoreboard import Scoreboard

screen = Screen()
screen.title("U.S. States Game")

image = "us-states-game/blank_map.gif"
screen.bgpic(image)
screen.setup(width=1.0, height=1.0)
screen.tracer()
writer = Writer()
scoreboard = Scoreboard((300, 300))
data = pandas.read_csv("us-states-game/50_states.csv")

states = data["state"].to_list()

screen.update()
game_is_on = True

while game_is_on:
    answer_state = (screen.textinput(title="Guess The State", prompt="What's another state's name?")).title()
    if answer_state in states:
        state = data["state"] == answer_state
        state_data = data[state]
        writer.write_state((int(state_data.x),int(state_data.y)), answer_state)
        scoreboard.add_score()
    if scoreboard.score == 50:
        exit_game = (screen.textinput(title="Winner!", prompt="You guessed all 50 states! Click anywhere to exit."))
        game_is_on = False
        screen.exitonclick()
        










turtle.mainloop()










