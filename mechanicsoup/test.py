import argparse
import mechanicalsoup
import cPickle as pickle

def save_object(obj, filename):
	with open(filename, 'a') as output:
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
	data = pickle.load(open(filename,"rb"))
	output2 = open("write.txt","w")
	output2.write(str(data))
	output2.flush()
	output2.close()

parser = argparse.ArgumentParser(description='Login to GitHub.')
parser.add_argument("username")
parser.add_argument("password")
args = parser.parse_args()

browsers = mechanicalsoup.Browser()

login_page = browsers.get("https://github.com/login")
login_form = login_page.soup.select("#login")[0].select("form")[0]

login_form.select("#login_field")[0]['value'] = args.username
login_form.select("#password")[0]['value'] = args.password

page2 = browsers.submit(login_form, login_page.url)

print page2.soup.title
save_object(page2.soup, 'soup.pkl')

messages = page2.soup.find('span', class_='js-select-button css-truncate css-truncate-target')
if messages:
    print(messages.text)

assert page2.soup.select(".logout-form")

print(page2.soup.title.text)

page3 = browsers.get("https://github.com/forgetz")
assert page3.soup.select(".logout-form")