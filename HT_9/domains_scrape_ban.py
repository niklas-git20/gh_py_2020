# https://www.expireddomains.net/
import requests
from bs4 import BeautifulSoup
import re
import time
import csv



main_url = 'https://www.expireddomains.net'
# GET request to fetch raw html content
main_response = requests.get(main_url)
# parse html content
main_data = BeautifulSoup(main_response.content,"lxml")

ua_dmn_aux1 = ''
# filter link for domains UA
for dmn_link in main_data.find_all('a'):
	if 'ua' in dmn_link.text:
		ua_dmn_aux1 = dmn_link.get('href')
ua_dmn_url = ua_dmn_aux1
print(ua_dmn_url)

# combine link to ua domain page
ua_dmn_url = main_url.strip() + ua_dmn_url.strip()
print(ua_dmn_url)

time.sleep(2)
# GET request to fetch raw html content
uadmn_response = requests.get(ua_dmn_url)
# parse html content
uadmn_data = BeautifulSoup(uadmn_response.content,"lxml")
# find url table

# uadmn_table = uadmn_data.find('table', attrs = {'class': 'base1'})
uadmn_table = uadmn_data.select_one('div.listing > table.base1')
uadmn_table_data = uadmn_table.find_all('tr')

# open csv file
f = open('ua_domains_list', 'w', newline='')
# process data from html
t_rec = []
re_ptn = r'[\'\s]+'
for tr in uadmn_table_data:
	#append list
	td_row = []
	for td in tr:
		td_elm = re.sub(re_ptn, '', td.string)
		# add record if not empty
		if td_elm != '':
			td_row.append(td_elm)
	# write to csv file
	csvwriter = csv.writer(f, delimiter=';')
	csvwriter.writerow(td_row)		
	print(td_row)
	t_rec.append(td_row)
# close csv file
f.close()	







