class Pet:
    def __init__(self, name, species, age, adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted

    def display(self):
        status = "adopted" if self.adopted else "not adopted"
        print(f"{self.name} is a {self.age}-year-old {self.species} and is currently {status}.")

