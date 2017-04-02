import json
f =  open('live.json','r')
data_json  =  json.load(f)
print len(data_json)
for i in range(len(data_json)):
	temp_stat = {}
	username = data_json[i].keys()[0].encode('ascii','ignore')
	for j in range(  0,  len(data_json[i][username]['statistics']), 2  ):
		key = data_json[i][username]['statistics'][j+1].encode('ascii','ignore')
		value = data_json[i][username]['statistics'][j].encode('ascii','ignore')
		temp_stat[key] = value
	data_json[i][username]['statistics'] = {}
	data_json[i][username]['statistics'] = temp_stat

	temp_details={}
	for j in range(len(data_json[i][username]['givendetails'])): 
		key = data_json[i][username]['givendetails'][j][0].encode('ascii','ignore')
		value =  ''.join([e.encode('ascii','ignore').strip()+' ' for e in data_json[i][username]['givendetails'][j][1:]])
		temp_details[key] =  value

	data_json[i][username]['givendetails']={}
	data_json[i][username]['givendetails'] = temp_details
	print i
g = open('modified_live.json','w')
for data in data_json:
	g.write(str(data)+'\n')
g.close()
