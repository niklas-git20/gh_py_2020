# 1. Create cycle from 0 to N (entered by user)
# remainder of the division by 17 is equal to 0.
from math import remainder

n = int(input('enter number: '))
divident = 0
divisor = 17

while divident <= n:
	if remainder(divident, divisor) == 0:
		print(divident)
	divident += 1 


