# 2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.
# sample input data
		# Test Data :
		# color_list_1 = set(["White", "Black", "Red"])
		# color_list_2 = set(["Red", "Green"])
		# Expected Output :
		# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# get difference list
color_list_3 = color_list_1 - color_list_2

# output result
print(color_list_3)
