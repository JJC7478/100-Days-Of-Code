from turtle import Turtle, Screen
import turtle
import pandas
from writer import Writer

screen = Screen()
screen.title("U.S. States Game")

image = "us-states-game/blank_map.gif"
screen.bgpic(image)
writer = Writer()
scoreboard = Writer()
data = pandas.read_csv("us-states-game/50_states.csv")

states = data["state"].to_list()
x_pos = data["x"].to_list()
y_pos = data["y"].to_list()

index = data.index

game_is_on = True

while game_is_on:
    answer_state = (screen.textinput(title="Guess The State", prompt="What's another state's name?")).title()
    if answer_state in states:
        state = data["state"] == answer_state
        state_index = index[state]
        state_index_list = state_index.tolist()
        index_int = state_index_list[0]
        x = x_pos[index_int]
        y = y_pos[index_int]
        writer.write_state((x,y), answer_state)
        










turtle.mainloop()










