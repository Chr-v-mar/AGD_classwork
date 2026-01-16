class Dog:

    species = "Canis familiaris"
    
    def __init__(self, name, age):
       self.name = name
       self.age = age

   def __str__(self):
       return f'Name: {self.name}, age: {self.age}'

class Car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage
    
    def __str__(self):
        return f"The {self.colour} car has {self.mileage} miles"