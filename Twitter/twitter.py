from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import time

twitter_url_count = 0
key_count = 0

twitter= []
urlcall = "https://api.twitter.com/1.1/users/show.json?screen_name="

####################################################################################
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY1 = "VpVNMfzvuCyiNs0LjqB4Js8Cl"
CONSUMER_SECRET1 = "fJY7QbAXxxBUDpgOgor8P8I2nSJm4rRVVemATzVQVqO015WjD6"

OAUTH_TOKEN1 = "846494307179683841-wNGeMWR4CMQjfVIcT1Hf3zp2nKuHpfk"
OAUTH_TOKEN_SECRET1 = "mu6pQ1dtZONKD4SpEXDD9EPFESgOeYw6p1ghE524ZCy7H"


CONSUMER_KEY2 = "zOQPDmYudkHXJKP80aEHu9r0P"
CONSUMER_SECRET2 = "mR9BfKeMYjrSkPwxoGba4I7G7RmQy8SXoFDDXAlCqcfBOR9WiL"

OAUTH_TOKEN2 = "846494307179683841-Ew9tBccl7NwjX1FKFB1RdnYeXRIorpY"
OAUTH_TOKEN_SECRET2 = "z3VNYZd2gLkEysLEPoAiFMeBX5uQ1E1LxbA8ObDvlQX8b"

CONSUMER_KEY3 = "34Kux1zV9l4bhTH8VdQ8VLgbf"
CONSUMER_SECRET3 = "8fxAgEyI1zKxc6xpUtrZl6IrpK4WXXK29yLFKwIjO9BqOF6a7Y"

OAUTH_TOKEN3 = "846494307179683841-RPR9eTnD2liOpyc22frGraZwysuX8L7"
OAUTH_TOKEN_SECRET3 = "BZTvZZRMEyD3bvLZePEKA5PAqhYW9rqiUkwJ3ESayeuAW"


CONSUMER_KEY4 = "SK2WzbOZ85wQzzcXEUjoJMqkt"
CONSUMER_SECRET4 = "1H6ASgo5Zd6OEYgEwP3RHq2iIOTd076KHApDrWPzQpZP9CjE6o"

OAUTH_TOKEN4 = "846494307179683841-2dUZUWl6sZmfl904u4nTc8lcxn5Vi5V"
OAUTH_TOKEN_SECRET4 = "HuX0q7Qygxn826Ktuwexk6QD14Zg8xVESNqkTte7lp3gZ"


CONSUMER_KEY5 = "B5hy8FaxU83VX0nbyiMgy97Ue"
CONSUMER_SECRET5 = "prlfeynfFU81SfQKLEil8ouvU2o2AEejJJFVPGH8lBCGOdDAmI"

OAUTH_TOKEN5 = "846494307179683841-AFNUJF1HvhpXgtBnXF6KbyoGT0mstqZ"
OAUTH_TOKEN_SECRET5 = "PI2W5rE0TMLvLrm2OvlhSfK7kRJ9nzZOit1N2kHS8Kr7s"

CONSUMER_KEY6 = "JzzJrn6yOsZY3hz6Y0tAks7Zr"
CONSUMER_SECRET6 = "kKNjBa30qeFom01Ou7vy7toIWNsQ4cijYDBHsXJm0NoxZMa6tn"

OAUTH_TOKEN6 = "846494307179683841-HA93Cubyx8jqbblTyVaC0G6EYc5pz4z"
OAUTH_TOKEN_SECRET6 = "voAWkUb2yqKPWS4kuOrNrQ3rUgl6E72PFu4061J6AEr1m"



#####################################################################################

keys_list=[
[CONSUMER_KEY1,	CONSUMER_SECRET1,	OAUTH_TOKEN1,	OAUTH_TOKEN_SECRET1],
[CONSUMER_KEY2,	CONSUMER_SECRET2,	OAUTH_TOKEN2,	OAUTH_TOKEN_SECRET2],
[CONSUMER_KEY3,	CONSUMER_SECRET3,	OAUTH_TOKEN3,	OAUTH_TOKEN_SECRET3],
[CONSUMER_KEY4,	CONSUMER_SECRET4,	OAUTH_TOKEN4,	OAUTH_TOKEN_SECRET4],
[CONSUMER_KEY5,	CONSUMER_SECRET5,	OAUTH_TOKEN5,	OAUTH_TOKEN_SECRET5],
[CONSUMER_KEY6,	CONSUMER_SECRET6,	OAUTH_TOKEN6,	OAUTH_TOKEN_SECRET6]

]
# def setup_oauth():
#     """Authorize your app via identifier."""
#     Request token
#     oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
#     r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
#     credentials = parse_qs(r.content)

#     resource_owner_key = credentials.get('oauth_token')[0]
#     resource_owner_secret = credentials.get('oauth_token_secret')[0]

#     Authorize
#     authorize_url = AUTHORIZE_URL + resource_owner_key
#     print 'Please go here and authorize: ' + authorize_url

#     verifier = raw_input('Please input the verifier: ')
#     oauth = OAuth1(CONSUMER_KEY,
#                    client_secret=CONSUMER_SECRET,
#                    resource_owner_key=resource_owner_key,
#                    resource_owner_secret=resource_owner_secret,
#                    verifier=verifier)

#     Finally, Obtain the Access Token
#     r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
#     credentials = parse_qs(r.content)
#     token = credentials.get('oauth_token')[0]
#     secret = credentials.get('oauth_token_secret')[0]

# 	return token, secret


def get_oauth(keypos):
	# oauth = OAuth1(CONSUMER_KEY,
	#             client_secret=CONSUMER_SECRET,
	#             resource_owner_key=OAUTH_TOKEN,
	#             resource_owner_secret=OAUTH_TOKEN_SECRET)
	oauth = OAuth1(keys_list[keypos][0],
				client_secret=keys_list[keypos][1],
				resource_owner_key=keys_list[keypos][2],
				resource_owner_secret=keys_list[keypos][3])
	return oauth


if __name__ == "__main__":
    # if not OAUTH_TOKEN:
    #This if part of the logic needs work if fresh keys are used to make it 
    # fully automated. Else for the time being I am just skipping the if loop
    
    if not keys_list:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        
    else:
    	f = open('all_nodes.txt','r')
    	data =  f.read()
    	data  = data.split('\n')

    	for link in data:
    		if not 'twitter' in link:
    			continue
    		else:
				print twitter_url_count, "::::" ,link

				twitter_url_count+=1
				if twitter_url_count>899:
					twitter_url_count =0
					key_count+=1
					if key_count == 6:
						key_count = 1
						print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
						print "The 15 mins delay has started to refresh the keys"
						print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
						time.sleep(900)
		        
				oauth = get_oauth(key_count)
				username =  link[link.rfind('/')+1:]
				newurl = urlcall +str(username)
				print "New Url: ", newurl
				r = requests.get(url=newurl, auth=oauth)
        		# r = requests.get(url="https://api.twitter.com/1.1/application/rate_limit_status.json?resources=help,users,search,statuses", auth=oauth)
				data = {}
				if 'error' not in r.json().keys()[0].encode('ascii','ignore'):
					data = {
					"screen_name": r.json()['screen_name'].encode('ascii','ignore'),
					"followers_count": r.json()['followers_count'],
					"friends_count": r.json()['friends_count'],
					"listed_count": r.json()['listed_count'],
					"created_at": r.json()['created_at'].encode('ascii','ignore'),
					"favourites_count": r.json()['favourites_count'],
					"statuses_count": r.json()['statuses_count'],
					"description": r.json()['description'].encode('ascii','ignore'),
					"location": r.json()['location'].encode('ascii','ignore')
					}
					print "This is the key being used", key_count
					twitter.append({str(username):data})
	g =  open('twitter.json','w')
	for ele in twitter:
		g.write(str(ele)+'\n')
	g.close()
	f.close()