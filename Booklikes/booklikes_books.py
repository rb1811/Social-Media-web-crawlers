import requests
from bs4 import BeautifulSoup

urlStr = 'http://booklikes.com/catalog/13/non-fiction/popular'

book_list= []

# print len(soup.find('div', attrs={'class':'container content'}).find_all('div',attrs={'class':'book-page-review'}))
next_page_url =  urlStr
while True:
	print "This is the next page: " , next_page_url
	response  = requests.get(next_page_url)
	soup = BeautifulSoup(response.content, "lxml")
	for book in soup.find_all('div', attrs={'class':'catalog-books-entry set-rel set-left'}):
			book_list.append(book.find('a')['href'])
	print "len of the book_list till now: " ,len(book_list)
	if 'next' in str(soup.find('div', attrs={'class':'set-text-right'}).find_all('a')):
		for page_link in soup.find('div', attrs={'class':'set-text-right'}).find_all('a'):
			if 'next' in str(page_link):
				next_page_url =  page_link['href']
	else:
		break		

f= open('booklikes_books_urls.txt', 'w')
for ele in book_list:
	f.write(ele)
	f.write(','+'\n')
f.close()

