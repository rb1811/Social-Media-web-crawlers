# This spider is for crawling all links that are present in the about page of any Youtube user 
import scrapy
import requests
from scrapy.selector import Selector

class linkyoutube(scrapy.Spider):
    name = "linkyoutube"
    f= open('all_nodes.txt','r') #Read the urls and seprate out all the urls that have youtube keyword in it. And store them in the start_urls
    data  = f.read()
    data =  data.split('\n')
    start_urls = []
    for link in data:
        if 'youtube' in link:
            start_urls.append(link+'/about')

    def parse(self, response):
        all_links = []
        links= response.css('ul.about-custom-links li.channel-links-item a::attr(href)').extract()[1:]# Skip the 0th entry. Because the 0th and 1st entry are basically same 
        for ele in links:
            all_links.append(ele.encode('ascii','ignore').strip())
        
        data = {
        "links": all_links
        }
        #get the username from the url by doing some basic string manipulation
        username =response.url[response.url.find('user/')+5:response.url.find('/about')]
        yield{
        username : data
        }