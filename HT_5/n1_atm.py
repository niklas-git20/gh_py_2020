# 1 ATM application
import json
from datetime import datetime

# 

def user_check(usr_name, usr_pass, file_name):
	with open(file_name, "r") as user_data:
		usr_list = json.load(user_data)
		log_ok = False
		for rec in usr_list:
			# print (usr_name, rec['name'])
			# print (usr_pass, rec['pass'])
			if (usr_name == rec['name'] and usr_pass == rec['pass']):
			 	log_ok = True				
			 	break
		if log_ok == True:
			print (f'Welcome {usr_name}! You entered in system')
		else:
			print ('Login or password is incorrect')


def user_read_balance(name):
	try:
		file_name = name + "_balance.json"	
		json_file = open(file_name, "r")
		balance_data = json.load(json_file)
		json_file.close()
		print (balance_data["date"], balance_data["balance"])
	except FileNotFoundError:
		print ('balance not available')


def user_write_balance(upd_data, name):
	file_name = name + "_balance.json"
	balance_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	balance_sum = upd_data	
	balance_rec ={"date":balance_date, "balance":balance_sum}			
	json_file = open(file_name, "w")		
	json.dump(balance_rec,json_file)
	json_file.close()
	print (balance_rec["date"], balance_rec["balance"])


def user_read_trans(name):
	try:
		file_name = name + "_trans.json"
		json_file = open(file_name, 'r')
		balance_data = json.load(json_file)
		json_file.close()
		for rec in balance_data:
			print (rec["date"], rec["charge"])
	except FileNotFoundError:
		print ('transactions not available')


def user_write_trans(upd_data, name):
	trans_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	trans_sum = upd_data
	trans_rec ={"date":trans_date, "charge":trans_sum}	
	try:
		file_name = name + "_trans.json"				
		json_file = open(file_name, 'r')	
		json_data = json.load(json_file)	
		json_file.close()
	except FileNotFoundError:
		json_data = {}
	temp_data =list(json_data)
	temp_data.append(trans_rec)
	json_file = open(file_name, 'w')	
	json.dump(temp_data,json_file,indent=2)
	json_file.close()
	print (trans_rec["date"], trans_rec["charge"])	


def user_check_trans(name):
	file_name = name + "_balance.json"
	try:
		charg_act = int(input('Enter charge amount sum: '))
	except ValueError:
		return ('value not valid')
	try:
		json_file = open(file_name, 'r')
		balance_data = json.load(json_file)
		balance_act = balance_data["balance"]
		json_file.close()
	except FileNotFoundError:
		balance_act = 0	
	if balance_act + charg_act > 0:		
		balance_act += charg_act		
	else:
		charg_act = 0
		print('operation not is not possible')
	print(balance_act)
	return balance_act, charg_act




# main route
flow =True
while flow == True:
	run_sel = input('Press "y" to continue or any key to exit: ')
	if run_sel == "y":
		flow = True
	else:
		flow = False
		break
	# user login
	usr = input('Enter user name: ')
	psw = int(input('Enter user password: '))	
	user_check(usr,psw,"users.json")
	# user menu
	oper = int(input('\nSelect operation: '
		'\n1 - check balance'
		'\n2-  accout extract'
		'\n3 - withdraw or charge account'
		'\n4 - activate account'
		'\n5 - exit\n'))
	
	if oper == 1:	 	
		user_read_balance(usr)
	if oper == 2:	 	
	 	user_read_trans(usr)
	if oper == 3:
		balance, charge = user_check_trans(usr)	 	
		user_write_trans(charge, usr)
		user_write_balance(balance, usr)
	if oper == 4:
		balance, charge = 0, 0
		user_write_trans(charge, usr)
		user_write_balance(balance, usr)		
	if oper == 5:	 	
	 	break

	# case operation menu - need to check !!!
	# started all functions
	# if oper == '3':
	#  	balance, charge = user_check_trans(usr)
	# else:
	#  	balance, charge = 0, 0
	# oper_menu = {
	# 1: user_read_balance(usr),
	# 2: user_read_trans(usr),
	# 3: (user_write_trans(charge, usr),user_write_balance(balance, usr))
	# }	
	# oper_menu[oper]



	
