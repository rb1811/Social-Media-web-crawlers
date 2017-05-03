import scrapy	
from scrapy.selector import Selector
import time
from scrapy.http import Request
class goodreads_book(scrapy.Spider):
	name = "goodreads_book"
	# start_urls =['https://www.goodreads.com/search?q=fiction+']
	# start_urls = ['https://www.goodreads.com/search?q=nonfiction']
	# start_urls =['https://www.goodreads.com/search?q=classic']
	start_urls =['https://www.goodreads.com/search?q=romance']
	base_url = 'https://www.goodreads.com/search?page=&q=romance+&tab=books'
	def parse(self, response):
	  	total_pages = response.css('div.leftContainer div:nth-child(10) a::text').extract()
	  	last_page  = total_pages[-2].encode('ascii','ignore')
	  	for i in range(1,int(last_page)+1):
	  		new_url = self.base_url[:self.base_url.find('=')+1]+str(i)+self.base_url[self.base_url.find('=')+1:] 
	  		req = Request(new_url,callback = self.parse_page)
			yield req

	def parse_page(self, response):
		all_authors = []
		book_titles= response.css('a.bookTitle span[itemprop="name"]::text').extract()
		book_urls= response.css('a.bookTitle ::attr(href)').extract()
		authors= response.css('span[itemprop="author"]').extract()
		for i in range(len(authors)):
			temp_arr = []
			html_string = authors[i]
			sel =  Selector(text=html_string)
			for node in sel.css('span *::text'):
				if not node.extract().encode('ascii','ignore').strip().isspace():
					if node.extract().encode('ascii','ignore') not in ('(Goodreads Author)',  '\n'   , ', '   ,   ', \n'   ,   ' '):
						temp_arr.append(node.extract().encode('ascii','ignore'))
			all_authors.append(temp_arr)
		ratings= response.css('span.minirating::text').extract()
		page_number = response.url[response.url.find('=')+1:response.url.find('&')-1]
		data ={}
		data ={
		"book_titles":book_titles,
		"book_urls":book_urls,
		"authors" : all_authors,
		"ratings":ratings,
		} 
		yield {
		page_number : data
		}
	