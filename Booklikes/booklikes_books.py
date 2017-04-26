import requests
from bs4 import BeautifulSoup
import json

# urlStr = 'http://booklikes.com/catalog/13/non-fiction/popular'

domain_url  =  "http://booklikes.com/catalog/list"
response = requests.get(domain_url)
soup = BeautifulSoup(response.content,'lxml')
category_list,done_cat = [],{}

for book_cat in soup.find_all('td'):
	category_list.append( {book_cat.find('a').string.encode('ascii','ignore') : {book_cat.find('a')['href'] : []} }  )

print "Total book categories", len(category_list)

# print category_list

f = open('booklikes_category.json', 'r')
for line in f:
	if line:
		done_category=  json.loads(line[:-2]).keys()[0].encode('ascii','ignore')
		done_cat[done_category]  = None

book_list= []

for i in range(len(category_list)):
	cat_name = category_list[i].keys()[0]
	if cat_name in done_cat:
		print "This category is already done: ", cat_name
		continue

	cat_url  = category_list[i][cat_name].keys()[0]

	urlStr =  cat_url+'/all'
	
	print "###############"
	print "This the current category: ", urlStr
	print "###############"

	next_page_url =  urlStr
	while True:
		print "This is the next page: " , next_page_url
		response  = requests.get(next_page_url)
		soup = BeautifulSoup(response.content, "lxml")
		for book in soup.find_all('div', attrs={'class':'catalog-books-entry set-rel set-left'}):
				book_list.append(book.find('a')['href'])
		print "len of the book_list till now: " ,len(book_list)
		try:
			if 'next' in str(soup.find('div', attrs={'class':'set-text-right'}).find_all('a')):
				for page_link in soup.find('div', attrs={'class':'set-text-right'}).find_all('a'):
					if 'next' in str(page_link):
						next_page_url =  page_link['href']
			else:
				break
		except Exception as e:
			pass

	category_list[i][cat_name][cat_url].extend(book_list)


	f =  open('booklikes_category.json', 'a')
	json.dump(category_list[i],f)
	f.write(','+'\n')
	f.close()

	f= open('booklikes_books_urls.txt', 'a')
	for ele in book_list:
		f.write(ele)
		f.write(','+'\n')
	f.close()
	book_list =[]




