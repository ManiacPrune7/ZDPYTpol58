"""
    Przyklad wzorca Command.
"""


from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        ...


class ConcreteCommand(Command):
    def execute(self):
        self.recv.action()


class Receiver:
    def action(self):
        print("Receiver Action")


class Invoker:
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


receiver = Receiver()
cmd = ConcreteCommand(receiver)
invoker = Invoker(cmd)
invoker.execute()
