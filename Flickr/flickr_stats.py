import scrapy
import requests
from scrapy.selector import Selector

class flickr(scrapy.Spider):
    name = "flickr"
    f= open('all_nodes.txt','r')
    data  = f.readlines()
    start_urls = []
    for link in data:
        if 'flickr' in link:
            start_urls.append(link[:-1])
    def parse(self, response):
        followers,following,photos =0,0,0
        followers_following_call = response.css('div.title-block-content').extract()
        html_string = followers_following_call[0]
        sel =  Selector(text=html_string)
        for node in sel.css('div *::text'):
            if not node.extract().encode('ascii','ignore').isspace():
                if 'Followers' in node.extract().encode('ascii','ignore'):
                    text= node.extract().encode('ascii','ignore')
                    followers = text[:text.find(' ')]
                if 'Following' in node.extract().encode('ascii','ignore'):
                    text= node.extract().encode('ascii','ignore')
                    following = text[:text.find(' ')]
        
        photos_call =response.css('div.metadata-content').extract()
        html_string =  photos_call[0]
        sel = Selector(text=html_string)
        for node in sel.css('div *::text'):
            if not node.extract().encode('ascii','ignore').isspace():
                 if 'Photos' in node.extract().encode('ascii','ignore'):
                    text= node.extract().encode('ascii','ignore')
                    photos = text[:text.find(' ')]        

        
        data = {
        "followers": followers,
        "following":followers,
        "photos":followers
        }
        modified_url =  response.url[:-1]
        username =  modified_url[modified_url.rfind('/')+1:]
        yield{
        username : data
        }