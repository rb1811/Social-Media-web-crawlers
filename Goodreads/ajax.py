import requests,urllib2,time
from bs4 import BeautifulSoup
from selenium import webdriver
import json

goodreads_url =  'https://www.goodreads.com'
# urlStr =['https://www.goodreads.com/user/5253785-lyn/followers','https://www.goodreads.com/user/6693836-melanie/followers']
urlStr ='https://www.goodreads.com/user/6693836-melanie/followers'

# req = urllib2.Request(url = urlStr)
# response = urllib2.urlopen(req,timeout=10)
# content = response.read()

def getDriver():
	print "adfd"
	driver = webdriver.PhantomJS(executable_path='/usr/local/share/phantomjs/bin/phantomjs')
	urlStr = "https://www.goodreads.com/user/sign_in"

	try:
		driver.get(urlStr)
		time.sleep(0.5)
		driver.find_element_by_id("user_email").send_keys("kai.shu00@gmail.com")
		driver.find_element_by_id("user_password").send_keys("19900327sk")
		login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/form/fieldset/div[5]/input")
		login.click()
	except Exception as e:
		print e.message
	print "something"
	return driver

driver = getDriver()
driver.get(ele)
response = driver.page_source
print response	