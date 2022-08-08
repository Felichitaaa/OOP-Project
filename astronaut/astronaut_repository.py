from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = [] #obj

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for a in self.astronauts:
            if a.name == name:
                return a
    def retire(self, name):
        if any(a.name == name for a in self.astronauts):
            self.astronauts.remove(self.find_by_name(name))
            return "Astronaut {astronaut_name} was retired!"
        else:
            raise Exception(f"Astronaut {name} doesn't exist!")