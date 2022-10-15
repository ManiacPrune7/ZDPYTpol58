from abc import ABC, abstractmethod


class Algorithm(ABC):

    def do_template_method(self):
        self.__do_absolutely_this()
        self.do_step_1()
        self.do_step_2()
        self.do_something()

    def __do_absolutely_this(self):
        """Protected operation. DON'T override me."""
        print('{}'.format(self.__class__.__name__))

    @abstractmethod
    def do_step_1(self):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def do_step_2(self):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @staticmethod
    def do_something():
        """Hook. You CAN override me, I'm NOT a placeholder."""
        print('do something')


class AlgorithmA(Algorithm):

    def do_step_1(self):
        print('do step 1 for Algorithm A')

    def do_step_2(self):
        print('do step 2 for Algorithm A')


class AlgorithmB(Algorithm):

    def do_step_1(self):
        print('do step 1 for Algorithm B')

    def do_step_2(self):
        print('do step 2 for Algorithm B')

    def do_something(self):
        print('do something else')


a = AlgorithmA()
a.do_template_method()

b = AlgorithmB()
b.do_template_method()
