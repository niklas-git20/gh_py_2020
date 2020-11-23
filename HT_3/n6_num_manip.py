# 6. function (??? probably acc. HT_3) <num_manipulation>
# take a number
# return result if number > 0 square, if number < 0 increase in 100, if number = 0 no changes
def num_manipulation(number):
	# check input parameter
	try:
		num = int(number)		
	except ValueError:
		print ('value not valid')
		return
	
	# check number
	if num > 0:
		num *= num
	elif num < 0:
		num +=100
	return num


usr_num = input('enter a number : ')
print(num_manipulation(usr_num))

res = num_manipulation(usr_num)
print(res)