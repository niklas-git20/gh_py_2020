# 7. Write a script to concatenate N strings

# sample input data
n = 3
str_list = ['1','-5','4','-6','8','12','-12']

n_str_conc = ''

# check if n out list range
if n > len(str_list): n = len(str_list)

# get concatenation of strings
for strg in range(0,n):
	n_str_conc += str_list[strg]

# output results
print(n)
print(str_list)
print(n_str_conc)