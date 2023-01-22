import turtle
import pandas

image = "blank_states_img.gif"

#SETUP
screen = turtle.Screen()
screen.title("US States")
# shape = turtle.Shape('image', image)
screen.addshape(image)
us_map = turtle.Turtle()
us_map.shape(image)
correct_answers = 0
correct_states_names = []
correct_states_labels = []
states_data = pandas.read_csv('50_states.csv')


def get_mouse_click_coords(x, y):
    print(x, y)


def get_state_name_input() -> str:
    raw_answer = screen.textinput(f"{correct_answers}/50 Correct", "What's another state?")
    return raw_answer.title()


def check_answer(answer: str) -> pandas.DataFrame | bool:
    matching_entries = states_data[states_data.state == answer]
    num_entries = len(matching_entries)
    if num_entries == 0:
        return False
    else:
        return matching_entries


def answer_to_xy(correct_entry: pandas.DataFrame | bool) -> tuple[float, float]():
    if len(correct_entry) != 1 or type(correct_entry) is not pandas.DataFrame:
        raise IndexError("Index of correct answer is ambiguous: data file might contain repeating entries")
    x = float(correct_entry.x)
    y = float(correct_entry.y)
    return x, y


def new_label(text: str, position: tuple[float, float]) -> turtle.Turtle:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(position)
    t.write(text, font=("Arial", 10, "normal"), align='center')
    return t


def play() -> bool:
    global correct_answers
    global correct_states_names
    global correct_states_labels
    answer = get_state_name_input()
    if answer.lower() == 'exit':
        return False
    if answer in correct_states_names:
        print("This state has already been guessed.")
        return True
    checked_answer = check_answer(answer)
    if type(checked_answer) is bool and checked_answer is False:
        print("Try again")
        return True
    else:
        correct_states_names.append(answer)
        state_coords = answer_to_xy(checked_answer)
        correct_answers += 1
        label = new_label(answer, state_coords)
        correct_states_labels.append(label)
        return True


while correct_answers < 50:
    if not play():
        missing_states = states_data[~states_data.state.isin(correct_states_names)]
        missing_states.to_csv('missing_states.csv')
        screen.bye()
        break

screen.exitonclick()
