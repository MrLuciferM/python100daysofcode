import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)



data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="Whats another state's name?").title()
    
    if answer_state == "Exit":
        missed_states = list(set(all_states).difference(set(guessed_states)))
        df = pd.DataFrame(missed_states)
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.up()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


save_file = "missed_states.csv"
df.to_csv(save_file)