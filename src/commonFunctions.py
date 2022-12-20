import random


def print_warning(warning_text: str, caption='Warning') -> None:
    print(f"\033[38;5;208m\033[1m\033[48;5;238m{caption}:\033[0m\033[38;5;220m {warning_text} \033[0m")


def print_info(info_text: str, caption='Information') -> None:
    print(f"\033[38;5;220m\033[48;5;238m{caption}:\033[0m\033[38;5;189m {info_text} \033[0m")


def reset_screen(page_header: str) -> None:
    print("\033[H\033[J\033[38;5;27m ")
    print(page_header)
    print("\033[0m")


def get_valid_response(question: str, possible_answers, case_sensitive=False) -> str:
    list_entry = "\t\t- "
    print(f"\033[38;5;123m\033[1m{question}\n\033[0m\033[1m\tPossible choice:")
    for a in possible_answers:
        print(list_entry + a)
    print(f"\033[0mAnswer is {'' if case_sensitive else 'not '}case sensitive.")
    while True:
        response_string = input("Your answer: ")
        if case_sensitive:
            for possible_answer in possible_answers:
                if response_string == possible_answer:
                    return possible_answer
        else:
            response_string = response_string.lower()
            for possible_answer in possible_answers:
                if response_string == possible_answer.lower():
                    return possible_answer
        print_info("Enter a valid response from the list.", "Incorrect input")


def get_AB_response(prompt: str) -> str:
    while True:
        response = input(prompt)
        if response.lower() == "a":
            return "A"
        elif response.lower() == "b":
            return "B"
        else:
            print_info("Enter 'A' or 'B'.", "Incorrect input")


def get_float_input(prompt: str) -> float:
    while True:
        x = input(prompt)
        try:
            x = float(x)
        except ValueError:
            print_warning("Please, provide a valid number.")
            continue
        return x


def get_int_input(prompt: str) -> float:
    while True:
        x = input(prompt)
        try:
            x = int(x)
        except ValueError:
            print_warning("Please, provide a valid integer number.")
            continue
        return x


class UniqueDrawFromList:
    def __init__(self, initial_list: list):
        self._list = initial_list.copy()
        self._initial_list_backup_ref = initial_list

    def draw(self) -> object:
        list_size = len(self._list)
        if list_size == 0:
            return False
        choice = random.randint(0, list_size - 1)
        element = self._list.pop(choice)
        return element

    def reset(self):
        self._list = self._initial_list_backup_ref.copy()
