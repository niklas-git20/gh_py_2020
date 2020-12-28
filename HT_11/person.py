# class person

class Person:
	""" class Person

	Attributes
	--------------
	age: int
		age of person
	name: str
		name of person


	Methods
	--------------
	show_age
		show person age
	sshow_name
		show person name


	"""
	def __init__(self, age, name):
		"""

		Parameters
		--------------
		age: int
		age of person
		name: str
		name of person
		"""
		self.age = age
		self.name = name
		super().__init__()

	def show_age(self):
		"""method show_age

		Parameters
		--------------
		age: int
			age of person

		Returns
		--------------
		age: int
			age of person
		"""
		return f'person age {self.age}'
	def show_name(self):
		"""method show_name

		Parameters
		--------------
		name: str
			name of person

		Returns
		--------------
		name: str
			name of person
		"""
		return f'person name {self.name}'
	def show_all_info(self):
		"""method show_age

		Parameters
		--------------
		age: int
			age of person
		name: str
			name of person

		Returns
		--------------
		age: int
			age of person
		name: str
			name of person
		"""
		r_age = self.show_age()
		r_name = self.show_name()
		return r_age, r_name


# define method 'show_prof'
def show_prof(prof):
	"""method show_prof

		Parameters
		--------------
		prof: str
			profession of person

		Returns
		--------------
		prof: str
			profession of person
		"""
	return f'person profession {prof}'
		
# create class Person instance		
person1 = Person(20, 'john')
# add to instance of Person new attribute 'profession' with value 'driver'
setattr(person1, 'profession', 'driver')
print(person1.age)
print(person1.name)
print(person1.profession)
print(person1.show_age())
print(person1.show_name())
print(person1.show_all_info())
# add to instance of Person new method 'show_prof' 
setattr(person1, 'show_prof', show_prof)
print(person1.show_prof('manager'))


# create class Person instance
person2 = Person(24, 'jane')
# add to instance of Person new attribute 'profession' with value 'seller'
setattr(person2, 'profession', 'seller')
print(person2.age)
print(person2.name)
print(person2.profession)
print(person2.show_age())
print(person2.show_name())
print(person2.show_all_info())
# add to instance of Person new method 'show_prof' 
setattr(person2, 'show_prof', show_prof)
print(person2.show_prof('doctor'))