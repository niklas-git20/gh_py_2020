# 4. Write a script to concatenate N strings

# sample input data
n, n2, n3 = 32, 32, 32
str_seq = '1','-5','4','-6','8','12','-12'
str_seq2 = 1, -5, 4, -6, 8, 12, -12
str_seq3 = input().split(', ')

print('type of str_seq ', type(str_seq), 'type of element str_seq ', type(str_seq[0]))
print('type of str_seq2 ', type(str_seq2), 'type of element str_seq2 ', type(str_seq2[0]))
print('type of str_seq3 ', type(str_seq3), 'type of element str_seq3 ', type(str_seq3[0]))

n_str_conc, n_str_conc2, n_str_conc3, = '', '', ''

# check if n out list range
if n > len(str_seq): n = len(str_seq)
if n2 > len(str_seq2): n2 = len(str_seq2)
if n3 > len(str_seq3): n3 = len(str_seq3)

# get concatenation of strings
for n in range(0,n):
	n_str_conc += str_seq[n]
# get concatenation of strings
for n2 in range(0,n2):
	n_str_conc2 += str(str_seq2[n2])
# get concatenation of strings
for n3 in range(0,n3):
	n_str_conc3 += (str_seq3[n3])	

# output results
print(n)
# print(str_seq)
print(n_str_conc)
print(n_str_conc2)
print(n_str_conc3)