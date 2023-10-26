class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, Species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == 'fishes':
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == 'birds':
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo = input()
zoo = Zoo(zoo)
number = int(input())

for animal in range(number):
    current_animal = input().split()
    species, name = current_animal
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
