import requests
from bs4 import BeautifulSoup
import json

f =open('followers_notfound', 'r')
user_list = []
for line in f:
	if line:
		if line[:-2] not in user_list:
			user_list.append(line[:-2])

user_followers ,followers_list ,done_urls = [],[],{}
g =  open('user_followers.json','r')
for line in g:
	if line:
		done_urls[json.loads(line[:-2]).keys()[0].encode('ascii','ignore')] =  None
g.close()

print "The number of user to be scraped", len(user_list)
print "The number of users already done", len(done_urls)


for urlStr in user_list:
	if urlStr in done_urls:
		# print "This url is done: ", urlStr
		continue

	
	if user_followers:
		print "@@@@@@@@@@@@@@@@@@@@@@@@@"
		print "Writing in batches"
		print "@@@@@@@@@@@@@@@@@@@@@@@@@"

		f  = open('user_followers.json','a')
		for ele in user_followers:
			json.dump(ele,f)
			f.write(','+'\n')
		f.close()
		user_followers = []	


	followers_list = []
	print "This is the current url being scraped: ",urlStr  
	try:
		response  =  requests.get(urlStr)
		soup = BeautifulSoup(response.content, 'lxml')
		if soup.find_all('div',attrs={'class':'follow-name'}):
			for tag in soup.find_all('div',attrs={'class':'follow-name'}):
				followers_list.append(tag.find('a')['href'])
			print "This user has this many followers: ", len(followers_list)
			user_followers.append({urlStr:followers_list})
		else:
			not_found.append(urlStr)
	except Exception as e:
		print "invalid url"
		pass

if user_followers:
	f  = open('user_followers.json','a')
	for ele in user_followers:
		json.dump(ele,f)
		f.write(','+'\n')
	f.close()
	user_followers = []	

