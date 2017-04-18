import scrapy
from scrapy.selector import Selector
import json
from scrapy.http import HtmlResponse
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
	# start_urls=['https://www.goodreads.com/book/show/1451345.The_Mammoth_Book_Of_Pulp_Fiction?from_search=true','https://www.goodreads.com/book/show/22522808-trigger-warning?from_search=true']
	def parse(self, response):
		user_names,user_ratings,likes_urls = [],[],[]
		user_urls = response.css('a.user::attr(href)').extract()
		for url in user_urls:
			user_names.append(' '.join(url[url.find('-')+1:].split('-')))
		for i in range(len(user_urls)):
			user_urls[i] = 'www.goodreads.com'+user_urls[i].encode('ascii','ignore')
		
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

		temp_likes_urls = response.css('div.left.bodycol').extract()
		for i in range(len(temp_likes_urls)):
			cresponse = HtmlResponse(url ="custom url", body=temp_likes_urls[i].encode('ascii','ignore'))
			if cresponse.css('span.likeItContainer').extract():
				if 'like_count_review' in cresponse.css('span.likeItContainer').extract()[0]:
					likes_urls.append('https://www.goodreads.com'+cresponse.css('span.likeItContainer a[rel="nofollow"]::attr(href)').extract()[0].encode('ascii','ignore'))
				else:
					likes_urls.append(None)
			else:
				likes_urls.append(None)
		data ={
		"user_names" :user_names,
		"user_ratings":user_ratings,
		"likes_urls":likes_urls,
		"user_urls":user_urls
		}
		yield {
		response.url:data
		}
	