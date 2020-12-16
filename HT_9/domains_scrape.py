# https://www.expireddomains.net/deleted-domains/
import requests
from bs4 import BeautifulSoup
import re
import time
import csv


#### process main page
# main_url = 'https://www.expireddomains.net'
# # GET request to fetch raw html content
# main_response = requests.get(main_url)
# # parse html content
# main_data = BeautifulSoup(main_response.content,"lxml")

# ua_dmn_aux1 = ''
# # filter link for page 'deleted domains'
# for dmn_link in main_data.find_all('a'):
# 	if 'Deleted Domains' in dmn_link.text:
# 		del_dmn_aux1 = dmn_link.get('href')
# del_dmn_url = del_dmn_aux1
# print(del_dmn_url)

# combine link to deleted domain page
# del_dmn_url = main_url.strip() + del_dmn_url.strip()


#### process page "deleted domain"
pre_url = 'https://www.expireddomains.net/deleted-domains'
next_url = ' '


### open page offline
offl_pre_url = "C:/Users/Nik/Desktop/gh_py_2020/HT_9/html/deleted-domains"
offl_next_url = '0'

# get data from pages
count = 0
while count < 5:
	count += 1
	del_dmn_url = pre_url.strip() + next_url.strip()
	print(del_dmn_url)
	# time.sleep(2)
	## GET request to fetch raw html content
	deldmn_response = requests.get(del_dmn_url)
	## parse html content
	deldmn_data = BeautifulSoup(deldmn_response.content,"html.parser")

	## offline page processing
	# offl_url = offl_pre_url.strip() + '_'.strip()  + offl_next_url.strip() + '.html'.strip()
	# print(offl_url)
	# offl_response = open(offl_url, 'r')
	# deldmn_data = BeautifulSoup(offl_response,"lxml")

	# page navigation
	page_next_aux = deldmn_data.select('a.next')
	for page_next in page_next_aux:
		offs_url = page_next['href']
	
	# prepare link to next page
	try:
		next_url = offs_url.replace('deleted-domains/', '')
		offl_next_url = str(re.search(r'\d+', offs_url)[0])
		print(offl_next_url)
	except:
		print ('page is banned')
		quit()

	# find url table
	# uadmn_table = uadmn_data.find('table', attrs = {'class': 'base1'})
	deldmn_table = deldmn_data.select_one('div.listing > table.base1')
	deldmn_table_data = deldmn_table.find_all('tr')

	# open csv file
	f_name = './csv/' + 'del_domains_list' + offl_next_url + '.csv'
	f = open(f_name, 'w', newline='')
	# process data from html
	t_rec = []
	re_ptn = r'[\'\s]+'
	for tr in deldmn_table_data:	
		#append list
		tr_data = tr.find_all(['td','th'])
		td_row = []
		for td in tr_data:		
			try:
				td_elm_aux = td.select_one('a').text				
			except AttributeError:
				td_elm_aux =  td.text
			# cleat record from string control
			td_elm = re.sub(re_ptn, '', td_elm_aux)
			# print(td_elm)
			# add record if not RL
			if td_elm != 'RL':
				td_row.append(td_elm)
		# write to csv file		
		csvwriter = csv.writer(f, delimiter=';')
		csvwriter.writerow(td_row)	
		# print(td_row)
		t_rec.append(td_row)
	# close csv file
	f.close()	







