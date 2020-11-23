# 1. function <square>. 
# take 1 arg - side. 
# return 3 args in tuple (perimeter, areaa of square, diagonal)
def square(side):
	# check input parameter
	try:
		s = int(side)
	except ValueError:
		print ('value not valid')
		return
	#calculate perimeter	
	peri = 4 * s
	# calculate area
	area = s * s
	# calculate diagonal
	diag = round((2**0.5 * s), 3)
	# return results
	res_list = [peri, area, diag]
	return tuple(res_list)

# output results
print(square(input('enter side of square 1: ')))

res = square(input('enter side of square 2: '))
print(res)


