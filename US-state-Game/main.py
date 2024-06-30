import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("us.csv")
All_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_state)}/50 Guess", 
                                     prompt="WHat's another state name").title()
    if answer_states == "Exit":
        missing_state = []
        for state in All_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("Missing_state.csv")

        break
    if answer_states in All_states:
        guessed_state.append(answer_states)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_states)









