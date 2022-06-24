import turtle
import pandas
import random

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"Guess the State: {len(guessed_states)}/50",
                                     prompt="What's another states name?")).title()
    if answer_state == "Exit":
        states_to_learn = [item for item in all_states if item not in guessed_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn4.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state_data = data[data.state == answer_state]
        state.goto(int(state_data.x), int(state_data.y))
        state.write(answer_state)


