"""
    Prezentacja zalozen PEP8
"""

# importy: najpierw biblioteki wbudowane
import os
import random
import re
# potem importy bibliotek zainstalowanych pipem
# import requests
# na koncu importujemy nasze pakiety
# import census

# 4 spacje zamiast 1 taba

# operator w nowej linii


def add(a, b):
    return a\
           + b \
           + 1 \
           + 2 \
           + 3 \
           + 4 \
           + 5


def subtract(a, b):
    return a - b


class PrzykladowaKlasa:

    def jakas_metoda(self):
        pass  # jedna pusta linia odstepu miedzy metodami

    def druga_metoda(self):
        pass


napis = 'A wtedy ona powiedziala: "O NIE"'


class TestClass:

    TEST = 1

    def __init__(blablabla, test_name):
        blablabla.name = test_name
        blablabla._test_no = 0
        # blablabla.test_field_ = "field to be tested"

    @classmethod
    def test_class_method(byle_co_a_co):
        print(byle_co_a_co.TEST)


test = TestClass("Test numer 1")
print(test.name)
print(test._test_no)

result = 2 + 1 + 5*10/(4 + 22) * 1/6

return_ = 10
sum_ = 5
sum([1, 2, 3])

l = 10
O = 0
o = 0

add(l, l)
