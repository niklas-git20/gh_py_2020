# https://www.olx.ua
# https://www.olx.ua/sitemap.xml
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re
import time

def scrape(url, quant):
# process sitemap
	# cat_url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/'
	cat_url = url
	time.sleep(1)
	# collect advert links
	ladv_response = requests.get(cat_url)
	ladv_data = BeautifulSoup(ladv_response.content,"lxml")
	# get list of href objects
	href_list = [href_obj['href'] 
		for href_obj in ladv_data.select('a[href]') if href_obj['href']]
	# filter doubled links
	adv_list = [lnk for lnk in href_list if '/obyavlenie' in lnk]
	[adv_list.remove(adv) for adv in adv_list if adv in adv_list]	
	[print(adv) for adv in adv_list]
	print(len(adv_list))

	# run data scraping
	n_rec = int(quant)
	adv_res_list =[]
	for i in range(n_rec):
		
		time.sleep(1)
		# adv_url_tmp = 'https://www.olx.ua/obyavlenie/moschnyy-igrovoy-pk-ryzen-1600-af-2600-gtx-1080ti-16-ssd-hdd-IDJLiHG.html#427813bd58'
		adv_url = adv_list[i]

		session = requests.Session()
		session.headers ={
			'referer': adv_url
		}

		# get data from advert page
		adv_response = session.get(adv_url)
		# create soup object
		adv_data = BeautifulSoup(adv_response.content,"lxml")
		## find tag with name
		adv_name_aux1 = adv_data.select_one('div.offer-user__actions > h4 > a')
		# process data (delete spaces)
		adv_name = adv_name_aux1.text.replace(' ','')
		# to convert try decode('cp1251') and encode('utf8')
		print(adv_name)
		## find tag with ID
		adv_id_aux2= []
		adv_id_aux1 = [val for elm in adv_data.find_all('div', class_='contact-button')
							for val in elm['class']]
		try:
			adv_id_aux2, = [val for val in adv_id_aux1 if "'id':" in val]
		except ValueError:
			print('id and phone are missing')					
		adv_id = adv_id_aux2.replace("'id':", "").replace("'", "").replace(",","")
		# print(adv_id)
		## find tag with token
		adv_pt_aux1 = adv_data.select_one('section.offer-section > script')
		# process data (delete spaces)
		adv_pt_aux2 = adv_pt_aux1.string.replace('var phoneToken =','')
		adv_pt = adv_pt_aux2.replace(' ','').replace("'", "").replace(";", "")
		ajax_url = 'https://www.olx.ua/ajax/misc/contact/phone/'
		ph_url = ajax_url.strip() + adv_id.strip() + '/?pt='.strip() + adv_pt.strip()
		# print(ph_url)
		ph_resp = (session.get(ph_url)).json()
		print(ph_resp['value'])

		# collect advent data
		adv_rec = (adv_id, adv_url, adv_name, ph_resp['value'])
		adv_res_list.append(adv_rec)
		
	return adv_res_list






