import argparse
import mechanicalsoup
import cPickle as pickle

def save_object(obj, filename):
        with open(filename, 'a') as output:
                pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def readpkl(filename):
	data = pickle.load(open(filename,"rb"))
	output = open("write.txt","w")
	output.write(str(data))
	output.flush()
	output.close()

parser = argparse.ArgumentParser(description='Login to FURS (TEST)')
parser.add_argument("username")
parser.add_argument("password")
args = parser.parse_args()

browsers = mechanicalsoup.Browser()

login_page = browsers.get("http://10.10.150.187:10002/login.aspx")
login_form = login_page.soup.select("form")[0]

login_form.select("#txtusrname")[0]['value'] = args.username
login_form.select("#txtpwd")[0]['value'] = args.password

#print login_form

print login_page.url

page2 = browsers.submit(login_form, login_page.url)

#print page2.soup
print "----------------------------"


print page2.soup.title
save_object(page2.soup, 'soup.pkl')
readpkl('soup.pkl')
