"""
    Napisz wlasna implementacje iteratora range.
    Na zajeciach napisalismy iterator MyRange, ktory przyjmowal jeden argument.
    range moze przyjmowac wiecej argumentow:
    - 2: range(5, 10) -> wygeneruje liste liczb od 5 do 9
    - 3: range(5, 10, 2) -> wygeneruje liste liczb od 5 do 9 skaczac co 2.

    Zaimplementuj JEDNA klase iteratora range obslugujaca 1, 2 lub 3 argumenty
    na podobnej zasadzie i dzialaniu jak prawdziwy range.

    Wskazowka1: konstruktor moze przyjmowac rozna ilosc argumentow (jeden, dwa lub trzy).
    Co trzeba zastosowac, aby mozna bylo podawac do funkcji rozna ilosc argumentow
    (nawet i nieskoczona ilosc)?

    Wskazowka2: wczesnej zmienialismy wartosc tylko zmiennej self.n (zwiekszalismy ja o 1).
    Teraz zgodnie z definicja niekoniecznie bedziemy zwiekszac self.n o 1 (moze o 2? o 3?).
    Potrzebna bedzie dodatkowy atrybut.
"""


class WrongNumberOfAttrs(Exception):
    pass


class MyRange:
    def __init__(self, *args):
        jump = 1
        start = 0
        if len(args) == 1:
            maximum = args[0]
        elif len(args) == 2:
            start = args[0]
            maximum = args[1]
        elif len(args) == 3:
            start = args[0]
            maximum = args[1]
            jump = args[2]
        else:
            raise WrongNumberOfAttrs(f"Number of args {len(args)} is wrong!")

        self.start = start
        self.max = maximum
        self.jump = jump

    def __iter__(self):
        return MyRangeIterator(self.start, self.max, self.jump)


class MyRangeIterator:
    def __init__(self, n, maximum, jump):
        self.max = maximum
        self.jump = jump
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.max > self.n:
            res = self.n
            self.n += self.jump
            return res
        else:
            raise StopIteration


my_range = MyRange(6, 18, 2)

for i in my_range:
    print(i)
