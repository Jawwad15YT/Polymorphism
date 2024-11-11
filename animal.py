class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound():
        print("Woof Woof")

class Cat(Animal):
    def sound():
        print("Meow Meow")

def animal_sound(animal):
    animal.sound()

Tom = Cat

animal_sound(Tom)