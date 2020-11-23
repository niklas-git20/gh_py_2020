# 4. function <is_prime_list>
# take a beginning and end of range 0..1000
# return list of prime numbers in range

def is_prime_list(range_beg, range_end):
	# check input parameter
	try:
		r_beg = int(range_beg)	
		r_end = int(range_end)	
	except ValueError:
		print ('values not valid')
		return
	
	# create prime numbers list
	# used construction for..else
	prime_list = []
	for num in range(r_beg,r_end):		
		if num > 1:
			for n in range(2,num):
				if num % n == 0:
					break
			else:
				prime_list.append(num)
	# output result
	return prime_list		

beg,end,*oth = input('enter hyphen separated start and end of interval: ').split('-')

print(is_prime_list(beg,end))

res = is_prime_list(beg,end)
print(res)