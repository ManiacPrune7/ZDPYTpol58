"""
    Klasa reprezentujaca notatnik z notatkami
"""

from note import Note


class Notepad:

    def __init__(self):
        self.notes = []

    def add_new_note(self, memo: str, tags: list) -> Note:
        new_note = Note(memo, tags)
        self.notes.append(new_note)
        return new_note

    def modify_memo(self, note_id: int, memo: str):
        for curr_note in self.notes:
            if curr_note.id_ == note_id:
                curr_note.modify_memo(memo)
                break

    def modify_tags(self, note_id: int, tags: list):
        for curr_note in self.notes:
            if curr_note.id_ == note_id:
                curr_note.modify_tags(tags)
                break

    def search(self, filter_: str) -> list:
        found_notes = []

        for curr_note in self.notes:
            if curr_note.match(filter_):
                found_notes.append(curr_note)

        return found_notes


notepad = Notepad()
# print(notepad.notes)
notepad.add_new_note("o 18 pon silka", ["biceps", "bialko"])
# print(notepad.notes)
notepad.add_new_note("o 20 wt silka", ["nogi", "aminokwasy"])
# print(notepad.notes)

for note in notepad.notes:
    print(note.memo)
    notepad.modify_memo(note.id_, "o 16 pon silka")
    print(note.memo)

# for note in notepad.search("silka"):
#     print(note)
