# 1. function login and pass list check
# if user name and pass matched with list = return True
# if user name or pass not matched with list and silent = return False
# if user name or pass not matched with list and no silent = raise LoginException
def func_loglist(usrname, usrpass, silent = False):
	usr_list = {'john' : 'nc45r5', 
				'peter' : 'bg67ui',
				'jil' : 'a4d32t',
				'simon' : '56yu3b',
				'kate' : 'g5h6hm'}
	match_res = False
	# match_rec = []
	for key, val in usr_list.items():
		if key == usrname and val == usrpass:
			match_res = True
			# match_rec = key, val
	if match_res != True:
		if silent == True:
			match_res = False
		elif silent == False:
			match_res = None
			raise Exception('LoginException')		
	return match_res
	

chk_usr1, chk_pass1 = 'john', 'nc45r5'
chk_usr2, chk_pass2 = 'peter', '7ui'
chk_usr3, chk_pass3 = 'jklmn', 'a4d32t'	

print('login and pass are correct: ', func_loglist(chk_usr1,chk_pass1))
print('login is correct and silent: ', func_loglist(chk_usr2,chk_pass2, True))
print('pass is correct and no silent: ', func_loglist(chk_usr3,chk_pass3, False))					
