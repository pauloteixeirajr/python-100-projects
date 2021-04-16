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

answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state's name?")

# Keep screen open
turtle.mainloop()
