from abc import ABC, abstractmethod


class Section(ABC):
	@abstractmethod
	def describe(self):
		pass


class PersonalSection(Section):
	def describe(self):
		print("Personal Section")


class AlbumSection(Section):
	def describe(self):
		print("Album Section")


class CareerSection(Section):
	def describe(self):
		print("Career Section")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Profile(ABC):
	def __init__(self):
		self.sections = []
		self.create_profile()

	@abstractmethod
	def create_profile(self):
		...

	def add_section(self, section):
		self.sections.append(section)


class Facebook(Profile):
	def create_profile(self):
		self.add_section(PersonalSection())
		self.add_section(AlbumSection())


class LinkedIn(Profile):
	def create_profile(self):
		self.add_section(PersonalSection())
		self.add_section(CareerSection())
