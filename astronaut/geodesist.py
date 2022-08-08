from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 50)

    def unit_for_breath(self):
        return 10