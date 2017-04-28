import scrapy
import json	
import requests
import time
class booklikes_followers(scrapy.Spider):
	name = "booklikes_followers"
	user_urls = {}
	f =open('/home/prabhat/Downloads/pj/Booklikes/booklikes_reviews.json', 'r')
	f2 =open('/home/prabhat/Downloads/pj/Booklikes/booklikes_reviews2.json', 'r')
	f3 =open('/home/prabhat/Downloads/pj/Booklikes/booklikes_reviews3.json', 'r')
	
	for line in f:
		try:
			if line:
				temp_dict =  json.loads(line[:-2])
				key = temp_dict.keys()[0].encode('ascii','ignore')
				for i in range(len(temp_dict[key])):
					if temp_dict[key][i]['user_url'].encode('ascii','ignore')+'/followers' not in user_urls: 
						user_urls[ temp_dict[key][i]['user_url'].encode('ascii','ignore')+'/followers' ]=1
		except Exception as e:
			pass
	for line in f2:
		try:
			if line:
				temp_dict =  json.loads(line[:-2])
				key = temp_dict.keys()[0].encode('ascii','ignore')
				for i in range(len(temp_dict[key])):
					if temp_dict[key][i]['user_url'].encode('ascii','ignore')+'/followers' not in user_urls: 
						user_urls[ temp_dict[key][i]['user_url'].encode('ascii','ignore')+'/followers' ]=1
		except Exception as e:
			pass
	for line in f3:
		try:
			if line:
				temp_dict =  json.loads(line[:-2])
				key = temp_dict.keys()[0].encode('ascii','ignore')
				for i in range(len(temp_dict[key])):
					if temp_dict[key][i]['user_url'].encode('ascii','ignore')+'/followers' not in user_urls: 
						user_urls[temp_dict[key][i]['user_url'].encode('ascii','ignore')+'/followers' ]=1
		except Exception as e:
			pass
	# start_urls = ['http://SelfProfessedBookHoarders.booklikes.com/followers']
	start_urls = user_urls.keys()
	print len(start_urls)
	time.sleep(15)

	def parse(self, response):
		followers_list=response.css('div[class = "follow-list"] a::attr(href)').extract()
		for i in range(len(followers_list)):
			followers_list[i] = followers_list[i].encode('ascii','ignore')

		newurl = response.url.replace('/followers','')
		yield{
			newurl  : followers_list
			}