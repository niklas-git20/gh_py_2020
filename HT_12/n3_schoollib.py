# school library structure
# class inheritance: school name - level - subject

class SchoolLib(object):
	school_name = '31'
	def show(self):
		print ('school number: ', self.school_name)

class Level(SchoolLib):
	def __init__(self, school_number, level):
		SchoolLib.__init__(self)
		self.level = level
	def show(self):
		SchoolLib.show(self)
		print ('school level: ', self.level)

class Subject(Level):
	def __init__(self, level, subject):
		super(Subject, self).__init__(self, level)
		self.subject = subject
	def show(self):
		super().show()	
		print ('subject: ', self.subject)
		

math_5 = Subject('5', 'math')
math_5.show()

bio_6 = Subject('6', 'biology')
bio_6.show()

chem_7 = Subject('7', 'chemistry')
chem_7.show()
