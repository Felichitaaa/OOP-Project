from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 90)

    def unit_for_breath(self):
        return 15