import scrapy
# import json	
# import requests
import time
# from scrapy.selector import Selector

class booklikes_meta(scrapy.Spider):
	name = "booklikes_meta"
	book_urls = {}
	f =open('/home/prabhat/Downloads/pj/Booklikes/booklikes_books_urls.txt', 'r')
	for line in f:
		try:
			if line and line[:-2] not in book_urls:
				book_urls[line[:-2].encode('ascii','ignore')] = 1
		except Exception as e:
			pass
	# start_urls = ['http://booklikes.com/the-kingmaker-s-daughter-philippa-gregory/book,12341674']
	start_urls = book_urls.keys()
	print len(start_urls)
	time.sleep(5)
	def parse(self, response):
		book_title,author,avg_rating,desc = "","",None,""
		try:
			book_title =  response.css('div[class= "book-page-title"]::text').extract()[0].encode('ascii','ignore')
		except Exception as e:
			pass
		try:
			author =  response.css('div[class= "book-page-author"] strong span[itemprop="name"]::text').extract()[0].encode('ascii','ignore')
		except Exception as e:
			pass
		try:
			avg_rating = response.css('div[class= "book-page-author"] div[class="set-hide"] span[itemprop="ratingValue"]::text').extract()[0].encode('ascii','ignore').strip()
		except Exception as e:
			pass
		try:	
			desc = response.css('div[class= "book-page-desc"]::text').extract()[0].encode('ascii','ignore')
		except Exception as e:
			pass
		data = {}
		data = {
		"book_title" : book_title,
		"author"  : author,
		"avg_rating" : avg_rating,
		"desc":desc
		}
		yield{
			response.url  : data
			}