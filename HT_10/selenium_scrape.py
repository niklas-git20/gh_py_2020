# run search on site with selenium
# https://www.olx.ua/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



drv_path = 'C:\\Program Files\\Google\\chromedriver.exe'
url = 'http://www.olx.ua'
url_tmp = 'https://www.olx.ua/list/q-raspberry-pi'
# run webdriver and get content
driver = webdriver.Chrome(drv_path)
# set timeout
# driver.implicitly_wait(20)
# driver.set_page_load_timeout(20)

# open page to get scrollheight
driver.get(url)
# # temp to check objects
# table_obj = driver.find_element_by_css_selector('div.listHandler > table')
# with open('temp1.txt', 'w') as f:
# 	f.write(table_obj.get_attribute('innerHTML'))
# with open('temp2.txt', 'w') as f:
# 	f.write(table_obj.get_attribute('outerHTML')
# get scroll height by using math
# height = driver.execute_script("return Math.max\
# 	( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, \
# 	document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
# get scroll height without math
height = driver.execute_script("return document.body.scrollHeight")
print('height = ', height)
#close browser
driver.close()

# browser options: headless with height extracted above
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--window-size=1920,{height}")
chrome_options.add_argument("--hide-scrollbars")
# run webdriver and get content
driver = webdriver.Chrome(drv_path, options=chrome_options)
# set timeout
wait = WebDriverWait(driver, 30)
# open page to get content
driver.get(url)
# save current url
curr_url = driver.current_url
# search keys
s_target = 'raspberry pi'
# to use explicit conditions: locator should be enclosed
# find search field
s_field = wait.until(EC.presence_of_element_located((By.ID, 'headerSearch')))
s_field.send_keys(s_target)
# find conform button
s_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-searchmain")))
s_button.click()
# wait for URL to change
p_load = wait.until(EC.url_changes(curr_url))
# save new url
new_url = driver.current_url
# take screenshot
# element with longest height on page
driver.get_screenshot_as_file('olx_search3.png')
driver.save_screenshot('olx_search3.png')
# html element
# s_table1 = driver.find_element_by_class_name('fixed offers.offers--top redesigned')
s_table1 = driver.find_element_by_xpath("//div[@class = 'content']//table")
s_table1.screenshot('olx_search1.png')

s_table2 = driver.find_element_by_id('offers_table')
# image re-size 
curr_win_size = driver.get_window_size()
sz = s_table2.size
h = sz['height']
driver.set_window_size(curr_win_size['width'], h + 200)
s_table2.screenshot('olx_search2.png')
# close web driver
driver.close()
print(curr_url, '\n', new_url)
