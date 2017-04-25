import requests
from bs4 import BeautifulSoup
import json

f =open('booklikes_reviews.json', 'r')
user_list = []
for line in f:
	if line:
		temp_dict =  json.loads(line[:-2])
		key = temp_dict.keys()[0].encode('ascii','ignore')
		for i in range(len(temp_dict[key])):
			if temp_dict[key][i]['user_url'].encode('ascii','ignore')+'/followings' not in user_list: 
				user_list.append( temp_dict[key][i]['user_url'].encode('ascii','ignore')+'/followings' )

user_following ,following_list ,done_urls = [],[],{}
g =  open('user_following.json','r')
for line in g:
	if line:
		done_urls[json.loads(line[:-2]).keys()[0].encode('ascii','ignore')] =  None
g.close()

print "The number of user to be scraped", len(user_list)
print "The number of users already done", len(done_urls)

not_found = []
for urlStr in user_list:
	if urlStr in done_urls:
		print "This url is done: ", urlStr
		continue

	print "@@@@@@@@@@@@@@@@@@@@@@@@@"
	print "Writing in batches"
	print "@@@@@@@@@@@@@@@@@@@@@@@@@"

	if user_following:
		f  = open('user_following.json','a')
		for ele in user_following:
			json.dump(ele,f)
			f.write(','+'\n')
		f.close()
		user_following = []	

		g = open('following_notfound', 'a')
		for ele in not_found:
			g.write(ele)
			g.write(','+'\n')
		g.close()
		not_found = []

	following_list = []
	print "This is the current url being scraped: ",urlStr  
	try:
		response  =  requests.get(urlStr)
		soup = BeautifulSoup(response.content, 'lxml')
		if soup.find('div',attrs={'class':'follow-list'}):
			for tag in soup.find('div',attrs={'class':'follow-list'}).find_all('a'):
				following_list.append(tag['href'])
			print "This user has this many following: ", len(following_list)
			user_following.append({urlStr:following_list})
		else:
			not_found.append(urlStr)
	except Exception as e:
		print "invalid url"
		pass

if user_following:
	f  = open('user_following.json','a')
	for ele in user_following:
		json.dump(ele,f)
		f.write(','+'\n')
	f.close()
	user_following = []	

if not_found:
	g = open('following_notfound', 'a')
	for ele in not_found:
		g.write(ele)
		g.write(','+'\n')
	g.close()
	not_found = []