from abc import ABC, abstractmethod

from project.astronaut.validator import Validator


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = [] #items

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_the_string_is_empty(value.strip(),1)
        self.__name = value

    def breathe(self):
        self.oxygen -= self.unit_for_breath()

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    @property
    @abstractmethod
    def unit_for_breath(self):
        pass