import scrapy
import requests
from scrapy.selector import Selector

class live(scrapy.Spider):
    name = "live"
    f= open('all_nodes.txt','r')
    data  = f.readlines()
    start_urls = []
    for link in data:
        if 'livejournal' in link:
            start_urls.append(link)

    def parse(self, response):
        statistics =[]
        heading =  response.css('h1.b-profile-intro-title a::text').extract()[0]
        subheading= response.css('h2.b-profile-intro-subtitle::text').extract()
        if not subheading:
            subheading = None
        else:
            subheading =  subheading[0]
        ###################################################################################################
        givendetails = response.css('div.b-profile-group-row').extract()
        rows = []
        for i in range(len(givendetails)):
            html_string = givendetails[i].encode('ascii','ignore')
            sel = Selector(text = html_string)
            temp_data=[]
            for node in sel.css('div *::text'):
                if not node.extract().encode('ascii','ignore').isspace():
                    # rows.append(node.extract().encode('ascii','ignore'))
                    temp_data.append(node.extract().encode('ascii','ignore'))
            rows.append(temp_data)
        # ####################################################################################################
        stats =  response.css('div.b-profile-stat-main').extract()
        html_string = stats [-1]       
        sel = Selector(text=html_string)
        
        for node in sel.css('ul *::text'):
            if not node.extract().encode('ascii','ignore').isspace():
                statistics.append(node.extract().encode('ascii','ignore'))
        
        

        data = {
        "heading": heading,
        "subheading":subheading,
        "givendetails":rows,
        "statistics":statistics
        }
        username =  response.url[response.url.find('//')+2:response.url.find('.')]
        yield{
        username : data
        }