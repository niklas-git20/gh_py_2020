# 14. Write a script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
		# Sample Dictionary ( n = 5) :
		# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# sample input list: 
n = 5

dic1 ={}
# fill dictionary by values
for n in range(1,n + 1):
	dic1[n] = n * n

# output result
print(dic1)