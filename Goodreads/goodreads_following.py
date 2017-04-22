import requests,urllib2,time
from bs4 import BeautifulSoup
from selenium import webdriver
import json

goodreads_url =  'https://www.goodreads.com'
f =  open('test_followers.json', 'r')
all_data,urlStr = [], []
for line in f:
	all_data.append(json.loads(line[:-2]))
for i in range(len(all_data)):
	key =  all_data[i].keys()[0]
	for link in all_data[i][key][0]['user_url']:
		if goodreads_url+link.encode('ascii','ignore').replace('/show','')+'/following' not in urlStr: 
			urlStr.append(goodreads_url+link.encode('ascii','ignore').replace('/show','')+'/following')
f.close()
all_data = []
# /user/show/5253785-lyn
print "Number of urls to be scrapped",len(urlStr)
# urlStr =['https://www.goodreads.com/user/5253785-lyn/following','https://www.goodreads.com/user/6693836-melanie/following', 'https://www.goodreads.com/user/1033675-matt/following']

done_data,done_urls = [], []
k = open('goodreads_following.json','r')
if k:
	print "Some data is there"
	for line in k:
		done_data.append(json.loads(line[:-2]))
	for i in range(len(done_data)):
		done_urls.append(done_data[i].keys()[0].encode('ascii','ignore'))
else:
	print "No data yet"
	pass
k.close()
done_data =[]


def getDriver():
	print "entered driver function"
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
following_dict = []
count = 1
for ele in urlStr:
	text = ele.replace('https://www.goodreads.com','').replace('/following','')
	if text[:text.rfind('/')]+'/show'+text[text.rfind('/'):] in done_urls:
		print "done urlls ", ele
		continue

	print "**************************"
	print "count",count
	print "**************************"
	following_list=[]

	print "This the current url being scrapped " , ele
	
	driver.get(ele)
	# response =  requests.get(ele)
	response = driver.page_source
	soup = BeautifulSoup(response, "lxml")
	
	while 1:
		for link in soup.find_all('a', attrs={"rel" : "acquaintance"}):
			following_list.append(link['href'])
		try:
			next_page_url = soup.find('div', attrs = {'class' :"right"}).find('a',attrs={"class":"next_page"})['href']
			driver.get(goodreads_url+next_page_url)
			response = driver.page_source
			soup = BeautifulSoup(response, "lxml")
			print "The next pageurl ",goodreads_url+next_page_url
		except Exception as e:
			# print e.message
			print "1 page only"
			next_page_url=0

		if next_page_url !=0:
			continue
			# for a_link in soup.find_all('a', attrs={"rel" : "acquaintance"}):
			 	# print a_link['href']
			# 	following_list.append(a_link['href']) 
			# last_page =  int(last_page_url[last_page_url.find('=')+1:])
			# print "The last page is ", last_page
			# for i in range(2,last_page+1):	
			# 	next_page_url = goodreads_url+last_page_url[:last_page_url.find('=')+1]+str(i)
			# 	print next_page_url
			# 	driver.get(next_page_url)
			# 	# response =  requests.get(ele)
			# 	response = driver.page_source
			# 	newsoup = BeautifulSoup(response, "lxml")
			# 	for link in newsoup.find_all('a', attrs={"rel" : "acquaintance"}):
			# 		following_list.append(link['href'])		
			# 	print "Till now following list count",len(following_list)																											
		else:
			# for link in soup.find_all('a', attrs={"rel" : "acquaintance"}):
			# 	following_list.append(link['href'])
			break
			

	print "This person had this many following",len(following_list)
	text = ele.replace('https://www.goodreads.com','').replace('/following','')
	following_dict.append({text[:text.rfind('/')]+'/show'+text[text.rfind('/'):] : following_list})

	if count == 3:
		print "Writing in batches"
		count = 1
		f = open ('goodreads_following.json','a')
		for ele in following_dict:
			json.dump(ele,f)
			f.write(','+'\n')
		f.close()
		following_dict = []
	
	count+=1

if following_dict:
	f = open ('goodreads_following.json','a')
	for ele in following_dict:
		json.dump(ele,f)
		f.write(','+'\n')
	f.close()