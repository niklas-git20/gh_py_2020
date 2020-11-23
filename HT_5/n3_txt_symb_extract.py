# 3. get defined symbol amount from beginning, middle and end of file
import os

def text_extract(textfile, symb_qty):
	symb_num = os.path.getsize(textfile)
	if symb_qty > symb_num:
		return 'file size too short'
	offs = 0
	if symb_num % 2 == 0:
		offs = 1

	with open (textfile, 'r') as text:
		text.seek(0)
		beg_text = text.read(symb_qty)
		
		text.seek(symb_num - symb_qty)
		end_text = text.read(symb_qty)
		
		text.seek(symb_num // 2 - offs)
		mid_text = text.read(symb_qty + offs)
		text.seek(0)
	return list(beg_text), list(mid_text), list(end_text)



print(text_extract('textlist_ok.txt', 3))
print(text_extract('textlist_nok.txt', 1))
