from project.astronaut.validator import Validator


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_the_string_is_empty(value, 1)
        self.__name = value
