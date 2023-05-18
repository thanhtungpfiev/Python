import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle_map = turtle.Turtle()
turtle_map.shape(image)

display = turtle.Turtle()
display.penup()
display.hideturtle()

answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name?").title()

data = pandas.read_csv('50_states.csv')
data_states = data['state'].tolist()
correct_states = []

while len(correct_states) < 50:
    if answer_state == "Exit":
        remained_state = set(data_states) - set(correct_states)
        pandas.DataFrame(remained_state).to_csv('states_to_learn.csv')
        break
    if answer_state in data_states and answer_state not in correct_states:
        correct_states.append(answer_state)
        correct_state = data[data['state'] == answer_state]
        display.goto(int(correct_state.iloc[0]['x']), int(correct_state.iloc[0]['y']))
        display.write(answer_state)
    answer_state = screen.textinput(title=f'{len(correct_states)}/50 States Correct', prompt="What's another state's name?").title()


screen.exitonclick()
