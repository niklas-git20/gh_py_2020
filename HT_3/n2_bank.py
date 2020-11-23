# 2. function <bank>
# take deposit <a> unit for period <years> at <percent>
# deposit increases by this percent each year, then growth added to deposit
# return printed expected deposit ammount

def bank(ammount, years, percent=10):
	# check input parameter
	try:
		amm = int(ammount)
		yr = int(years)
		perc = int(percent)
	except ValueError:
		print ('values not valid')
		return
	# calculate depo increase
	for i in range(yr):
		incr = amm * perc / 100
		amm += incr
	return(amm)

# get input data
a,y,*p = input('enter commaseparated deposit \n ammount, duration, percentage (default 10%): ').split(',')
# check input data
# print(a,y,*p)

# output results
print(f'expected deposit is: {bank(a,y,*p)}')

res = bank(a,y,*p)
print('expected deposit is: {0}'.format(res))


