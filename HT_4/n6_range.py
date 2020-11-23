# 6. function <range>
def func_range(*args):
	# get parameters
	start, stop, step = 0, 0, 1
	if len(args) == 1:
		start, stop, step = 0, args[0], 1
	elif len(args) == 2:
		start, stop, step = args[0], args[1], 1
	elif len(args) == 3:
		start, stop, step = args[0], args[1], args[2]
	else:
		return
	if step == 0:
		raise ValueError
	# positive step r[i] = start + step*i where i >= 0 and r[i] < stop
	if stop > start and step > 0:
		i = start
		while i < stop:
			yield i
			i += step
		# negative step r[i] = start + step*i, but the constraints are i >= 0 and r[i] > stop.
	if stop < start and step < 0:
		i = start
		while i > stop:
			yield i
			i += step	
		
# b,e,s =  map(int, input('enter commaseparated start, stop, step: ').split(','))
# print(b,e,*s)

# sample positive
o = 'omitted'
print('test cases', '\n', '-' * 20)
e = 10 
print(f'start = {o}, stop = {e}, step = {o}', '\n', list(func_range(e)))
b, e = 100, 110 
print(f'start = {b}, stop = {e}, step = {o}', '\n', list(func_range(b,e)))
b,e,s = 1000, 1100, 10 
print(f'start = {b}, stop = {e}, step = {s}', '\n', list(func_range(b,e,s)))
b, e = -110, -100
print(f'start = {b}, stop = {e}, step = {o}', '\n', list(func_range(b,e)))
b,e,s = -1000, -1100, -10 
print(f'start = {b}, stop = {e}, step = {s}', '\n', list(func_range(b,e,s)))
# sample none
e = -100 
print(f'start = {o}, stop = {e}, step = {o}', '\n', list(func_range(e)))
b, e = 100, 0 
print(f'start = {b}, stop = {e}, step = {o}', '\n', list(func_range(e)))
b,e,s = -1100, -1000, -10 
print(f'start = {b}, stop = {e}, step = {s}', '\n', list(func_range(b,e,s)))
# sample error
b,e,s = 0, 1000, 0 
print(f'start = {b}, stop = {e}, step = {s}', '\n', list(func_range(b,e,s)))

