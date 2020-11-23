# 5. function <fibonacci>
# take a number
# return fibonacci number less than argument

def fibonacci(number):
	# check input parameter
	try:
		num = int(number)		
	except ValueError:
		print ('value not valid')
		return
	if  num <= 0: 	# sequence start from 1
		print ('value out range')
		return
	
	# create fibonacci numbers list
	# default fibonacci list, 1st and 2nd elements
	fibo_list = [0,1]
	for n in range(2,num+1):
		# check number is less than argument
		if (fibo_list[n-1] + fibo_list[n-2]) <= num:
			fibo_list.append(fibo_list[n-1] + fibo_list[n-2])
		else:
			break
	# output result
	fibo_list.pop(0) # sequence start from 1
	return fibo_list

usr_num = input('enter a number greater 0: ')
print(fibonacci(usr_num))

res = fibonacci(usr_num)
print(res)



