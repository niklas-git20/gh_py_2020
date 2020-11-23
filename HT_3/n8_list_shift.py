# 8. function <list_shift>
# take a list and shift
# shift > 0 move from end to biginning, shift < 0 move from beginning to end
# return shifted list
from collections import deque
def list_shift(in_list,shift=0):
	# shift elements in list
	# v1 use negative indices
	# indc = shift % len(in_list)
	# tmp_list = in_list[-indc:] + in_list[:-indc]	
	#v2 use collections.deque
	tmp_list = deque(in_list)
	tmp_list.rotate(shift)
	# convert list elements
	out_list = [int(elm) for elm in tmp_list]
	return out_list

usr_list = input('enter a commaseparated sequence: ').split(',')
usr_shift = int(input('enter a shift: '))
print(list_shift(usr_list,usr_shift))

res = list_shift(usr_list,usr_shift)
print(res)