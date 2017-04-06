#This spider scraps the nsid for those flickr users whose urls end with usernames and not nsid because for profile details we need nsid  not usernames
import scrapy
import requests
from scrapy.selector import Selector

class flickr_getnsid(scrapy.Spider):
    name = "flickr_getnsid"
    f= open('flickrusernames.txt','r')
    data  = f.readlines()
    start_urls = []
    for link in data:
        start_urls.append(link[:-1])
    def parse(self, response):
        raw_nsid = response.css('div.avatar.no-menu.person.large ::attr(style)').extract()
        nsid = raw_nsid[0].encode('ascii','ignore')
        nsid = nsid[nsid.find('#')+1:nsid.find(')')].encode('ascii','ignore').strip()
        modified_url =  response.url[:-1]
        username =  modified_url[modified_url.rfind('/')+1:]
        yield{
        username : nsid
        }