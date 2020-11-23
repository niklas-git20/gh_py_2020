# enter values x and y. create some function to check equality of variables
# - x > y;     answ: x is greater than y in z
# - x < y;     answ: y is greater than x in z
# x == y.      answ: - х equal y

def equality(x,y):
	if x > y:
		print(f'x is greater than y in {x - y}')
	elif x < y:
		print(f'y is greater than x in {y - x}')
	elif x == y:
		print(f'x is equal y')

x, y = map(int, input('enter spaced x and y: ').split()) 

equal1 = equality(x,y) 





