from random import choice, randint
from turtle import Turtle


class CarManager:
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    MOVE_DISTANCE = 4
    MOVE_INCREMENT = 4

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.color(choice(CarManager.COLORS))
        random_y = randint(-250, 250)
        new_car.setheading(180)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(CarManager.MOVE_DISTANCE)
            if car.xcor() < -350:
                self.all_cars.remove(car)
                car.hideturtle()
                del car

    def increase_speed(self):
        CarManager.MOVE_DISTANCE += CarManager.MOVE_INCREMENT
