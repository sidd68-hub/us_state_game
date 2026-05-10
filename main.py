import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missing_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)/50}", prompt="What's another state's name?")

    if answer_state is None:
        break

    if answer_state is "Exit":
        for item in all_states:
            if item not in guessed_states:
                missing_states.append(item)
           
        data_dic = {
    "Missing State": missing_states
}

        df = pandas.DataFrame(data_dic)
        df.to_csv('missing_states.csv')
        break

    answer_state = answer_state.strip().title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

