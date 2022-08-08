from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class Creating:
    astronaut_type = {"Biologist": Biologist,
                      "Geodesist": Geodesist,
                      "Meteorologist": Meteorologist}

    def create_astronaut(self, name, a_type):
        if a_type in self.astronaut_type:
            self.astronaut_type[a_type](name)
        else:
            raise Exception("Astronaut type is not valid!")
