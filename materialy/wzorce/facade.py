"""
    Przyklad fasady na podstawie organizacji wesela.
"""


class Hotelier:
    def book_hotel(self):
        pass


class Florist:
    def set_flower_requirements(self):
        pass


class Caterer:
    def set_cuisine(self):
        pass


class Musician:
    def set_music_type(self):
        pass


class EventManager:

    def __init__(self):
        print("Event Manager:: Let me talk to the folks...")
        self.hotelier = Hotelier()
        self.florist = Florist()
        self.caterer = Caterer()
        self.musician = Musician()

    def arrange(self):
        self.hotelier.book_hotel()
        self.florist.set_flower_requirements()
        self.caterer.set_cuisine()
        self.musician.set_music_type()


ev_manager = EventManager()
ev_manager.arrange()
