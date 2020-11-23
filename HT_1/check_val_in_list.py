# 6. Write a script to check whether a specified value is contained in a group of values
		# Test Data :
		# 3 -> [1, 5, 8, 3] : True
		# -1 -> (1, 5, 8, 3) : False

# sample input data
lst_1 = [1,5,8,3]
chk_1 = 3

lst_2 = [1,5,8,3]
chk_2 = -1

print(chk_1 in lst_1)
print(chk_2 in lst_2)