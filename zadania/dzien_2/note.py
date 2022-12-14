"""
    Implementacja przykladowa notatki jako klasy.
"""

import datetime


class Note:

    note_id = 0

    def __init__(self, memo: str, tags: list):
        self.id_ = Note.note_id
        Note.note_id += 1
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.today()

    def match(self, filter_: str) -> bool:
        if filter_ in self.memo or filter_ in self.tags:
            return True
        return False

    def modify_memo(self, memo):
        self.memo = memo

    def modify_tags(self, tags):
        self.tags = tags

    def __str__(self):
        return f"<OBJ> Note id: {self.id_}; " \
               f"memo: {self.memo}; tags: {self.tags} <OBJ>"


if __name__ == '__main__':
    note1 = Note("o 18 pon silka", ["biceps", "bialko"])
    print(note1.match("nogi"))
    print(note1.creation_date)
