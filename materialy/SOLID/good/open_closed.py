"""
    Modul napisany w sposob zmuszajacy do modyfikacji
    kodu, zamiast jego rozszerzenia.
"""

import abc


class ProfessionTax:
    ARTIST = 0.25
    LAWYER = 0.34
    TEACHER = 0.15
    PROGRAMMER = 0.0


class TaxPayer(abc.ABC):

    def __init__(self, salary):
        self.salary = salary

    @abc.abstractmethod
    def calculate_tax(self):
        ...


class ArtistTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * ProfessionTax.ARTIST


class LawyerTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * ProfessionTax.LAWYER


class TeacherTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * ProfessionTax.TEACHER


class ProgrammerTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * ProfessionTax.PROGRAMMER
