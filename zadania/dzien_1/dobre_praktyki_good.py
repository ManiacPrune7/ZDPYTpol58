import math


class Calculator:
    def __init__(self):
        print("Calculator creation...")
        self._a = 0
        self.__b = 0
        self.result = None

    def add(self, x, y):
        self._a = x
        self.__b = y
        self.result = self._a + self.__b

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    def multiply_numbers(self):
        return self._a * self.__b

    @staticmethod
    def divide_two_numbers(number, number1):
        print('In a moment the method called DivideTwoNumbers will divide '
              'two numbers: number/number1, the result will be printed on '
              'a terminal, so you will have a chance to see it live')
        result = number/number1
        print(f"{result}")

    @staticmethod
    def do_hard_counting():
        return 5*3*(-2 + (4 + 5 / 8)) / 4+6

    @staticmethod
    def sqrt(number):
        return math.sqrt(number)

    @staticmethod
    def print_all_numbers(all_numbers):
        winning_number = 5

        for number in all_numbers:
            if number == winning_number:
                for i in range(3):
                    print(number)

    @staticmethod
    def divide_zero(num):
        try:
            return num/0
        except ZeroDivisionError:
            return num/0


class XYZ:
    def __init__(self):
        self.calculator = Calculator()

    @staticmethod
    def add_it(*args):
        return sum(args)

    def add(self, x, y):
        self.calculator.add(x, y)


Calculator.divide_zero(10)