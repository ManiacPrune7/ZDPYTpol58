"""
    Przyklad wzorca Command.
"""


from abc import ABC, abstractmethod


class Receiver:
    def action(self):
        print("Receiver Action")


class Command(ABC):
    def __init__(self, recv: Receiver):
        self.recv = recv

    @abstractmethod
    def execute(self):
        ...


class ConcreteCommand(Command):
    def execute(self):
        self.recv.action()


class Invoker:
    def __init__(self, cmd: Command):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


receiver = Receiver()
cmd = ConcreteCommand(receiver)
invoker = Invoker(cmd)
invoker.execute()
