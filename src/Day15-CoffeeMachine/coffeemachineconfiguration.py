class CoffeeMachineConfiguration:

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 1000,
        "milk": 350,
        "coffee": 150,
    }

    coins = {
        "Penny": 0.01,
        "Nickel": 0.05,
        "Dime": 0.1,
        "Quarter": 0.25,
    }
