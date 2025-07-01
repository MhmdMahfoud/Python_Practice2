class Pet:
    def __init__(self, name, species, age, adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted

    def display(self):
        status = "adopted" if self.adopted else "not adopted"
        print(f"{self.name} is a {self.age}-year-old {self.species} and is currently {status}.")
    
    def mark_adopted(self):
        self.adopted = True
 
    def birthday(self):
        self.age += 1
pet1 = Pet("Buddy", "Dog", 5)
pet2 = Pet("Whiskers", "Cat", 2)
pet3 = Pet("Coco", "Parrot", 1)

pet1.display()
pet1.mark_adopted()
pet1.display()
print("*****************")
pet2.display()
pet2.birthday()
pet2.display()
print("*****************"
)
pet3.display()
pet3.birthday()
pet3.mark_adopted()
pet3.display()
