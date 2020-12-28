# class simple calculator

class Calc:
	"""simple calculator class

	Attributes
	--------------
	last_res: int
		stored result of last operation

	Methods
	--------------
	add
		add two values x and y
	sub
		substract two values y from x
	mul
		multiply two values x and y
	div
		divide two values x by y


	"""
	def __init__(self):
		"""

		Parameters
		--------------
		last_res: int
			stored result of last operation
		"""
		self.last_res = 0
	def sum(self,x,y):
		"""method add

		Parameters
		--------------
		x, y: int
			values for calculation

		Returns
		--------------
		res: int
			result of adding x and y
		"""
		res = x + y
		self.last_res = res
		return res	
	def sub(self,x,y):
		"""method substraction

		Parameters
		--------------
		x, y: int
			values for calculation

		Returns
		--------------
		res: int
			result of substraction y from x
		"""
		res = x - y
		self.last_res = res
		return res
	def mul(self,x,y):
		"""method multiplication
		Parameters
		--------------
		x, y: int
			values for calculation

		Returns
		--------------
		res: int
			result of multiplication x and y
		"""
		res = x * y
		self.last_res = res
		return res
	def div(self,x,y):
		"""method division
		Parameters
		--------------
		x, y: int
			values for calculation

		Returns
		--------------
		res: int
			result of division x by y
		"""
		res = int(x / y)
		self.last_res = res
		return res	



calc1 = Calc()
print(calc1.last_res)

res = calc1.sum(2,2)
print(res)
print(calc1.last_res)

res = calc1.sub(12,2)
print(res)
print(calc1.last_res)

res = calc1.mul(22,2)
print(res)
print(calc1.last_res)

res = calc1.div(62,2)
print(res)
print(calc1.last_res)

res = calc1.sum(calc1.last_res,3)
print(res)
print(calc1.last_res)


print(calc1.__doc__)
print(help(calc1))