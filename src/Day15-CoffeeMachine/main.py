from coffeemachineconfiguration import CoffeeMachineConfiguration
from coffeemachine import CoffeeMachine


def main() -> None:
    configuration = CoffeeMachineConfiguration()
    coffee_machine = CoffeeMachine(configuration)
    while True:
        user_choice = coffee_machine.ask_which_coffee()
        if user_choice == "report":
            coffee_machine.printReport()
        elif user_choice == "off":
            coffee_machine.turnOff()
            return
        else:
            coffee_machine.prepare_coffee(user_choice)


main()
