import random


class Aquarium:
    def __init__(self, initial_carbon_dioxide_level, initial_oxygen_level):
        self.animals: [Animal] = []
        self.plants: [Plant] = []
        self.carbon_dioxide = initial_carbon_dioxide_level
        self.oxygen = initial_oxygen_level

    def create_fish(self):
        self.animals.append(Fish())

    def create_plant(self):
        self.plants.append(Plant())

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def remove_plant(self, plant):
        self.plants.remove(plant)

    def report_status(self):
        print(f"Aquarium status - Animals: {self.animals}, Plants: {self.plants}")

    def auto_cycle(self, days):
        for minute in range(24 * 60 * days):
            for animal in self.animals:
                ret = animal.respire(self)
                if ret == 0:
                    print(f"Animal killed due to oxygen level being too low at minute {minute}")
                    self.report_status()
            for plant in self.plants:
                ret = plant.respire(self)
                if ret == 0:
                    print(f"Plant killed due to co2 level being too low at minute {minute}")
                    self.report_status()

class Animal:
    def __init__(self, size):
        self.size = size
        self.oxygen_required = self.size

    def respire(self, aquarium: Aquarium):
        # Check if oxygen level is high enough for this animal to respire
        if aquarium.oxygen >= self.oxygen_required:
            aquarium.oxygen -= self.oxygen_required
            aquarium.carbon_dioxide += self.oxygen_required
        # If oxygen level is not high enough, remove this animal from the aquarium
        else:
            aquarium.remove_animal(self)
            return 0

    def __repr__(self):
        return f"Animal - size: {self.size}"

class Fish(Animal):
    def __init__(self):
        size = random.randrange(1, 5)
        super().__init__(size)
        self.oxygen_required = 3 * size

    def __str__(self):
        return f"Fish - size: {self.size}"

    def __repr__(self):
        return str(self)

class Plant():
    def __init__(self):
        self.size = random.randrange(1, 5)
        self.co2_required = self.size * 3

    def respire(self, aquarium: Aquarium):
        # Check if oxygen level is high enough for this animal to respire
        if aquarium.carbon_dioxide >= self.co2_required:
            aquarium.oxygen += self.co2_required
            aquarium.carbon_dioxide -= self.co2_required
        # If oxygen level is not high enough, remove this animal from the aquarium
        else:
            aquarium.remove_plant(self)
            return 0

    def __str__(self):
        return f"Plant - size: {self.size}"

    def __repr__(self):
        return str(self)


def main():
    aquarium = Aquarium(initial_carbon_dioxide_level=18, initial_oxygen_level=30)
    aquarium.create_fish()
    aquarium.create_plant()
    aquarium.report_status()
    aquarium.auto_cycle(days=3)
    aquarium.report_status()

if __name__ == "__main__":
    main()