class Dog:
    def __init__ (self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

Deatils = Dog("Buddy", 3, "Golden", "Golden Retriever")
deatils1 = Dog("Max", 5, "Black", "Labrador")
deatils2 = Dog("Bella", 2, "White", "Poodle")

print("Dog 1: Name:", Deatils.name, ", Age:", Deatils.age, ", Color:", Deatils.color, ", Breed:", Deatils.breed)
print("Dog 2: Name:", deatils1.name, ", Age:", deatils1.age, ", Color:", deatils1.color, ", Breed:", deatils1.breed)
print("Dog 3: Name:", deatils2.name, ", Age:", deatils2.age, ", Color:", deatils2.color, ", Breed:", deatils2.breed)