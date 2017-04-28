import requests, urllib2, time
from bs4 import BeautifulSoup
from selenium import webdriver
import json
from tqdm import tqdm

output_file = 'goodreads_followers3.json'

goodreads_url = 'https://www.goodreads.com'
f = open('user_reviews_fiction.json', 'r')
all_data, urlStr = [], {}
for line in f:
    all_data.append(json.loads(line[:-2]))
f1 = open('user_reviews_nonfiction.json', 'r')
for line in f1:
    all_data.append(json.loads(line[:-2]))
f2 = open('user_reviews_classic.json', 'r')
for line in f2:
    all_data.append(json.loads(line[:-2]))
for i in range(len(all_data)):
    key = all_data[i].keys()[0]
    for link in all_data[i][key][0]['user_url']:
        if goodreads_url + link.encode('ascii', 'ignore').replace('/show', '') + '/followers' not in urlStr:
            urlStr[goodreads_url + link.encode('ascii', 'ignore').replace('/show', '') + '/followers'] = 1
f.close()
all_data = []
# /user/show/5253785-lyn
print "Number of urls to be scrapped", len(urlStr)
# urlStr =['https://www.goodreads.com/user/5253785-lyn/followers','https://www.goodreads.com/user/6693836-melanie/followers']

done_data,done_urls = [], {}
k = open('goodreads_followers.json','r')
if k:
	# print "Some data is there"
	for line in k:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k.close()

k3 = open('goodreads_followers3.json','r')
if k3:
	# print "Some data is there"
	for line in k3:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k3.close()

done_data =[]


def getDriver():
    # print "entered driver function"
    driver = webdriver.PhantomJS(
        executable_path='C:\\Users\\skai2\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    urlStr = "https://www.goodreads.com/user/sign_in"

    try:
        driver.get(urlStr)
        time.sleep(0.5)
        driver.find_element_by_id("user_email").send_keys("kai.shu00@gmail.com")
        driver.find_element_by_id("user_password").send_keys("19900327sk")
        login = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/form/fieldset/div[5]/input")
        login.click()
    except Exception as e:
        print e.message
    return driver


driver = getDriver()
followers_dict = []

all_urls_list = urlStr.keys()
count = 1
reamining_url_list = []
for ele in all_urls_list[60001:80000]:
    text = ele.replace('https://www.goodreads.com', '').replace('/followers', '')
    if text[:text.rfind('/')] + '/show' + text[text.rfind('/'):] in done_urls:
        continue
    reamining_url_list.append(ele)

for ele in tqdm(reamining_url_list):
    text = ele.replace('https://www.goodreads.com', '').replace('/followers', '')
    if text[:text.rfind('/')] + '/show' + text[text.rfind('/'):] in done_urls:
        # print "done urlls ", ele
        continue

    # print "**************************"
    # print "count",count
    # print "**************************"
    followers_list = []

    # print "This the current url being scrapped " , ele

    driver.get(ele)
    # response =  requests.get(ele)
    response = driver.page_source
    soup = BeautifulSoup(response, "lxml")
    try:
        last_page_url = soup.find('div', attrs={'style': "text-align: right"}).find_all('a')[-2]['href']
    except Exception as e:
        # print e.message
        # print "1 page followers"
        last_page_url = 0

    if last_page_url != 0:
        for a_link in soup.find_all('a', attrs={"rel": "acquaintance"}):
            followers_list.append(a_link['href'])
        last_page = int(last_page_url[last_page_url.find('=') + 1:])
        if last_page > 100:
            last_page = 100
        # print "The last page is ", last_page
        for i in range(2, last_page + 1):
            next_page_url = goodreads_url + last_page_url[:last_page_url.find('=') + 1] + str(i)
            # print next_page_url
            driver.get(next_page_url)
            # response =  requests.get(ele)
            response = driver.page_source
            newsoup = BeautifulSoup(response, "lxml")
            for link in newsoup.find_all('a', attrs={"rel": "acquaintance"}):
                followers_list.append(link['href'])
            # print "Till now followers list count",len(followers_list)
    else:
        for link in soup.find_all('a', attrs={"rel": "acquaintance"}):
            followers_list.append(link['href'])
    text = ele.replace('https://www.goodreads.com', '').replace('/followers', '')
    followers_dict.append({text[:text.rfind('/')] + '/show' + text[text.rfind('/'):]: followers_list})

    if count == 5:
        # print "Wrrting in batches"
        count = 1
        f = open(output_file, 'a')
        for ele in followers_dict:
            json.dump(ele, f)
            f.write(',' + '\n')
        f.close()
        followers_dict = []

    count += 1

if followers_dict:
    f = open(output_file, 'a')
    for ele in followers_dict:
        json.dump(ele, f)
        f.write(',' + '\n')
    f.close()