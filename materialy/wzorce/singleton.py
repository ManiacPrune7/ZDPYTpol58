"""
	Najprostsza implementacja Singletona w Pythonie.
"""


class Singleton:
	
	__instance = None
	
	def __init__(self):
		if Singleton.__instance is None:
			print("__init__ called")
			self.to_be_kept = 1
		else:
			print(f"Instance already created: {self.get_instance()}")
			
	@classmethod
	def get_instance(cls):
		if cls.__instance is None:
			cls.__instance = Singleton()
		return cls.__instance


# s = Singleton()
# ss = Singleton()
s2 = Singleton.get_instance()
s1 = Singleton.get_instance()
print(s2.to_be_kept)
s2.to_be_kept = 5
print(s1.to_be_kept)
print(id(s1), id(s2))
