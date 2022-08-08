from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import PlanetRepository
from project.creating import Creating
from project.planet.planet import Planet


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
       if self.astronaut_repository.find_by_name(name):
           return f"{name} is already added."
       astronaut = Creating.create_astronaut(name, astronaut_type)
       self.astronaut_repository.add(astronaut)
       return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        planet.items.append(items.split(", "))
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        return self.astronaut_repository.retire(name)

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):
        pass

    def report(self):
        pass
