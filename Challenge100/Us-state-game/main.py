import turtle
import pandas


screen = turtle.Screen()
image_turtle = turtle.Turtle()
screen.title("U.S State Game")
image = "Us-state-game/blank_states_img.gif"
screen.addshape(image)
image_turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
# CSV
data = pandas.read_csv("Us-state-game/50_states.csv")
state_list = data.state.to_list()

guessed_state = []
while len(guessed_state) < 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 States Correct", prompt="Whats another state name").title()
    if answer_state == "Exit":
        # DATA SAVING
        record = []
        for state in state_list:
            if state not in guessed_state:
                record.append(state)
        record_data = pandas.DataFrame(record)
        record_data.to_csv("Us-state-game/states_learn.csv")

        break
    if answer_state in state_list:
        guessed_state.append(answer_state)
        new_state = data[data.state == answer_state]

        pen.goto(int(new_state.x), int(new_state.y))

        pen.write(arg=answer_state)  # new_state.state.item()
