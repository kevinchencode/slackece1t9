import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://www.example.com")
br.open("https://en.wikipedia.org/wiki/Main_Page")

response = br.back()

print response.geturl()