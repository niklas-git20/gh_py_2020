# 7. function <list_count>
# take a list
# return amount of identical elements in list
from collections import Counter

def list_count(in_list):
	# v1 use comprehension
	dupl_dict = {elm:in_list.count(elm) for elm in in_list}
	# v2 use collections.Counter
	# dupl_dict = Counter(in_list)
	# v3 use cycle for..
	# dupl_dict = {}
	# for elm in in_list:
	# 	dupl_dict[elm] = in_list.count(elm)
	
	# output duplicate amount
	return dupl_dict

usr_list = input('enter a commaseparated sequence: ').split(',')
print(list_count(usr_list))

res = list_count(usr_list)
print(res)
