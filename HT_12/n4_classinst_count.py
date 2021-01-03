# calculation a number of class instances
class SomeClass(object):
	count = 0

	def __init__(self):
		SomeClass.count += 1

	def __del__(self):
		SomeClass.count -= 1



cls1 = SomeClass()
print(cls1.count)

cls2 = SomeClass()
print(cls2.count)

cls3 = SomeClass()
print(cls3.count)

cls4 = SomeClass()
print(cls4.count)

cls5 = SomeClass()
print(cls5.count)

cls5.__del__()
print(cls5.count)
print(cls4.count)

