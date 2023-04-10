import random
from threading import Timer
from os import path

DIR = path.dirname(__file__)


def print_warning(warning_text: str, caption='Warning') -> None:
    print(f"\033[38;5;208m\033[1m\033[48;5;238m{caption}:\033[0m\033[38;5;220m {warning_text} \033[0m")


def print_info(info_text: str, caption='Information') -> None:
    print(f"\033[38;5;220m\033[48;5;238m{caption}:\033[0m\033[38;5;189m {info_text} \033[0m")


def reset_screen(page_header: str) -> None:
    print("\033[H\033[J\033[38;5;27m ")
    print(page_header)
    print("\033[0m")


def get_valid_response(question: str, possible_answers, case_sensitive=False) -> str:
    list_entry_beginning = "\t\t- "
    print(f"\033[38;5;123m\033[1m{question}\n\033[0m\033[1m\tPossible choice:")
    for a in possible_answers:
        print(list_entry_beginning + a)
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


def email_credentials() -> dict:
    with open(path.join(DIR, "email.pwd")) as pwd_f:
        email_srv = pwd_f.readline().strip()
        email_addr = pwd_f.readline().strip()
        email_pass = pwd_f.readline().strip()
    return {
        "server": email_srv,
        "user": email_addr,
        "password": email_pass
    }


class UniqueDrawFromList:
    def __init__(self, initial_list: list):
        self._list = initial_list.copy()
        self.__original_list_backup_ref = initial_list

    def draw(self) -> object:
        list_size = len(self._list)
        if list_size == 0:
            return False
        choice = random.randint(0, list_size - 1)
        element = self._list.pop(choice)
        return element

    def reset(self):
        self._list = self.__original_list_backup_ref.copy()


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

