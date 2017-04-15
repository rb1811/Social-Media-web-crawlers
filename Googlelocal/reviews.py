import json
f = open('reviews.json','r')
l=[]
for line in f:
	temp_dict = ""
	temp_dict ='{'+str(line[:-2]).strip()+'}' #  For each line do some basic string manipulation and and create a proper dict out of it
	if len(temp_dict) > 3: # Check if that line has a valid json or not. Like the first and last line will have only the brackets. So ignore such lines
		l.append(json.loads(temp_dict))
	i+=1
	if i>10:
		break

# You can  remove lines from 9-11 and directly push temp_dict to Mongodb as long as there is a line in f. 
