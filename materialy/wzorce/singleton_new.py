"""
    Singleton z uzyciem metody __new__.
"""


class Singleton:

    class __Singleton:
        def __init__(self):
            self.val = None

        def __str__(self):
            return "-----" + repr(self) + self.val + "-----"

    __instance = None

    def __new__(cls):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton.__Singleton()
        return Singleton.__instance


x = Singleton()
x.val = 'test01'
print(x)
y = Singleton()
print(y)
x.val = 'test02'
print(y)

