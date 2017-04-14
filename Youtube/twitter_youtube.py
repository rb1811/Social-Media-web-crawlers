import json 
f = open ('linkyoutube.json','r')
twitterurls = []
data = json.loads(f.read())
for i in range(len(data)):
	key  = data[i].keys()[0].encode('ascii','ignore')
	for j in range(len(data[i][key]['links'])):
		if 'twitter' in data[i][key]['links'][j]:
			twitterurls.append(data[i][key]['links'][j].encode('ascii','ignore'))
g = open ('twitter_youtube.txt','w')
for ele in twitterurls:
	g.write(ele)
	g.write('\n')
g.close()
f.close()