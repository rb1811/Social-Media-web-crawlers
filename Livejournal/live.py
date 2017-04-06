#You need scrapy package in your system to run this code 
# If you have it this is the command :scrapy crawl <spidername> -o <json file name> -t json
#For the code purpose give json file name as live.json in the above command so that livejournal_modified.py code can read this json file and make it mongodb compatible
import scrapy
import requests
from scrapy.selector import Selector

class live(scrapy.Spider):
    name = "live"
    f= open('all_nodes.txt','r') #Read the urls and seprate out all the urls that have livejournal keyword in it. And store them in the start_urls
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
        #######################################Fetch the basic details that you need ############################################################
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
        # ##########################################Fetch the statistics ##########################################################
        stats =  response.css('div.b-profile-stat-main').extract()
        html_string = stats [-1]       
        sel = Selector(text=html_string)
        
        for node in sel.css('ul *::text'):
            if not node.extract().encode('ascii','ignore').isspace():
                statistics.append(node.extract().encode('ascii','ignore'))
        
        
        #Create an almost proper json structure 
        data = {
        "heading": heading,
        "subheading":subheading,
        "givendetails":rows,
        "statistics":statistics
        }
        #get the username from the url by doing some basic string manipulation
        username =  response.url[response.url.find('//')+2:response.url.find('.')]
        yield{
        username : data
        }