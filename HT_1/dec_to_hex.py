# 5. Write a script to convert decimal to hexadecimal
		# Sample decimal number: 30, 4
		# Expected output: 1e, 04

# sample input data
dec_list = [30, 4]
hex_list = []

for n in range(0,len(dec_list)):

#	hex_list.append('{:02x}'.format(dec_list[n]))
	hex_list.append('%02x' % (dec_list[n]))
print(*hex_list, sep = ', ')

# print as string
hex_str = ", ".join(hex_list)
print(hex_str)
