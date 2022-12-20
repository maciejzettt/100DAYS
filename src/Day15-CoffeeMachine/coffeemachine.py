import decimal

from src.commonFunctions import print_info, print_warning, get_int_input


class CoffeeMachine:

    def __init__(self, configuration):
        self.resources = configuration.resources
        self.menu = configuration.MENU
        self.money = 0
        decimal.getcontext().prec = 4

    def ask_which_coffee(self, question="\nWhat would you like?", case_sensitive=False) -> str:
        possible_answers = [e for e in self.menu.keys()]
        list_entry = "\t\t- "
        print(f"\033[38;5;123m\033[1m{question}\n\033[0m\033[1m\tPossible choice:")
        for a in possible_answers:
            print(list_entry + a)
        print(f"\033[0mAnswer is {'' if case_sensitive else 'not '}case sensitive.")
        while True:
            response_string = input("Your answer: ")
            if response_string == "report":
                return "report"
            if response_string == "off":
                return "off"
            response_string = response_string.lower()
            for possible_answer in possible_answers:
                if response_string == possible_answer.lower():
                    return possible_answer
            print_info("Enter a valid response from the list.", "Incorrect input")

    def printReport(self):
        print_warning("", "Resources report")
        for resource in self.resources:
            print_info(str(self.resources[resource]), resource)
        print_info(str(self.money), "Money")

    def turnOff(self):
        print_info("Turning off.")

    def prepare_coffee(self, coffee_type):
        if self.are_sufficient_resources(coffee_type):
            coffee_cost = self.menu[coffee_type]['cost']
            print(f"\nYour {coffee_type} will cost ${coffee_cost}. Insert coins:")
            provided_money = self.ask_for_money()
            if provided_money >= coffee_cost:
                self.settle_money(provided_money, coffee_cost)
                self.brew_coffee(coffee_type)
            else:
                print_warning(f"Insufficient amount of money: ${str(provided_money)} while {coffee_type} costs ${coffee_cost}")
        else:
            print_warning(f"Insufficient resources for {coffee_type}")

    def are_sufficient_resources(self, coffee_type) -> bool:
        try:
            for component in self.menu[coffee_type]["ingredients"]:
                if self.menu[coffee_type]["ingredients"][component] > self.resources[component]:
                    return False
            return True
        except KeyError:
            return False

    def brew_coffee(self, coffee_type):
        self.use_resources(coffee_type)
        print(f"Here is your {coffee_type}. Enjoy!")

    def use_resources(self, coffee_type) -> None:
        for component in self.menu[coffee_type]["ingredients"]:
            self.resources[component] -= self.menu[coffee_type]["ingredients"][component]

    def ask_for_money(self) -> decimal.Decimal():
        pennies = get_int_input("How many pennies do you want to use?: ")
        PENNIE_VALUE = decimal.Decimal("0.01")
        nickels = get_int_input("How many nickels do you want to use?: ")
        NICKEL_VALUE = decimal.Decimal("0.05")
        dimes = get_int_input("How many dimes do you want to use?: ")
        DIME_VALUE = decimal.Decimal("0.1")
        quarters = get_int_input("How many quarters do you want to use?: ")
        QUARTER_VALUE = decimal.Decimal("0.25")
        amount = pennies * PENNIE_VALUE + nickels * NICKEL_VALUE + dimes * DIME_VALUE + quarters * QUARTER_VALUE
        return amount

    def settle_money(self, provided, expected) -> None:
        self.money += expected
        change = provided - decimal.Decimal(expected)
        if change > 0:
            print(f"Here is your change of ${str(change)}.")
