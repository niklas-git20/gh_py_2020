# ATM functionality
import json
import csv
from os import path
from datetime import datetime
from itertools import combinations
import random

# check user login and password json
def user_check_json(usr_name, usr_pass, file_name):
	with open(file_name, "r") as user_data:
		usr_list = json.load(user_data)
	usr_ok = False
	pass_ok = False
	# check user name and password
	for rec in usr_list:
		if usr_name == rec['name'] and usr_pass == rec['pass']:
			usr_ok = True
			pass_ok = True
			print (f'Welcome {usr_name}! You entered in system')
			break
	else:
		print('Login or password is incorrect')
	return (usr_ok and pass_ok)



# check user login and password csv
def user_check_csv(usr_name, usr_pass, file_name):
	usr_ok = False
	pass_ok = False
	usr_rec =[]
	with open(file_name, "r") as user_data:
		usr_list = csv.reader(user_data, delimiter=';')	
		# for rec in usr_list:
		# 	print(rec[0],rec[1])
		for rec in usr_list:
			usr_rec.append(rec)
		# check user name and password
		for up in usr_rec:
			us, psw = up
			if usr_name == us and usr_pass == psw:
				usr_ok = True
				pass_ok = True
				print (f'Welcome {usr_name}! You entered in system')
				break
		else:
			print('Login or rassword is incorrect')
		return (usr_ok and pass_ok)

def user_promo(usr_name):
	file_name = "promo.csv"
	promo_fld = ["name","entry", "bonus entry"]
	promo = False
	with open(file_name, "r+", newline ='') as promo_file:
		temp_data_rd = list(csv.reader(promo_file, delimiter=';'))	
		for prec in temp_data_rd:			
			us,lcount,bcount = prec
			if us == usr_name:
				eidx = prec.index(lcount)
				bidx = prec.index(bcount)
				# increse entrance counter
				prec[eidx]= str(int(prec[eidx]) + 1)
				# calculate bonus entry every 10
				if int(prec[eidx]) % 10 == 0:
					prec[bidx] = str(random.randint(1, 10))
				# activate promotion
				if int(prec[eidx]) % 10 == int(prec[bidx]):
					promo = True
					prec[bidx] = 0
					print ('entry #: ',prec[eidx], 'bonus entry #: ',prec[bidx])
				# write updated data
				promo_file.seek(0)	
				temp_data_wr = csv.writer(promo_file, delimiter=';')
				temp_data_wr.writerows(temp_data_rd)
		return (promo)



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
	'1': ('acc_check', 'balance_read_json'),
	'2': ('acc_check', 'trans_read_csv'),
	'3': ('trans_check', 'comb_check', 'trans_write_csv', 'balance_write_json')
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
def balance_read_json(usr_name, enabl):
	if enabl == False:
		return 0
	file_name = usr_name + "_balance.json"
	with open(file_name, "r") as balance_file:
		balance_data = json.load(balance_file)
		print (balance_data["date"], balance_data["balance"])
	return balance_data["balance"]


# write user balance
def balance_write_json(usr_name, balance_sum):
	file_name = usr_name + "_balance.json"
	balance_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	balance_rec = {"date":balance_date, "balance":balance_sum}
	with open(file_name, "w") as balance_file:
		json.dump(balance_rec, balance_file)
		print (balance_rec)


# read user transactions json
def trans_read_json(usr_name, enabl):
	if enabl == False:
		return
	file_name = usr_name + "_trans.json"
	with open(file_name, "r") as trans_file:
		trans_data = json.load(trans_file)
		for trans in trans_data:
			print (trans["date"], trans["charge"])

# read user transactions csv
def trans_read_csv(usr_name, enabl):
	trans_rec =[]
	if enabl == False:
		return
	file_name = usr_name + "_trans.csv"
	with open(file_name, "r") as trans_file:
		trans_data = csv.reader(trans_file, delimiter=';')
		for tdata in trans_data:
			trans_rec.append(tdata)
		for trec in trans_rec:
			print (*trec)
		


# write user transaction json
def trans_write_json(usr_name, trans_sum):	
	file_name = usr_name + "_trans.json"
	trans_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	trans_fld = ["date","charge"]
	trans_rec = {"date":trans_date, "charge":trans_sum}
	with open(file_name, "r+") as trans_file:
		temp_data = list(json.load(trans_file))
		temp_data.append(trans_rec)
		trans_file.seek(0)
		json.dump(temp_data, trans_file,indent =2)
		print (trans_rec)

# write user transaction csv
def trans_write_csv(usr_name, trans_sum):	
	file_name = usr_name + "_trans.csv"
	trans_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	trans_fld = ["date","charge"]
	trans_rec = [trans_date, trans_sum]
	with open(file_name, "r+", newline ='') as trans_file:
		temp_data_rd = list(csv.reader(trans_file, delimiter=';'))		
		temp_data_rd.append(trans_rec)
		#trans_file.seek(0)
		temp_data_wr = csv.writer(trans_file, delimiter=';')
		#temp_data_wr.writerows(temp_data_rd)
		temp_data_wr.writerow(trans_rec)
		print (*trans_rec)


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




	
	
	










		

