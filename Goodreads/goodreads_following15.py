import requests, urllib2, time
from bs4 import BeautifulSoup
from selenium import webdriver
import json
from tqdm import tqdm

output_file = 'goodreads_following15.json'

goodreads_url = 'https://www.goodreads.com'
all_data, urlStr = [], {}

f = open('user_reviews_fiction.json', 'r')
for line in f:
    all_data.append(json.loads(line[:-2]))
f1 = open('user_reviews_nonfiction.json', 'r')
for line in f1:
    all_data.append(json.loads(line[:-2]))
f2 = open('user_reviews_classic.json', 'r')
for line in f2:
    all_data.append(json.loads(line[:-2]))
f3 = open('user_reviews_romance.json', 'r')
for line in f3:
    all_data.append(json.loads(line[:-2]))

for i in range(len(all_data)):
    key = all_data[i].keys()[0]
    for link in all_data[i][key][0]['user_url']:
        if goodreads_url + link.encode('ascii', 'ignore').replace('/show', '') + '/following' not in urlStr:
            urlStr[goodreads_url + link.encode('ascii', 'ignore').replace('/show', '') + '/following'] = 1
f1.close()
f2.close()
f3.close()
f.close()
all_data = []
# /user/show/5253785-lyn
print "Number of urls to be scrapped", len(urlStr)
# urlStr =['https://www.goodreads.com/user/5253785-lyn/following','https://www.goodreads.com/user/6693836-melanie/following', 'https://www.goodreads.com/user/1033675-matt/following']

done_data, done_urls = [], {}
k = open('goodreads_following.json', 'r')
if k:
    # print "Some data is there"
    for line in k:
        try:
            done_data.append(json.loads(line[:-2]))
        except:
            pass
    for i in range(len(done_data)):
        done_urls[done_data[i].keys()[0].encode('ascii', 'ignore')] = 1
else:
    # print "No data yet"
    pass
k.close()

k1 = open('goodreads_following1.json', 'r')
if k1:
    # print "Some data is there"
    for line in k1:
        try:
            done_data.append(json.loads(line[:-2]))
        except:
            pass
    for i in range(len(done_data)):
        done_urls[done_data[i].keys()[0].encode('ascii', 'ignore')] = 1
else:
    # print "No data yet"
    pass
k1.close()

k2 = open('goodreads_following2.json', 'r')
if k2:
    # print "Some data is there"
    for line in k2:
        try:
            done_data.append(json.loads(line[:-2]))
        except:
            pass
    for i in range(len(done_data)):
        done_urls[done_data[i].keys()[0].encode('ascii', 'ignore')] = 1
else:
    # print "No data yet"
    pass
k2.close()

k3 = open('goodreads_following3.json', 'r')
if k3:
    # print "Some data is there"
    for line in k3:
        try:
            done_data.append(json.loads(line[:-2]))
        except:
            pass
    for i in range(len(done_data)):
        done_urls[done_data[i].keys()[0].encode('ascii', 'ignore')] = 1
else:
    # print "No data yet"
    pass
k3.close()

k4 = open('goodreads_following4.json', 'r')
if k4:
    # print "Some data is there"
    for line in k4:
        try:
            done_data.append(json.loads(line[:-2]))
        except:
            pass
    for i in range(len(done_data)):
        done_urls[done_data[i].keys()[0].encode('ascii', 'ignore')] = 1
else:
    # print "No data yet"
    pass
k4.close()

k5 = open('goodreads_following_roman.json', 'r')
if k5:
    # print "Some data is there"
    for line in k5:
        try:
            done_data.append(json.loads(line[:-2]))
        except:
            pass
    for i in range(len(done_data)):
        done_urls[done_data[i].keys()[0].encode('ascii', 'ignore')] = 1
else:
    # print "No data yet"
    pass
k5.close()


#############################################################################################
k6 = open('goodreads_following6.json','r')
if k6:
	# print "Some data is there"
	for line in k6:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k6.close()


k7 = open('goodreads_following7.json','r')
if k7:
	# print "Some data is there"
	for line in k7:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k7.close()

k8 = open('goodreads_following8.json','r')
if k8:
	# print "Some data is there"
	for line in k8:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k8.close()

k9 = open('goodreads_following9.json','r')
if k9:
	# print "Some data is there"
	for line in k9:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k9.close()

k10 = open('goodreads_following10.json','r')
if k10:
	# print "Some data is there"
	for line in k10:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k10.close()

k11 = open('goodreads_following11.json','r')
if k11:
	# print "Some data is there"
	for line in k11:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k11.close()

k12 = open('goodreads_following12.json','r')
if k12:
	# print "Some data is there"
	for line in k12:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k12.close()

k13 = open('goodreads_following13.json','r')
if k13:
	# print "Some data is there"
	for line in k13:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k13.close()

k14 = open('goodreads_following14.json','r')
if k14:
	# print "Some data is there"
	for line in k14:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k14.close()

k15 = open('goodreads_following15.json','r')
if k15:
	# print "Some data is there"
	for line in k15:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k15.close()

k1 = open('goodreads_following1.json','r')
if k1:
	# print "Some data is there"
	for line in k1:
		try:
			done_data.append(json.loads(line[:-2]))
		except:
			pass
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=1
else:
	# print "No data yet"
	pass
k1.close()


##############################################################################################

done_data = []


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
following_dict = []
count = 1
all_urls_list = urlStr.keys()
remain_list = []
for ele in tqdm(all_urls_list):
    text = ele.replace('https://www.goodreads.com', '').replace('/following', '')
    if text[:text.rfind('/')] + '/show' + text[text.rfind('/'):] in done_urls:
        continue
    remain_list.append(ele)

for ele in tqdm(remain_list[25001:50000]):

    # print "**************************"
    # print "count",count
    # print "**************************"
    following_list = []

    # print "This the current url being scrapped " , ele

    driver.get(ele)
    # response =  requests.get(ele)
    response = driver.page_source
    soup = BeautifulSoup(response, "lxml")

    while 1:
        for link in soup.find_all('a', attrs={"rel": "acquaintance"}):
            following_list.append(link['href'])
        try:
            next_page_url = soup.find('div', attrs={'class': "right"}).find('a', attrs={"class": "next_page"})['href']
            driver.get(goodreads_url + next_page_url)
            response = driver.page_source
            soup = BeautifulSoup(response, "lxml")
        # print "The next pageurl ",goodreads_url+next_page_url
        except Exception as e:
            # print e.message
            # print "1 page only"
            next_page_url = 0

        if next_page_url != 0:
            continue
        # for a_link in soup.find_all('a', attrs={"rel" : "acquaintance"}):
        # print a_link['href']
        # 	following_list.append(a_link['href'])
        # last_page =  int(last_page_url[last_page_url.find('=')+1:])
        # print "The last page is ", last_page
        # for i in range(2,last_page+1):
        # 	next_page_url = goodreads_url+last_page_url[:last_page_url.find('=')+1]+str(i)
        # 	print next_page_url
        # 	driver.get(next_page_url)
        # 	# response =  requests.get(ele)
        # 	response = driver.page_source
        # 	newsoup = BeautifulSoup(response, "lxml")
        # 	for link in newsoup.find_all('a', attrs={"rel" : "acquaintance"}):
        # 		following_list.append(link['href'])
        # 	print "Till now following list count",len(following_list)
        else:
            # for link in soup.find_all('a', attrs={"rel" : "acquaintance"}):
            # 	following_list.append(link['href'])
            break

    # print "This person had this many following",len(following_list)
    text = ele.replace('https://www.goodreads.com', '').replace('/following', '')
    following_dict.append({text[:text.rfind('/')] + '/show' + text[text.rfind('/'):]: following_list})

    if count == 3:
        # print "Writing in batches"
        count = 1
        f = open(output_file, 'a')
        for ele in following_dict:
            json.dump(ele, f)
            f.write(',' + '\n')
        f.close()
        following_dict = []

    count += 1

if following_dict:
    f = open(output_file, 'a')
    for ele in following_dict:
        json.dump(ele, f)
        f.write(',' + '\n')
    f.close()