from func import *


# ATM main route
while True:
	# user login
	usr_name = input('Enter user name: ')
	usr_pass = input('Enter user password: ')
	enabl = False
	balance_sum, trans_sum = 0, 0
	n_list = []
	########### user check ###########
	#log_check = user_check_json(usr_name, usr_pass, "users.json" )
	log_check = user_check_csv(usr_name, usr_pass, "users.csv" )
	if log_check == False:
		continue
	# activate promo program json
	bprog = user_promo(usr_name)
	print(bprog)
	# start promotion program
	if bprog:
		bbalance = balance_read_json(usr_name, enabl = True)
		bbalance += (bbalance // 10)
		balance_write_json(usr_name, bbalance)
	sel, func = atm_menu()
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
		trans_sum, balance_sum = trans_check(usr_name)
		trans_ok = (trans_sum != 0)
		########### banknotes box check ###########
		with open("note_box.json", "r") as note_file:
			note_data = json.load(note_file)
		# sort banknotes box in descending order
		# stack_s = {k: v for k, v in sorted(stack.items(), key=lambda item: item[1])}
		stack_s = {k: v for k, v in sorted(note_data.items(), key=lambda item: item[1], reverse = True)}
		# unpack exixting banknote set to list
		for key,val in stack_s.items():	
			for i in range(0, val):
				if key * val != 0:
					n_list.append(int(key))
		#print(n_list)
		# sort banknotes box in descending order
		n_list.sort(reverse=True)
		########debug print(n_list)
		# find sum combination for discharge in list
		c_list = []
		discharg = False
		if trans_sum < 0:
			c_list = comb_check(n_list, abs(trans_sum))
			discharg = True
		#print(c_list)
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
		########debugprint('stack u', stack_u)
		########debugprint('ok',trans_ok, comb_ok)
		if trans_ok and (comb_ok or discharg == False):
			#trans_write_json(usr_name, trans_sum)
			trans_write_csv(usr_name, trans_sum)
			balance_write_json(usr_name, balance_sum)
			with open("note_box.json", "w") as note_file:
				json.dump(stack_u, note_file)
		
	











	












