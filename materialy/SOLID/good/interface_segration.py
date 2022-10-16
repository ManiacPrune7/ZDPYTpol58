"""
    Zbyt duza klasa abstrakcyjna Animal.
"""

import abc


class Animal(abc.ABC):

    @abc.abstractmethod
    def eat(self):
        ...

    @abc.abstractmethod
    def give_a_voice(self):
        ...


class RunnableAnimal(Animal):

    @abc.abstractmethod
    def run(self):
        ...


class FlyableAnimal(Animal):

    @abc.abstractmethod
    def fly(self):
        ...


class SwimmableAnimal(Animal):

    @abc.abstractmethod
    def swim(self):
        ...


class Lion(RunnableAnimal):

    def eat(self):
        ...

    def run(self):
        ...

    def give_a_voice(self):
        ...
