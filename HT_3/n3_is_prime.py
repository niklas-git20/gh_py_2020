# 3. function <is_prime>
# take a number in range 0..1000
# return True if number is prime, False if not

def is_prime(number):
	# check input parameter
	try:
		num = int(number)		
	except ValueError:
		print ('value not valid')
		return
	if  num < 0 or num > 1000:
		print ('value out range')
		return
	
	is_prime = False
	# number check for division by 1 and itself
	# used construction for..else
	if num > 1:
		for n in range(2,num):
			if num % n == 0:
				is_prime = False
				break
		else:
			is_prime = True
	else:
		is_prime = False
	return is_prime

usr_num = input('enter a number in range 0...1000: ')
print(is_prime(usr_num))

res = is_prime(usr_num)
print(res)



