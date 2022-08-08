from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 70)

    def unit_for_breath(self):
        return 5