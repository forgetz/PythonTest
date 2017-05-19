from line import LineClient, LineGroup, LineContact
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

USERNAME = 'saranpong.kom@gmail.com'
PASSWORD = ''
GROUPNAME = 'Bnz'
MYID = 'forgetz'
 
#optional
COMPUTERNEME = 'Bnz-PC'
TOKEN = ''

try:
	client = LineClient(id=USERNAME, password=PASSWORD)
	TOKEN = client.authToken
	print "TOKEN : %s\r\n" % TOKEN

except Exception as ex:
	print "Login Failed"
	print ex
	exit()

client_group = client.getGroupByName(GROUPNAME)
client_group.sendMessage("Hello!!")

recent_group_msg = client_group.getRecentMessages(count=10)
print "RecentMessages : %s\r\n" % recent_group_msg

while True:
	op_list = []
	for op in client.longPoll():
		op_list.append(op)

	for op in op_list:
		sender   = op[0]
		receiver = op[1]
		message  = op[2]
		msg = message.text

		fromwhom = client.getContactByName(sender.name)
		print "fromwhom : %s\r\n" % fromwhom
		#fromwhom.sendMessage("Hi")

		if msg == "exit":
			time.sleep(3)
			receiver.sendMessage("%s\r\n" % ("goodbye!"))
			exit()

		if msg.startswith("sel"):
			time.sleep(3)
			params = msg.split(' ')
			input_dep = params[1]
			input_arr = params[2]
			input_date = params[3]

			print input_dep
			print input_arr
			print input_date

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

			try:
				time.sleep(10)
				screenname = "screen_" + input_dep + "_" + input_arr + "_" + input_date + ".png"
				savescreen = browser.save_screenshot(screenname)
				print "save screenshot completed!"
			except Exception as ex:
				print "error: save screenshot"
				receiver.sendMessage("%s\r\n" % ("error: save screenshot!"))

			browser.quit()
			time.sleep(3)
			
			receiver.sendImage(screenname)
			receiver.sendSticker()