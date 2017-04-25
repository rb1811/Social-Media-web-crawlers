import requests
from bs4 import BeautifulSoup

f =  open('booklikes_books_urls.txt','r')
book_list = []
for line in f:
	if line:
		book_list.append(line[:-2]+'/reviews')

reviews = []

book_list = []
book_list.append('http://booklikes.com/trigger-warning-short-fictions-and-disturbances-neil-gaiman/book,12993075/reviews')

for urlStr in book_list:
	response =  requests.get(urlStr)
	soup =  BeautifulSoup(response.content, 'lxml')
	for rev in soup.find('div', attrs={'class':'container content'}).find_all('div',attrs={'class':'book-page-review'}):
		full_star,half_star  = 0,0
		user_url = rev.find('div',attrs = {'class':'book-page-review-user'}).find('a')['href']
		user_name  = rev.find('div',attrs = {'class':'book-page-review-user'}).find('a').string

 		for tag in 	rev.find_all('span'):
 			if 'star' in str(tag):
 				for star_img in tag.find_all('img'):
 					if 'star_a' in star_img['src']:
 						full_star+=1
 					elif 'star_h' in star_img['src']:
 						half_star+=1
 					else:
 						pass
 			else:
 				pass
 		rating = full_star + 0.5*half_star
 		reviews.append({"name" : user_name, "user_url":user_url, "rating": rating})


# http://booklikes.com/the-shadow-of-the-wind-lucia-graves-carlos-ruiz-zafon/book,17306/reviews
# http://booklikes.com/murder-of-crows-the-twenty-sided-sorceress-book-2-annie-bellet/book,12910512
# http://booklikes.com/trigger-warning-short-fictions-and-disturbances-neil-gaiman/book,12993075/reviews&p=1
# http://booklikes.com/trigger-warning-short-fictions-and-disturbances-neil-gaiman/book,12993075/reviews&p=0