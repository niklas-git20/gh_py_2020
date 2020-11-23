# 5. check leap year in range

year1, year2 = [int(x) for x in input("Enter two years comma separated: ").split(',')]
# year1, year2 = int(input("Enter two years comma separated: ").split(','))
if year1 > year2:
	tmp_year = year2
	year2 = year1
	year1 = tmp_year

for year in range(year1,year2+1):
	if (year % 4) == 0:
	   if (year % 100) == 0:
	       if (year % 400) == 0:
	           print("{0} is a leap year".format(year))
	       else:
	           # print("{0} is not a leap year".format(year))
	           pass
	   else:
	       print("{0} is a leap year".format(year))	    
	else:
	   # print("{0} is not a leap year".format(year))
	   pass
	



