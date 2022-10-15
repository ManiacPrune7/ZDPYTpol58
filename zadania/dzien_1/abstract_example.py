"""
    Przyklad zastosowania klasy abstrakcyjnej
"""

import abc


class Animal(abc.ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def eat(self):
        ...

    @abc.abstractmethod
    def move(self):
        ...

    def introduce_yourself(self):
        print(f"Siemanko, jestem {self.name}")


class Lion(Animal):

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("Mlasku mlask")

    def move(self):
        print("Biegu biegu")

    def sleep(self):
        print("zzzzzz")


class Shark(Animal):

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("omomomomo")

    def move(self):
        print("plywu plywu")

    def hunt(self):
        print("tutututututututuu")


class HungryAnimal:
    pass


# animal = Animal("Zwierz")
# print(animal)
lion = Lion("Leon")
print(lion)
shark = Shark("Szczena")
print(shark)
hungry = HungryAnimal()

animals = [lion, shark]

for animal in animals:
    animal.introduce_yourself()
