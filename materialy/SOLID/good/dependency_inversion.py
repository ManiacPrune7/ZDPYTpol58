"""
    Modul niespelniajacy zasady odwrotnej zaleznosci.
    Klasa nie zalezy od abstrakcji!
"""

import abc


class Sender(abc.ABC):

    @abc.abstractmethod
    def send(self, message: str):
        ...


class Task:

    def __init__(self, sender: Sender):
        self.sender = sender

    def process(self) -> None:
        # some processing things...
        self.sender.send('some nice message')


class EmailSender(Sender):
    def send(self, message) -> None:
        # send email
        print(f'Sending email with message:')


class SmsSender(Sender):
    def send(self, message: str) -> None:
        # send sms
        print(f'Sending sms with message: {message}')


sms = SmsSender()
email = EmailSender()
task = Task(email)
