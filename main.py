import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

game_over = False
screen.addshape(image)

turtle.shape(image)

while game_over == False:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_state:
        answer_state = answer_state.lower()
           


