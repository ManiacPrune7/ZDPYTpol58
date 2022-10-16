"""
    Prezentacja zlamania i zastosowania zasady pojedynczej odpowiedzialnosci
"""

import database_conn


# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#         self.energy = 100
#         self.url = "postgres://username:password/db"
#
#     def give_voice(self):
#         print("WADGAGASFAG")
#
#     def send_data_to_db(self):
#         db = database_conn.connect(self.url)
#         db.save(self.name, self.energy)


class AnimalDB:

    def __init__(self):
        self.url = "postgres://username:password/db"

    def save_to_db(self, animal):
        db = database_conn.connect(self.url)
        db.save(animal.name, animal.energy)  # save to jest metoda w obiekcie db
                                             # nie mamy jej definicji


class Animal:

    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.db = AnimalDB()

    def give_voice(self):
        print("WADGAGASFAG")

    def send_data_to_db(self):
        self.db.save_to_db(self)


