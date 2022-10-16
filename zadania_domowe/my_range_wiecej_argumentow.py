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


class MyRange:
    pass
