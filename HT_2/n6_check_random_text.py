# 6. check random text
# if lenght 30-50 print lenght, number of digits and letters
# if lenght < 30- print sum of number and concated letters only
# if lenght > 50 print 'too long row'
in_strg = input()

def let_numb(strg):
	numb = 0
	lett = 0
	oth = 0
	leng = len(strg)
	if 30 < leng < 50:		
		numb = sum(elm.isdigit() for elm in strg)
		lett = sum(elm.isalpha() for elm in strg)
		# oth  = len(strg) - numb - lett
		print(f'lenght is: {leng}, numbers ammount is: {numb}, letters ammount is :{lett}')
	if leng < 30:
		sum_numb = 0
		conc_lett = ''
		for elm in strg:
			if elm.isdigit():				
				sum_numb += int(elm)
			elif elm.isalpha():
				conc_lett += elm
		print(f'numbers sum is: {sum_numb}, letters concated is :{conc_lett}')

	if leng > 50:
		print(f'lenght is: {leng}, too long row')


		

		
let_numb1 = let_numb(in_strg)