# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
import lxml
import re
import time

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
html_data = BeautifulSoup(response.text, "lxml")
quotes = html_data.find_all(class_='quote')
store_file = open('quotes.txt', 'r+')
for quote in quotes:
	print()
	quote_text = quote.find(class_='text').get_text().replace('“', '').replace('”', '')
	print(quote_text)
	quote_author = quote.find(class_='author').get_text()
	print(quote_author)
	quote_keyw = quote.find(class_='keywords')['content']
	print(quote_keyw)
	## use CSS selectors
	href_obj = quote.find('a', href = True)
	# get list of href objects
	href_list = [href_obj['href'] 
		for href_obj in quote.select('a[href]') if href_obj['href']]
	# filter links about author
	href_link = [lnk for lnk in href_list if lnk.startswith('/author')]
	css_link = url + href_link[0]
	print(css_link)
	## use regular expressions
	re_link = url + quote.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
	print(re_link)
	# get info by sublink
	time.sleep(1)
	aut_data = BeautifulSoup(requests.get(css_link).text, "lxml")
	# aut_data = BeautifulSoup(requests.get(re_link).text, "lxml")
	aut_born = aut_data.find(class_='author-born-date').get_text()
	aut_loc = aut_data.find(class_='author-born-location').get_text()
	print('born ', aut_born, aut_loc)
	# write data to txt file
	store_file.write('\n'+ quote_text)
	store_file.write('\n' + quote_author)
	if quote_author not in store_file:
		store_file.write('\n' + aut_born + aut_loc)
store_file.close()




