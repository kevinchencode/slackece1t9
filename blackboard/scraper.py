import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import sys, logging

logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)

#br.set_debug_http(True)
#br.set_debug_responses(True)
#br.set_debug_redirects(True)

#general headers for header spoofing
general_headers = {"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
 "Accept-Encoding" : "gzip, deflate, sdch, br",
 "Connection" : "keep-alive",
 "Upgrade-Insecure-Requests" : "1",
 "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
 "Referer" : "https://www.google.ca/",
 "Accept-Language" : "en-US,en;q=0.8"
 }

#go to blackboard
br.open("https://portal.utoronto.ca/")
print "\n\n"
for link in br.links():
	if link.text == "Login":
		#follows link to login screen
		br.follow_link(link)

#submits a javascript form that sends you to login page
br.select_form(nr=0)
br.submit()
with open("login.html", "w") as w:
	w.write(br.response().read())
br.select_form(nr=0)
br.form['user'] = 'chenka24' #should be environment variables
br.form['pass'] = 'R7362L58' #same
response = br.submit()
with open("blackboard.html", "w") as w:
	w.write(response.read())




'''
soup = BeautifulSoup(br.response().read(), from_encoding=br.respone.info().getparam("charset"))
print soup.find("").text

print "\n\n"

print br.geturl()

print "\n\n"
'''
#with open("")

"""
#Connect to uoft login (grabs login cookie) This is a 10 hour login
br.open("https://portal.utoronto.ca/webapps/login")
br.select_form(nr=0)
br.form['user'] = 'chenka24' #should be environment variables
br.form['pass'] = 'R7362L58' #same
with open("login.html", "w") as w:
	w.write(br.response().read())
br.submit()


#go to portal site
br.open("https://portal.utoronto.ca/")
with open("bb1.html", "w") as w:
	w.write(br.response().read())
for cookie in cj:
	print cookie.name, cookie.value

#Connects to blackboard itself
br.open("https://portal.utoronto.ca/")
redirect = br.click_link(text="Login")
#print redirect.header_items()
br.open(redirect)
with open("blackboard.html", "w") as w:
	w.write(br.response().read())
"""