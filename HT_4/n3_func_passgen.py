# 3 function generate valid pass list
# create list with usernames and passwords, valid and not
# ckeck list in cycle and set validity for each record
def func_loglist_check(usrlist):
	name_len_ok = False
	name_comp_ok = False
	pass_len_ok = False
	pass_comp_ok = False

	
	for usr_pass in usrlist:		
		for usr, passw in usr_pass.items():
			# user name lenght check
			name_len_ok = (len(usr) > 3 and len(usr) < 50)			
			# spaces in username check
			space_count = 0			
			for symb in usr:
				if symb.isspace():
					space_count += 1 
			name_comp_ok = (space_count == 0)
			# user pass lenght check
			pass_len_ok = (len(passw) > 8)
			# user pass composition check
			digt_count = 0
			space_count = 0
			for symb in passw:
				if symb.isdigit():
					digt_count += 1
				if symb.isspace():
					space_count += 1
			pass_comp_ok = (digt_count >= 1 and space_count == 0)
			
			# output results
			msg = ''
			if name_len_ok and name_comp_ok and pass_len_ok and pass_comp_ok:
				msg = 'OK'
			elif name_len_ok != True:
				msg = 'username lenght not ok'
			elif name_comp_ok != True:
				msg = 'username consists spaces'
			elif pass_len_ok != True:
				msg = 'user password lenght not ok'
			elif pass_comp_ok != True:
				msg = 'user password consists spaces or dont have digits'
			print (f'\n Name: {usr} \n Password: {passw} \n Status: {msg}' )
	return

usr_list = [{'john' : 'nc45r5vbt'}, 
				{'pe' : '7uirg567rt'},
				{'j kty' : '7uirg567rt'},
				{'simon' : 'adt6'},
				{'kate' : 'adt rtyuy'}]


func_loglist_check(usr_list)
