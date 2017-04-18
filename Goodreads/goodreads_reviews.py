#r=response.css('div#reviews span.likeItContainer a[rel="nofollow"]::attr(href)').extract() likes
# r=response.css('div.reviewHeader.uitext.stacked').extract() rating ke lie
 # r= response.css('a.user::attr(href)').extract()

import scrapy
from scrapy.selector import Selector
import json
from scrapy.http import Request
class goodreads_reviews(scrapy.Spider):
	name = "goodreads_reviews"
	start_urls =[]
	f=  open('goodreads_book.json','r')
	data  =  json.loads(f.read())
	for i in range(len(data)):
		key = data[i].keys()[0].encode('ascii','ignore')
		temp_arr = []
		temp_arr = data[i][key]['book_urls']
		start_urls.extend(['https://www.goodreads.com'+ ele.encode('ascii', 'ignore') for ele in temp_arr])
	def parse(self, response):
		user_names,user_ratings = [],[]
		user_urls = response.css('a.user::attr(href)').extract()
		for url in user_urls:
			user_names.append(' '.join(url[url.find('-')+1:].split('-')))
		for i in range(len(user_urls)):
			user_urls[i] = 'www.goodreads.com'+user_urls[i].encode('ascii','ignore')
		
		likes_urls = response.css('div#reviews span.likeItContainer a[rel="nofollow"]::attr(href)').extract()
		likes_urls = likes_urls[0::2]

		ratings = response.css('div.reviewHeader.uitext.stacked').extract()
		for rate in ratings:
			if 'it was amazing' in rate.encode('ascii','ignore'):
				user_ratings.append(5)
			elif 'really liked it' in rate.encode('ascii','ignore'):
				user_ratings.append(4)
			elif 'liked it' in rate.encode('ascii','ignore'):
				user_ratings.append(3)
			elif 'it was ok' in rate.encode('ascii','ignore'):
				user_ratings.append(2)
			elif 'did not like it' in rate.encode('ascii','ignore'):
				user_ratings.append(1)
			else:
				user_ratings.append(None)
		data ={
		"user_names" :user_names,
		"user_ratings":user_ratings,
		"likes_urls":likes_urls,
		"user_urls":user_urls
		}
		yield {
		response.url:data
		}
	