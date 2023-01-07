from turtle import Turtle
from abc import abstractmethod, ABC


class GameFieldComponent(Turtle, ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def step(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass
