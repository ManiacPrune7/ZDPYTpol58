"""
    Prezentacja dzialania wzorca builder na przykladzie tworzenia pizzy.
"""

import abc


class Cook:
    """
    Director - zarządza tworzeniem obiektu
    """
    def __init__(self):
        self.recipe = None

    def prepare(self, recipe):
        self.recipe = recipe
        self.recipe.prepare_dough()
        self.recipe.add_extras()
        self.recipe.bake()


class PizzaBuilder(abc.ABC):
    """
    Builder - abstrakcyjny interfejs do tworzenia docelowych obiektów
    """
    def __init__(self):
        self.pizza = Pizza()

    @abc.abstractmethod
    def prepare_dough(self): pass

    @abc.abstractmethod
    def add_extras(self): pass

    @abc.abstractmethod
    def bake(self): pass


class MargeritaBuilder(PizzaBuilder):
    """
    ConcreteBuilder - konkretny builder tworzący i łączący składniki tworzonego obiektu
    """
    def prepare_dough(self):
        # robimy margerite
        pass

    def add_extras(self):
        # robimy margerite
        pass

    def bake(self):
        # robimy margerite
        pass


class PepperoniBuilder(PizzaBuilder):

    def prepare_dough(self):
        # robimy pepperoni
        pass

    def add_extras(self):
        # robimy pepperoni
        pass

    def bake(self):
        # robimy pepperoni
        pass


class Pizza:
    """
    generowany obiekt złożony
    """
    pass


def main():
    cook = Cook()
    # wybieramy buildera
    baking = PepperoniBuilder()
    cook.prepare(baking)
    pizza = baking.pizza
