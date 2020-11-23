# 3. Write a script to sum of the first n positive integers

# sample input data
n = 3
num_list = 1,-5,4,-6,8,12,-12

num_pos_list = []
# for num in num_list:
# 	if num >= 0:
# 		num_pos_list.append(num)

# separate positive numbers
list(num_pos_list.append(pnum) for pnum in list(num_list) if pnum >= 0)

# check if n out list range
if n > len(num_pos_list): n = len(num_pos_list)

# get sum of n numbers
n_num_sum = 0
for num in range(0,n):
	n_num_sum +=num_pos_list[num]

# output results
print(n)
print(num_pos_list)
print(n_num_sum)

