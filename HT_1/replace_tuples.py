# 8. Write a script to replace last value of tuples in a list.
		# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
		# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# sample input list: 
# lst_1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
lst_1 = [(10, 20, 40, 90), (40, 50), (70, 80, 90, 87)]
rval = 100
lst_2 = []

for tup_elem in lst_1:
	# convert and changes of elements
	lst_elem = list(tup_elem)
	l_elem = len(lst_elem)
	lst_elem[l_elem - 1] = rval
	tup_elem = tuple(lst_elem)
	# fill converted list
	lst_2.append(tup_elem)

# output result
print (lst_2)

