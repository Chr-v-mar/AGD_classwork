

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


def __str__(self):
    return f'Name: {self.name}, age: {self.age}'

def speaks(self, sound):
    return f'{self.name} says {sound}'

class Dachshund(Dog):
    def speaks(self, sound = "Arf! Arf!"):
        return super().speak(sound)


rufus = Dachshund('Rufus', 8)
fido = Dog('Fido', 6)
tdrt = Dog('ThreeDimensionalRotatingTorus', 7)

class Car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage

    def __str__(self):
        return f"The {self.colour} car has {self.mileage} miles"
