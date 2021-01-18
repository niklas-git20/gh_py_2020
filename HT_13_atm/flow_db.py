from func_db import *


# !!! before running start database creation and initialization: atm_init_db.py file
# ATM with sqlite3 database main route
while True:
	# user login
	usr_name = input('Enter user name: ')
	usr_pass = input('Enter user password: ')
	enabl = False
	balance_sum, trans_sum = 0, 0
	n_list = []
	########### user check ###########
	#log_check = user_check_json(usr_name, usr_pass, "users.json" )
	#log_check = user_check_csv(usr_name, usr_pass, "users.csv" )
	log_check = user_check_db(usr_name, usr_pass)
	if log_check == False:
		continue
	# activate promo program json
	bprog = user_promo_db(usr_name)
	print(bprog)
	# start promotion program
	if bprog:
		bbalance = balance_read_db(usr_name, enabl = True)
		bbalance += (bbalance // 10)
		balance_write_db(usr_name, bbalance)
	sel, func = atm_menu_db()
	# select operation functions
	if sel == '1' or sel == '2':
		func1,func2 = func
		# account availability check	
		func1_res = globals()[func1](usr_name)
		print(func1_res)
		#read data from balance / transaction
		func2_res = globals()[func2](usr_name, func1_res)	
		print(func2_res)
	if sel == '3':
		########### transaction check ###########	 
		trans_sum, balance_sum = trans_check_db(usr_name)
		trans_ok = (trans_sum != 0)
		
		########### banknotes box check ###########
		# read data from note box table
		db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
		conn = sqlite3.connect(db_file)
		curs = conn.cursor()
		sql_cmd = " SELECT * FROM "
		table_name = 'note_box'
		table_cons = " "
		sql_query = sql_cmd + table_name + table_cons
		curs.execute(sql_query)
		rd = curs.fetchone()
		# nominal value rd type: tuple --> list
		val_list = (list(rd))
		# nominal names type: list
		nom_list = list(map(lambda x: x[0], curs.description))
		# using dictionary comprehension 
		# to convert lists to dictionary 
		note_data = {nom_list[i]: val_list[i] for i in range(len(nom_list))}
		########debug
		print('note data', note_data)
		#commit the changes to db			
		conn.commit()
		#close the connection
		conn.close()

		# sort banknotes box in descending order
		# stack_s = {k: v for k, v in sorted(stack.items(), key=lambda item: item[1])}
		stack_s = {k: v for k, v in sorted(note_data.items(), key=lambda item: item[1], reverse = True)}
		# unpack exixting banknote set to list
		for key,val in stack_s.items():	
			for i in range(0, val):
				if key * val != 0:
					n_list.append(int(key))
		# sort banknotes box in descending order
		n_list.sort(reverse=True)
		########debug 	print('n_list', n_list)
		# find sum combination for discharge in list
		c_list = []
		discharg = False
		if trans_sum < 0:
			c_list = comb_check(n_list, abs(trans_sum))
			discharg = True
		########debug 	print('c_list', c_list)
		# banknotes combination is available
		comb_ok = False
		if len(c_list) > 0:
			comb_ok = True
			comb_c = c_list[0]
			# discharge combination from account
			for n in comb_c:
				for m in n_list:
					if n == m:
						n_list.remove(m)
						break
		elif len(c_list) == 0 and discharg == True:
			print("Required banknotes are missing, please change sum")	
		############ write transaction to balance ############
		stack_u = {str(i): n_list.count(i) for i in n_list}
		########debug 		print('stack u', stack_u)
		########debug
		print('trans_ok', 'comb_ok', trans_ok, comb_ok)
		if trans_ok and (comb_ok or discharg == False):
			trans_write_db(usr_name, trans_sum)
			balance_write_db(usr_name, balance_sum)

			# split dictionary into keys and values 
			nom, val = zip(*stack_u.items())
			########debug
			print('nominal', nom)
			print('value', val)

			db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
			conn = sqlite3.connect(db_file)
			curs = conn.cursor()
			sql_cmd = " UPDATE "
			table_name = "note_box"
			table_data = (f" SET '{nom[0]}' = '{val[0]}', '{nom[1]}' = '{val[1]}', '{nom[2]}' = '{val[2]}',"
							f"'{nom[3]}' = '{val[3]}', '{nom[4]}' = '{val[4]}', '{nom[5]}' = '{val[5]}'")			
			table_cons = " "
			sql_query = sql_cmd + table_name + table_data + table_cons
			curs.execute(sql_query)
			#commit the changes to db			
			conn.commit()
			#close the connection
			conn.close()

		
	











	












