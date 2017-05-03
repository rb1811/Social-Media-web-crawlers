import requests,urllib2,time
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time
from tqdm import tqdm
first_part='https://www.goodreads.com'
second_part =""
third_part = 'authenticity_token=kgTHED0Aa4Ah1aP93G37AqfQmz%2F5dbCmmPt3IScZ%2B%2BqANzOJw1yw2HGjSepcQHPkjEd0mNQZDjbu81Vsgp%2B1SQ%3D%3D&amp;hide_last_page=true&amp;page='
fourth_part=""
fifth_part= '&authenticity_token=nXQXzqHMY4usRlL%2FBOkVL0DRh5Kfnd35bFcgZcpdk5CPR%2BNXX5C40%2FwwuOiExJ3Ja0ZoNbLxY2kaXwIob9vdMw%3D%3D'
user_reviews = []
header ={
		  	"Accept":"text/javascript, text/html, application/xml, text/xml, */*",
			"Accept-Encoding":"gzip, deflate, sdch, br",
			"Accept-Language":"en-US,en;q=0.8",
			"Connection":"keep-alive",
			"Cookie":"csid=BAhJIhg4NzYtNDc5MTMwNy03MzE3MzMwBjoGRVQ%3D--9015ae6c6997fb0c3dbe115af175567dd8860898; __qca=P0-1986983302-1491770731021; fbm_2415071772=base_domain=.goodreads.com; u=An-NUvgkfF3Ew623eNkUqV9N_hk1KmWjkoJIPgAmSYdHBsTB; p=J4omKhY0N867ks24pDMwMK6ISLLc4pLinD9fYL8eVt0tUqKv; fbl=true; locale=en; csm-sid=293-1514290-6245195; __utma=250562704.2145582756.1491770731.1492210866.1492220542.3; __utmc=250562704; __utmz=250562704.1492210866.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); fbsr_2415071772=Ca5ZyVqCxOC62lWyWIe-GtOEB_Ta0_soRT1k2M7bfvY.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUJjMVR1ZnlJbFFkV2tBMDBxckhRVnN1Umx3aTFkT2IwdmotUXJ0RGp0SWlzWU0tSTYtYndISHdJYUIzaFpMc3lEUXA0Umo5ZFpfMkxVNnlhOWxQazUwLXJtZS1DMUxRcXpIZ05CWjJfVnNKbFhfNnRKUlNuMGpZYlhmWmItNTNJbzAxaDNfVXBtX1ZhNjhzakg2aDBxRmZwMWF0ZHliUXBSLTZHaGlCLUN6MW91aWcyd29MUmUyRXYwSnhGbmFBQVl3Ml9EZ3BSQlNGY2RSbXhadTR6SXk4aFl3WThBODB2S2JTV1FxUW02R1BQMGJEcFo0WFpTYnl6V3VKaGJySVZjYmJ1VklxZFlUMXZMZTlycWdLZ3NkSDEwWWFUMU9kb1V2T1Q5TjFJM1l3TlpOdmJ6MklSWW52amRfU2FlYXJCOS11OHV3Rm5DUDZSdjgwNHA3WGR1RFQtSVFPbDBmQW95RVEtRzhzQzlnS2V6emlDMC1wVWhhY2d2bUtReWNCSDAiLCJpc3N1ZWRfYXQiOjE0OTIyMjMxMTIsInVzZXJfaWQiOiIxMDAwMDM5NjAxMzMwMjQifQ; _session_id2=a35e635abc06c8a3c507d1359bcc8bb6",
			"DNT":"1",
			"Host":"www.goodreads.com",
			"Referer":"https://www.goodreads.com/book/show/14313.Anna_Karenina_by_Leo_Tolstoy_Fiction_Classics_Literary?from_search=true",
			"Related-Request-Id":"7R98YGBNFAAE04228W0Z",
			"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36",
			"X-CSRF-Token":"Sn0ptQxolaW59MyFvmSKLT8L2f7RkGzBYzw6Nm2THXBYTt0s8jRO/emCJpI+SQLLFJw2Wfz80lEVNBh7yBVT0w==",
			"X-Prototype-Version":"1.7",
			"X-Requested-With":"XMLHttpRequest",

	  	}
urlStr = []
g = open('goodreads_book_classic.json','r')
book_data =  json.loads(g.read())
for i in range(len(book_data)):
	key  = book_data[i].keys()[0]
	for link in book_data[i][key]['book_urls']:
		urlStr.append('https://www.goodreads.com'+link)
g.close()
# urlStr =['https://www.goodreads.com/book/show/32487617-beneath-a-scarlet-sky','https://www.goodreads.com/book/show/889430.Microworlds']
print "No of books to be scraped:",len(urlStr)
time.sleep(10)

count=1
done_data,done_urls = [], {}
k = open('user_reviews_classic.json','r')
if k:
	# print "Some data is there"
	for line in k:
		done_data.append(json.loads(line[:-2]))
	for i in range(len(done_data)):
		done_urls[done_data[i].keys()[0].encode('ascii','ignore')]=None
else:
	# print "No data yet"
	pass
k.close()

# print done_urls

for new_book in tqdm(urlStr):
	if new_book in done_urls:
		# print "Done book",new_book
		continue


	# print "**************************"
	# print "count",count
	# print "**************************"
	if count==20:
		count=0
		f = open('user_reviews_classic.json', 'a')
		for ele in user_reviews:
			json.dump(ele,f)
			f.write(','+'\n')
		f.close()
		user_reviews =[]

	user_url, user_names, ratings,likes_url, oldajax_url = [], [],[],[], ""
	# previous_page = 1
	print "This is the current book being scrapped", new_book	
	response =  requests.get(new_book)
	soup = BeautifulSoup(response.content, "lxml")
	try:
		for container in soup.find('div', attrs={'id':'bookReviews'}).find_all('div',attrs={'class':'friendReviews elementListBrown notext'}):
			text = container.text
			if 'rated it' not in text:
				continue
			temp_user_url  = container.find('div',attrs={'class':'reviewHeader uitext stacked'}).find('a')['href'] 
			tmep_user_name = ' '.join(temp_user_url[temp_user_url.find('-')+1:].split('-'))
			user_url.append(temp_user_url)
			user_names.append(tmep_user_name)
			likes_url.append(None)
			if container.find('span',attrs={'class':'staticStars'}).find('span')['title']:
				temp_rate = container.find('span',attrs={'class':'staticStars'}).find('span')['title']
				if 'it was amazing' == temp_rate :
					ratings.append(5)
				elif 'really liked it' == temp_rate:
					ratings.append(4)
				elif 'liked it' == temp_rate:
					ratings.append(3)
				elif 'it was ok' == temp_rate:
					ratings.append(2)
				elif 'did not like it' == temp_rate:
					ratings.append(1)
			else:
				ratings.append(None)
	except Exception as e:
		pass



	review_container = soup.find_all('div',attrs={'class':'friendReviews elementListBrown'})
	for container in review_container:
		text = container.text
		if 'rated it' not in text:
			continue
		for link in container.find_all('a',attrs= {"class":"user"}):
				if link['href']:
					user_url.append(link['href'])
					user_names.append(' '.join(link['href'][link['href'].find('-')+1:].split('-')))
				else:
					user_url.append("None")
					user_names.append("None")

		if container.find('span',attrs={"class":"staticStar"}):
			# print container.find('span',attrs={"class":"staticStar"})
			current_rate =  container.find('span',attrs={"class":"staticStar"})
			if 'it was amazing' == current_rate['title']:
				ratings.append(5)
			elif 'really liked it' == current_rate['title']:
				ratings.append(4)
			elif 'liked it' == current_rate['title']:
				ratings.append(3)
			elif 'it was ok' == current_rate['title']:
				ratings.append(2)
			elif 'did not like it' == current_rate['title']:
				ratings.append(1)
		else:
			# print "None"
			ratings.append(None)


		temp_likes_url = container.find_all('div',attrs={"class":"left bodycol"})
		for ele in temp_likes_url:
			likecontainer  = ele.find('span',attrs={"class":"likeItContainer"})
			if 'like_count_review' in str(likecontainer):
				likes_url.append(likecontainer.find('a')['href'])
			else:
				likes_url.append(None)
	# print ratings
	# print user_url
	# print user_names
	# print likes_url
	# print "#################"
	print "usernames: user_url: ratings:  likes_url ",len(user_names), len(user_url), len(ratings), len(likes_url)
	# print "#################"
	while True:
		# print  previous_page 
		# print "@@@@@@@@@@@@@"
		if not soup.find('a',attrs={"class":"next_page"}):
			break
		next_page = soup.find('a',attrs={"class":"next_page"})['onclick']
		if next_page:
			temp_second_part = next_page[next_page.find("'")+1:next_page.find(',')]
			fourth_part=temp_second_part[temp_second_part.rfind('=')+1:][:-1]
			print "next page ",fourth_part
			second_part = temp_second_part[:temp_second_part.find('?')+1]
			newajax_url =   first_part+second_part+third_part+str(fourth_part)+fifth_part 
			print "############"
			print newajax_url
			print "############"
			# if previous_page != int(fourth_part):
			if newajax_url != oldajax_url:
				# previous_page  = int(fourth_part)
				oldajax_url =  newajax_url 
				response = requests.get(newajax_url,headers=header)
				time.sleep(0.3)
				data = response.content.decode('unicode-escape')
				soup = BeautifulSoup(data, "lxml")
				try:
					for container in soup.find('div', attrs={'id':'bookReviews'}).find_all('div',attrs={'class':'friendReviews elementListBrown notext'}):
						text = container.text
						if 'rated it' not in text:
							continue
						temp_user_url  = container.find('div',attrs={'class':'reviewHeader uitext stacked'}).find('a')['href'] 
						tmep_user_name = ' '.join(temp_user_url[temp_user_url.find('-')+1:].split('-'))
						user_url.append(temp_user_url)
						user_names.append(tmep_user_name)
						likes_url.append(None)
						if container.find('span',attrs={'class':'staticStars'}).find('span')['title']:
							temp_rate = container.find('span',attrs={'class':'staticStars'}).find('span')['title']
							if 'it was amazing' == temp_rate :
								ratings.append(5)
							elif 'really liked it' == temp_rate:
								ratings.append(4)
							elif 'liked it' == temp_rate:
								ratings.append(3)
							elif 'it was ok' == temp_rate:
								ratings.append(2)
							elif 'did not like it' == temp_rate:
								ratings.append(1)
						else:
							ratings.append(None)
				except Exception as e:
					pass


				review_container = soup.find_all('div',attrs={'class':'friendReviews elementListBrown'})
				for container in review_container:
					text = container.text
					if 'rated it' not in text:
						continue
					for link in container.find_all('a',attrs= {"class":"user"}):
							if link['href']:
								user_url.append(link['href'])
								user_names.append(' '.join(link['href'][link['href'].find('-')+1:].split('-')))
							else:
								user_url.append("None")
								user_names.append("None")

					if container.find('span',attrs={"class":"staticStar"}):
						# print container.find('span',attrs={"class":"staticStar"})
						current_rate =  container.find('span',attrs={"class":"staticStar"})
						if 'it was amazing' == current_rate['title']:
							ratings.append(5)
						elif 'really liked it' == current_rate['title']:
							ratings.append(4)
						elif 'liked it' == current_rate['title']:
							ratings.append(3)
						elif 'it was ok' == current_rate['title']:
							ratings.append(2)
						elif 'did not like it' == current_rate['title']:
							ratings.append(1)
					else:
						# print "None"
						ratings.append(None)

					temp_likes_url = container.find_all('div',attrs={"class":"left bodycol"})
					for ele in temp_likes_url:
						likecontainer  = ele.find('span',attrs={"class":"likeItContainer"})
						if 'like_count_review' in str(likecontainer):
							# print likecontainer.find('a')['href']
							likes_url.append(likecontainer.find('a')['href'])
						else:
							# print "None"
							likes_url.append(None)
				# print "&&&&&&&&&&&&&&&&&&&"
				print "usernames: user_url: ratings:  likes_url ",len(user_names), len(user_url), len(ratings), len(likes_url)
				# print "&&&&&&&&&&&&&&&&&&&"
	
			else:
				break
		else:
			break
	temp_dict={}
	user_reviews.append(
			{
				new_book:[
				{"user_url":user_url},
				{"ratings" : ratings},
				{"user_names": user_names},
				{"likes_url": likes_url}

						]
			} 

		)
	count+=1
if user_reviews:
	f = open('user_reviews_classic.json', 'a')
	for ele in user_reviews:
		json.dump(ele,f)
		f.write(','+'\n')
	f.close()		