import sqlite3
from sqlite3 import Error
from datetime import datetime
import random


# atm menu
def atm_menu_db():
	# menu text set
	oper_menu = {
	'1': 'check balance',
	'2': 'account extract', 
	'3': 'charge(+) / withdraw(-) account',
	}
	# menu functions set
	oper_func = {
	'1': ('acc_check_db', 'balance_read_db'),
	'2': ('acc_check_db', 'trans_read_db'),
	'3': ('trans_check_db', 'comb_check', 'trans_write_db', 'balance_write_db')
	}		
	[print(key,': ', value) for key, value in oper_menu.items()]
	oper = ''
	while True:
		oper = input('\nSelect operation: ')
		if oper not in oper_menu:
			print("Inpossible operation selected")
			continue
		else:
			break
	return oper, oper_func[oper]


# check user login and password
def user_check_db(usr_name, usr_pass):
	usr_ok = False
	pass_ok = False
	db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	conn = sqlite3.connect(db_file)
	sql_cmd = " SELECT * FROM "
	table_name = " users "
	table_cons = f" WHERE name IS '{usr_name}'"
	sql_query = sql_cmd + table_name + table_cons
	rd = ()	
	try:			
		curs = conn.cursor()
		curs.execute(sql_query)	
		rd = curs.fetchone()
	except Error as e:
		print(e)			
	# unpack tuple
	db_id, db_name, db_pass = 0, '', 0	
	try:
		(db_id, db_name, db_pass) = rd
	except TypeError:
		print('Account not exists')
	# print((db_id, db_name, db_pass))
	if usr_name == db_name and usr_pass == db_pass:
		usr_ok = True
		pass_ok = True
		print (f'Welcome {usr_name}! You entered in system')
	else:
		print('Login or password is incorrect')
	conn.commit()
	conn.close()		
	return (usr_ok and pass_ok)


# check user promotion status
def user_promo_db(usr_name):
	promo = False
	db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	conn = sqlite3.connect(db_file)
	sql_cmd = " SELECT * FROM "
	table_name = 'promo'
	table_cons = f" WHERE name IS '{usr_name}'"
	sql_query = sql_cmd + table_name + table_cons
	rd = ()
	try:			
		curs = conn.cursor()
		curs.execute(sql_query)
		rd = curs.fetchone()
	except Error as e:
		print(e)
	# unpack tuple
	db_id, db_us,db_lcount,db_bcount = 0, '', 0, 0
	try:
		(db_id, db_us,db_lcount,db_bcount) = rd
	except TypeError:
		print('Promotion for the account not exists')
	print (db_id, db_us,db_lcount,db_bcount)
	if db_us == usr_name:
		# increase entrance counter
		db_lcount += 1
		# calculate bonus entry every 10
		if db_bcount % 10 == 0:
			db_bcount = random.randint(1, 10)
		# activate promotion
		if db_lcount % 10 == db_bcount:
			promo = True
			db_bcount = 0
			print ('entry #: ', db_lcount, 'bonus entry #: ', db_bcount)
		# reset entry counter if over 100
		if db_lcount >= 100:
			db_lcount = 1
		#prepare updated data
		sql_cmd = " UPDATE "
		table_name = "promo"
		table_data = f" SET entry = '{db_lcount}', bonus_entry = '{db_bcount}' "
		table_cons = f" WHERE name IS '{usr_name}'"
		sql_query = sql_cmd + table_name + table_data + table_cons
		# write updated data
		try:
			curs = conn.cursor()
			curs.execute(sql_query)
			conn.commit()
		except Error as e:
			print(e)
	print('Promotion status: ')	
	return promo	


# check user account is available
def acc_check_db(usr_name):
	db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	conn = sqlite3.connect(db_file)
	curs = conn.cursor()
	check_ok = False
	# check if tables exist
	balance = "balance"
	trans = usr_name + "_transaction"
	sql_query = f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{balance}'"
	#get the count of tables with the name
	curs.execute(sql_query)	
	#if the count is 1, then table exists
	if curs.fetchone()[0]==1:
		check_ok = True
		#print('Table 1 exists.')
	sql_query = f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{trans}'"
	#get the count of tables with the name
	curs.execute(sql_query)	
	#if the count is 1, then table exists
	if curs.fetchone()[0]==1:
		check_ok = check_ok and True
		#print('Table 2 exists.')			
	#commit the changes to db			
	conn.commit()
	#close the connection
	conn.close()
	return check_ok


	# read user balance
def balance_read_db(usr_name, enabl):	
	if enabl == False:
		return 0
	db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	conn = sqlite3.connect(db_file)
	curs = conn.cursor()
	sql_cmd = " SELECT * FROM "
	table_name = "balance"
	table_cons = f" WHERE name IS '{usr_name}'"
	sql_query = sql_cmd + table_name + table_cons
	curs.execute(sql_query)
	rd = curs.fetchone()	
	# unpack tuple
	db_id, db_us,db_date,db_amm = 0, '', 0, 0
	try:
		(b_id, db_us, db_date, db_amm) = rd
	except TypeError:
		print('Record for the account not exists')
	# print(*rd)
	print (db_date, db_amm)
	return db_amm
	#commit the changes to db			
	conn.commit()
	#close the connection
	conn.close()


# write user balance
def balance_write_db(usr_name, balance_sum):
	db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	balance_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	conn = sqlite3.connect(db_file)
	curs = conn.cursor()
	sql_cmd = " UPDATE "
	table_name = "balance"
	table_data = f" SET bamm = '{balance_sum}', bdate = '{balance_date}' "
	table_cons = f" WHERE name IS '{usr_name}' "
	sql_query = sql_cmd + table_name + table_data + table_cons
	curs.execute(sql_query)
	#commit the changes to db			
	conn.commit()
	#close the connection
	conn.close()
	
	

# read user transactions
def trans_read_db(usr_name, enabl):
	if enabl == False:
		return	
	db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	conn = sqlite3.connect(db_file)
	curs = conn.cursor()
	sql_cmd = " SELECT * FROM "
	table_name = f'{usr_name}' + '_transaction'
	table_cons = " "
	sql_query = sql_cmd + table_name + table_cons
	curs.execute(sql_query)
	rd = curs.fetchall()
	#print(*rd)
	[print(*r) for r in rd]
	#commit the changes to db			
	conn.commit()
	#close the connection
	conn.close()
	

# write user transaction
def trans_write_db(usr_name, trans_sum):
	trans_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	trans_rec = (trans_date, trans_sum)
	db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	conn = sqlite3.connect(db_file)
	curs = conn.cursor()
	sql_cmd = " INSERT INTO "
	table_name = f'{usr_name}' + '_transaction'
	table_cons = " VALUES (?, ?)"			
	sql_query = sql_cmd + table_name + table_cons
	curs.execute(sql_query, trans_rec)
	#commit the changes to db			
	conn.commit()
	#close the connection
	conn.close()



# check transaction
def trans_check_db(usr_name):
	try:
		trans_act = int(input('Enter charge amount sum: '))
	except ValueError:
		return ('value not valid')
	db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	conn = sqlite3.connect(db_file)
	curs = conn.cursor()
	sql_cmd = " SELECT * FROM "
	table_name = "balance"
	table_cons = f" WHERE name IS '{usr_name}'"
	sql_query = sql_cmd + table_name + table_cons
	curs.execute(sql_query)
	rd = curs.fetchone()
	#commit the changes to db			
	conn.commit()
	#close the connection
	conn.close()
	# unpack tuple
	db_id, db_us,db_date,db_amm = 0, '', 0, 0
	try:
		(b_id, db_us,db_date,db_amm) = rd
	except TypeError:
		print('Record for the account not exists')
	balance_act = db_amm
	if balance_act + trans_act > 0:		
		balance_act += trans_act		
	else:
		trans_act = 0
		print('operation not is not possible')
	return trans_act, balance_act


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