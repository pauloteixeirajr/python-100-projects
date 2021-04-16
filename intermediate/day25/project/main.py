import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./intermediate/day25/project/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
states = pandas.read_csv("./intermediate/day25/project/50_states.csv")

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(
        title=f"{len(correct_guesses)}/{states.state.size} States Correct",
        prompt="What's another state's name?"
    ).title()

    if answer_state == "Exit":
        break

    state = states[states.state == answer_state]
    if not state.empty and answer_state not in correct_guesses:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)
        correct_guesses.append(answer_state)
