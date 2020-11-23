# 1 .Write a script which accepts a sequence of comma-separated numbers from user 
# and generate a list and a tuple with those numbers
		# Sample data : 1, 5, 7, 23
		# Output :
		# List : [‘1', ' 5', ' 7', ' 23']
		# Tuple : (‘1', ' 5', ' 7', ' 23')

# sample data sequence from input
# num_seq = map(str, input().split(', '))
# num_list = list(num_seq)
# num_tup = tuple(num_list)

# sample input data sequence 1, 5, 7, 23
num_seq = 1, 5, 7, 23


# create tuple from list
num_tup = num_seq
# create list from sequence
num_list = list(num_tup)

# output results
print(num_list)
print(num_tup)

