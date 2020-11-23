# 9. Write a script to remove an empty tuple(s) from a list of tuples
		# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
		# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# sample input list: 
lst_1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# check elements if not empty
lst_1 = list(tup_elem for tup_elem in lst_1 if tup_elem != ())

# output result
print (lst_1)