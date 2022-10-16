"""
    Prezentacja zasady otwarte-zamkniete
"""

import abc


# PIERWSZY ETAP
# class Drawer:
#
#     def __init__(self, shape):
#         self.shape = shape
#
#     def draw(self):
#         if self.shape == 'circle':
#             print("rysuje kolo...")
#         elif self.shape == 'square':
#             print("rysuje kwadrat")

# DRUGI ETAP
# class Drawer:
#
#     def __init__(self, shape):
#         self.shape = shape
#
#     def draw(self):
#         if self.shape == 'circle':
#             print("rysuje kolo...")
#         elif self.shape == 'square':
#             print("rysuje kwadrat")
#         elif self.shape == 'rectangle':
#             print("rysuje prostokat")

# ETAP TRZECI

class Drawer(abc.ABC):

    @abc.abstractmethod
    def draw(self):
        ...


class CircleDrawer(Drawer):

    def draw(self):
        print("rysuje kolo...")


class SquareDrawer(Drawer):

    def draw(self):
        print("rysuje kwadrat...")


class RectangleDrawer(Drawer):

    def draw(self):
        print("rysuje prostokat...")
