# class figure

class Figure(object):
	color = 'white'

	def change_color(self, new_color):
		self.color = new_color
		return self.color
		


class Oval(Figure):
	def __init__(self, size=2):
		self.size = size


class Square(Figure):
	def __init__(self, size=2):
		self.size = size


fig1 = Figure()
ov1 = Oval()
sq1 = Square()


# get subclass attribute 'color'
print(fig1.color)
print(ov1.color)
print(sq1.color)

# change subclass attribute 'color'
fig1.change_color('pink')
ov1.change_color('blue')
sq1.change_color('red')

# get subclass attribute 'color'
print(fig1.color)
print(ov1.color)
print(sq1.color)

# get subclass attribute 'size'
print(ov1.size)
print(sq1.size)

