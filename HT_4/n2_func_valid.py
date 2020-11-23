# 2. function login and pass list validation
# login less then 50 and more then 3 symbols
# pass more then 8 symbols and consist at least 1 digit
# no space in pass and login
# if any parametrs not match - create Exception
def func_valid(usrname, usrpass):
	name_len_ok = False
	name_comp_ok = False
	pass_len_ok = False
	pass_comp_ok = False	

	if len(usrname) > 3 and len(usrname) < 50:
		name_len_ok = True
	else:
		raise Exception('UserNameLenghtException')

	space_count = 0
	for symb in usrname:
		if symb.isspace():
			space_count += 1 
	if space_count == 0:
		name_comp_ok = True
	else:
	 	raise Exception('UserNameCompositionException')

	if len(usrpass) > 8:
		pass_len_ok = True
	else:
	 	raise Exception('UserPassLenghtException')

	digt_count = 0
	space_count = 0
	for symb in usrpass:
		if symb.isdigit():
			digt_count += 1
		if symb.isspace():
			space_count += 1
	if digt_count >= 1 and space_count == 0:
		pass_comp_ok = True
	else:
	 	raise Exception('UserPassCompositionException')

	valid = (name_len_ok and name_comp_ok and pass_len_ok and pass_comp_ok)
	# return (valid, name_len_ok, name_comp_ok, pass_len_ok, pass_comp_ok)
	return valid	
	

chk_usr1, chk_pass1 = 'john', 'nc45r5vbt'
chk_usr2, chk_pass2 = 'pe', '7uirg567rt'
chk_usr3, chk_pass3 = 'j kty', '7uirg567rt'

chk_usr4, chk_pass4 = 'marco', 'adt6'
chk_usr5, chk_pass5 = 'greg', 'adt rtyuy'	

# case1
print('login and pass are correct: ', func_valid(chk_usr1,chk_pass1))

# case2
print('login lenght is incorrect: ', func_valid(chk_usr2,chk_pass2))
# case3
# print('login composition is incorrect: ', func_valid(chk_usr3,chk_pass3))

# case4
# print('pass lenght is incorrect: ', func_valid(chk_usr4,chk_pass4))
# case5
# print('pass composition is incorrect: ', func_valid(chk_usr5,chk_pass5))				
