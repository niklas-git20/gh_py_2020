# ATM functionality
import json
from os import path
from datetime import datetime
from itertools import combinations

# check user login and password
def user_check(usr_name, usr_pass, file_name):
	with open(file_name, "r") as user_data:
		usr_list = json.load(user_data)
	usr_ok = False
	pass_ok = False
	# check user name
	for rec in usr_list:
		if usr_name == rec['name']:
			usr_ok = True
			break
	else:
		print('Login is incorrect')
	# check user password
	for rec in usr_list:
		if usr_pass == rec['pass']:
			pass_ok = True
			break
	else:
		print('Password is incorrect')
	if usr_name == True and usr_pass == True:
		print (f'Welcome {usr_name}! You entered in system')
	return (usr_ok and pass_ok)


# dummy function
def atm_dummy(*args):
	pass


# atm menu
def atm_menu():
	# menu text set
	oper_menu = {
	'1': 'check balance',
	'2': 'account extract', 
	'3': 'charge(+) / withdraw(-) account',
	}
	# menu functions set
	oper_func = {
	'1': ('acc_check', 'balance_read'),
	'2': ('acc_check', 'trans_read'),
	'3': ('trans_check', 'comb_check', 'trans_write', 'balance_write')
	}		
	[print(key,': ', value) for key, value in oper_menu.items()]
	oper = ''
	while True:
		oper = input('\nSelect operation: ')
		if oper not in oper_menu:
			print("inpossible operation")
			continue
		else:
			break
	return oper, oper_func[oper]


# check user account is available
def acc_check(usr_name):
	balance = usr_name + "_balance.json"
	trans = usr_name + "_trans.json"
	check_ok = False
	# used os.path
	if path.exists(balance) and path.exists(trans):
	 	check_ok = True
	return check_ok


# check transaction
def trans_check(usr_name):
	file_name = usr_name + "_balance.json"
	try:
		trans_act = int(input('Enter charge amount sum: '))
	except ValueError:
		return ('value not valid')
	balance_file = open(file_name, 'r')
	balance_data = json.load(balance_file)
	balance_act = balance_data["balance"]
	balance_file.close()
	if balance_act + trans_act > 0:		
		balance_act += trans_act		
	else:
		trans_act = 0
		print('operation not is not possible')
	return trans_act, balance_act


# read user balance
def balance_read(usr_name, enabl):
	if enabl == False:
		return
	file_name = usr_name + "_balance.json"
	with open(file_name, "r") as balance_file:
		balance_data = json.load(balance_file)
		print (balance_data["date"], balance_data["balance"])


# write user balance
def balance_write(usr_name, balance_sum):
	file_name = usr_name + "_balance.json"
	balance_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	balance_rec = {"date":balance_date, "balance":balance_sum}
	with open(file_name, "w") as balance_file:
		json.dump(balance_rec, balance_file)
		print (balance_rec)


# read user transactions
def trans_read(usr_name, enabl):
	if enabl == False:
		return
	file_name = usr_name + "_trans.json"
	with open(file_name, "r") as trans_file:
		trans_data = json.load(trans_file)
		for trans in trans_data:
			print (trans["date"], trans["charge"])


# write user transaction
def trans_write(usr_name, trans_sum):	
	file_name = usr_name + "_trans.json"
	trans_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	trans_rec = {"date":trans_date, "charge":trans_sum}
	with open(file_name, "r+") as trans_file:
		temp_data = list(json.load(trans_file))
		temp_data.append(trans_rec)
		trans_file.seek(0)
		json.dump(temp_data, trans_file,indent =2)
		print (trans_rec)


# find sum combinations in list
def comb_check (numbers, target):	
	# define combinations of banknotes to get required sum				
	idx_end = len(numbers)
	idx_start = 0
	count_m = []	
	while idx_start < idx_end:
		targ_tmp = target
		count_tmp = []
		for idx in range(idx_start, idx_end):
			diff = targ_tmp - numbers[idx]		
			if diff >= 0:
				targ_tmp -= numbers[idx]
				count_tmp.append(numbers[idx])
			if diff < 0:
				diff + numbers[idx]
				continue
			if diff == 0:
				count_m.append(count_tmp)	
		idx_start += 1
	return count_m




	
	
	










		

