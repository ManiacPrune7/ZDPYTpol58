"""
    Klasa Circle z dwiema odpowiedzialnosciami - NAPRAWIONE
"""

import math


class CircleDrawer:

    # def __init__(self):
    #     pass

    def draw(self):
        pass


class Circle:
    def __init__(self, radius=0, color="red"):
        self.radius = radius
        self.color = color
        self.drawer = CircleDrawer()

    def draw(self):
        """Draws a circle"""
        self.drawer.draw()

    def get_area(self):
        """Counts the area"""
        return math.pi * self.radius**2
