# 3. Print season if month number in related range

month_num = int(input('enter a month number 1-12: '))

if 1 <= month_num <= 2 or month_num == 12:
	print('winter')
elif 3 <= month_num <= 5:
	print('spring')
elif 6 <= month_num <= 8:
	print('summer')
elif 9 <= month_num <= 11:
	print('autunumn')
else:
	pass



