import json 
f = open('goodreads_book_fiction.json','r')
f1 = open('goodreads_book_classic.json','r')
f2 = open('goodreads_book_nonfiction.json','r')
f3 = open('goodreads_book_romance.json','r')
county = {}

for line in f3:
	try:
		if line:
			temp_dict = json.loads(line[:-2]) 
			key =  temp_dict.keys()[0]
			for url in temp_dict[key]['book_urls']:
				if url not in county:
					county[url]  = None
	except Exception as e:
		pass

print len(county)
for line in f1:
	try:
		if line:
			temp_dict = json.loads(line[:-2]) 
			key =  temp_dict.keys()[0]
			for url in temp_dict[key]['book_urls']:
				if url not in county:
					county[url]  = None
	except Exception as e:
		pass
print len(county)

for line in f:
	try:
		if line:
			temp_dict = json.loads(line[:-2]) 
			key =  temp_dict.keys()[0]
			for url in temp_dict[key]['book_urls']:
				if url not in county:
					county[url]  = None
	except Exception as e:
		pass



print len(county)

for line in f2:
	try:
		if line:
			temp_dict = json.loads(line[:-2]) 
			key =  temp_dict.keys()[0]
			for url in temp_dict[key]['book_urls']:
				if url not in county:
					county[url]  = None
	except Exception as e:
		pass


print len(county)
