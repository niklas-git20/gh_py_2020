# https://www.expireddomains.net/deleted-domains/
import requests
from bs4 import BeautifulSoup
import re
import time
import csv

#### process page "deleted domain"
pre_url = 'https://rozetka.com.ua'
# check category computers, memory, id = 
cat_name = 'memory'
cat_id = 'c80081'
# csv file for records
f_name = cat_id + '_products.csv'
store_file = open(f_name, 'a', encoding='utf-16')
# titles for file
t_rec = ['id','link','description','price']
data_wr = csv.writer(store_file, delimiter=';')
data_wr.writerow(t_rec)

# start url
start_url = pre_url + '/' + cat_name + '/' + cat_id
url = start_url
print(url)


count = 1
# collect data from 5 pages
while count < 6:
	count +=1
	# get data from page		
	response = requests.get(url)
	html_data = BeautifulSoup(response.text, "lxml")
	# # get pool of link to other pages
	# page_url = [url.get('href') for url in html_data.select('a.pagination__link')]
	# page_url.remove(None)
	# print(page_url)
	# # get link to next page
	# some_url = [url.get('href') for url in html_data.select('a.button')]
	# next_url = [url for url in some_url if 'page' in str(url)]
	# print(next_url)
	# # [print(url) for url in some_url if str(url).find('https') != -1]
	suf_url = '/' + 'page=' + str(count)
	url = start_url + suf_url
	print(url)

	# get data from page
	products = html_data.find_all(class_='goods-tile__inner')
	for product in products:
		p_rec = []
		p_id = product['data-goods-id']
		p_rec.append(p_id)
		# print(p_id)
		p_link = product.find('a')['href']
		p_rec.append(p_link)
		# print(p_link)
		p_descr = product.find(class_='goods-tile__title')
		p_rec.append(p_descr.text)
		# print(p_descr.text)
		p_price = product.find(class_='goods-tile__price-value')
		p_rec.append(p_price.text)
		# print(p_price.text)
		data_wr = csv.writer(store_file, delimiter=';')
		data_wr.writerow(p_rec)
store_file.close()
