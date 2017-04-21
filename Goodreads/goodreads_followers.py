import requests,urllib2,time
from bs4 import BeautifulSoup
from selenium import webdriver
import json

goodreads_url =  'https://www.goodreads.com'
urlStr =['https://www.goodreads.com/user/5253785-lyn/followers','https://www.goodreads.com/user/6693836-melanie/followers']
# urlStr ='https://www.goodreads.com/user/6693836-melanie/followers'

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
	return driver

driver = getDriver()
followers_dict ={}

for ele in urlStr:
	followers_list=[]
	driver.get(ele)
	response = driver.page_source
	soup = BeautifulSoup(response, "lxml")
	try:
		last_page_url = soup.find('div', attrs = {'style' :"text-align: right"}).find_all('a')[-2]['href']
	except Exception as e:
		# print e.message
		print "1 page followers"
		last_page_url=0

	if last_page_url !=0:
		for a_link in soup.find_all('a', attrs={"rel" : "acquaintance"}):
			followers_list.append(a_link['href'])
		last_page =  int(last_page_url[last_page_url.find('=')+1:])
		print last_page
		# for i in range(2,last_page+1):
		for i in range(2,4):	
			next_page_url = goodreads_url+last_page_url[:last_page_url.find('=')+1]+str(i)
			print next_page_url
			driver.get(next_page_url)
			response = driver.page_source
			newsoup = BeautifulSoup(response, "lxml")
			for link in newsoup.find_all('a', attrs={"rel" : "acquaintance"}):
				followers_list.append(link['href'])		
			print len(followers_list)																											
	else:
		for link in soup.find_all('a', attrs={"rel" : "acquaintance"}):
			followers_list.append(link['href'])
	followers_dict.update({ele:followers_list})
final_data=[]
final_data.append(followers_dict)
f = open ('goodreads_followers.json','w')
for ele in final_data:
	json.dump(ele,f)
	f.write(','+'\n')
f.close()