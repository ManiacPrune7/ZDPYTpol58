from datetime import datetime
import re


class Note:
    note_id = 0

    def __init__(self, memo: str, tags: list):
        self.memo = memo
        self.tags = tags
        self._id = Note.note_id
        self.creation_date = datetime.today()
        Note.note_id += 1
        print(Note.note_id, self.note_id)

    def match(self, filter_: str) -> bool:
        if filter_.lower() in self.tags or re.match(filter_.lower(), self.memo):
            return True
        else:
            return False

note = Note('a', [1,2,3])
print(note.note_id)
