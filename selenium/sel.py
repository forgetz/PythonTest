from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import autopy
import time
import sys

input_dep = sys.argv[1]
input_arr = sys.argv[2] 
input_date = sys.argv[3]

browser = webdriver.Firefox()
browser.get('http://sis.pg')

elem_user = browser.find_element_by_name('txtUserName')
elem_user.send_keys('kanisorn.won')
elem_pass = browser.find_element_by_name('txtUserPwd')
elem_pass.send_keys('1234' + Keys.RETURN)

browser.get('http://sis.pg/fBookingSummary.aspx')

time.sleep(3)
elem_date = browser.find_element_by_name('txtflightdate').clear()
time.sleep(3)
elem_date2 = browser.find_element_by_name('txtflightdate')
#elem_date2.send_keys('20160826' + Keys.RETURN)
elem_date2.send_keys(input_date + Keys.RETURN)

try:
	time.sleep(3)
	elem_dep = browser.find_element_by_xpath("//select[@name='cboDeptPort']")
	dep_options = elem_dep.find_elements_by_tag_name("option")
	for option1 in dep_options:
		if option1.get_attribute("value") == input_dep:
			option1.click()
except Exception as ex:
	print "error: elem_dep"

try:
	time.sleep(3)
	elem_arr = browser.find_element_by_xpath("//select[@name='cboArrPort']")
	arr_options = elem_arr.find_elements_by_tag_name("option")
	for option2 in arr_options:
		if option2.get_attribute("value") == input_arr:
			option2.click()
except Exception as ex:
	print "error: elem_arr"

time.sleep(3)
elem_query = browser.find_element_by_name('cmdQuery')
elem_query.send_keys(Keys.RETURN)

time.sleep(10)
savescreen = browser.save_screenshot('screen.png')
print "save screenshot completed!"

browser.quit()