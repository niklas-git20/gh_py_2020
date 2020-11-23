# 11. Write a script to remove duplicates from Dictionary

# sample input data
dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 20, 8: 40, 9: 60}

tmp_key_list = []
tmp_val_list = []
del_key_list = []
dic2 = dic1

# check dictionary for duplicates
# direct order
# for key, val in dic1.items():
# reverswed order
for key, val in reversed(dic1.items()):
	if val not in tmp_val_list:
		# get non-repeated value list
		tmp_val_list.append(val)
		# get non-repeated key list
		tmp_key_list.append(key)
		
# create repeated key list
for key in dic1.keys():
	if key not in tmp_key_list:
		del_key_list.append(key)

# delete repeated items from dictionary
for key in del_key_list:
	del dic2[key]

# output result
print(tmp_val_list)
print(tmp_key_list)
print(del_key_list)
print(dic2)

