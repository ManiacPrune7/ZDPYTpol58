"""
    Prezentacja zasady liskov
"""

"""
    Modul nie spelniajacy zasady Liskov:
    klasy potomnej nie da sie podstawic w kazdym przypadku za klase bazowa!
"""

import abc


class ReadableFile(abc.ABC):

    @abc.abstractmethod
    def read(self):
        ...


class WritableFile(abc.ABC):

    @abc.abstractmethod
    def write(self, input_text):
        ...


class NormalFile(ReadableFile, WritableFile):

    # MRO - Method resolution order
    # def __init__(self):
    #     super(ReadableFile, self).__init__()
    #     super(WritableFile, self).__init__()

    def read(self):
        # read file implementation
        print('Reading from regular file')

    def write(self, input_text):
        # write file implementation
        print('Writing to regular file')


class ReadonlyFile(ReadableFile):

    def read(self):
        # read readonly file implementation
        print('Reading from readonly file')


normal_file = NormalFile()
readonly_file = ReadonlyFile()


def make_file_operations(file: NormalFile, input_text):
    file.write(input_text)
    # some processing stuff
    file.read()


make_file_operations(normal_file, 'tekst')
make_file_operations(readonly_file, 'tekst')
