# 4. Create 3 functions with simple operation
# create 4th function wich contains all 3 others
x, y = map(int, input('enter spaced x and y: ').split()) 

def func1(a,b):
	return (a + b)

def func2(a,b):
	return (a - b)

def func3(a,b):
	return (a * b)

def func4(a,b):
	e = func1(a,b)
	f = func2(a,b)
	g = func3(a,b)
	print('\n', e+1, '\n', f+2, '\n' ,g+3)

func4(x,y)

