"""
    Przyklad adaptera na podstawie gniazdek europejskich i amerykanskich.
"""


class EuropeanSocketInterface:
    def get_voltage(self): pass

    def get_live(self): pass

    def get_neutral(self): pass

    def get_earth(self): pass


# Adaptee
class Socket(EuropeanSocketInterface):
    def get_voltage(self):
        return 230

    def get_live(self):
        return 1

    def get_neutral(self):
        return -1

    def get_earth(self):
        return 0


# Target interface
class USASocketInterface:
    def get_voltage(self): pass

    def get_live(self): pass

    def get_neutral(self): pass


# The Adapter
class Adapter(USASocketInterface):

    def __init__(self, socket):
        self.__socket = socket

    def get_voltage(self):
        return 110

    def get_live(self):
        return self.__socket.live()

    def get_neutral(self):
        return self.__socket.neutral()


# Client
class ElectricKettle:

    def __init__(self, adapter):
        self.__power = adapter

    def boil(self):
        if self.__power.get_voltage() > 110:
            print("Kettle on fire!")
        else:
            if self.__power.get_live() == 1 \
                    and self.__power.get_neutral() == -1:
                print("Coffee time!")
            else:
                print("No power.")


def main():
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    # Make coffee
    kettle.boil()


if __name__ == "__main__":
    main()
