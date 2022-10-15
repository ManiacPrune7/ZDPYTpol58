"""
    Przyklad strategii.
"""


class Zoo:

    def __init__(self, animal):
        self.animal = animal

    def make_animal_give_voice(self):
        self.animal.give_sound()


class Lion:

    def give_sound(self):
        print("ROOAAARRRR")


class Frog:

    def give_sound(self):
        print("uuueeeee")