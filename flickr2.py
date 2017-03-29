import flickrapi
import webbrowser
import json
flickrapi_call = 0
key_count  = 0

# api_key1 = '2b3b4d7eaf7dd7527e42eebd7b66e5e8'
# api_secret1 = '678c6ca91b73eb23'

api_key1 = 'a91745e3de764fb547d1c0547f8167cd'
api_secret1 = '16147f1695cae970'

api_key2 = 'b384fb49fb89bb1ca9069f31d2ab4429'
api_secret2 = '8bf159ca0c475690'

api_key3 = 'bdaed96fbcb617d03c023d135f6dd6f7'
api_secret3 = '44662dbf608a86ad'

api_key4 = '7b4bfd3040ad13d2f857c15f22752112'
api_secret4 = '3cc7a38746b064a6'

api_key5 = '14e70d57122324b7683e3caefe04763c'
api_secret5 = '3a1cfedd7f06448e'

api_key6 = 'f09113731ee9762dd193d1b069324b81'
api_secret6 = '36bdfe5fe7255a85'

api_key7 = '48c92fa738627e95d3528bddeaf672c9'
api_secret7 = '5c9bffaa8638c5c9'

api_key8 = '6974d8901d773e682e183bdd99909aad'
api_secret8 = '08baf3c9200381e0'

key_list=[

[api_key3,  api_secret3],
[api_key4,  api_secret4],
[api_key5,  api_secret5],
[api_key6,  api_secret6],
[api_key7,  api_secret7],
[api_key8,  api_secret8],
[api_key2,  api_secret2],
[api_key1,  api_secret1],
]



# print('Step 1: authenticate')

# # Only do this if we don't have a valid token already
# if not flickr.token_valid(perms='read'):

#     # Get a request token
#     flickr.get_request_token(oauth_callback='oob')

#     # Open a browser at the authentication URL. Do this however
#     # you want, as long as the user visits that URL.
#     authorize_url = flickr.auth_url(perms='read')
#     webbrowser.open_new_tab(authorize_url)

#     # Get the verifier code from the user. Do this however you
#     # want, as long as the user gives the application the code.
#     verifier = str(input('Verifier code: '))

#     # Trade the request token for an access token
#     flickr.get_access_token(verifier)

# print('Step 2: use Flickr')
# resp = flickr.profile.getProfile(user_id='11883454@N08')

# fli = flickrapi.FlickrAPI(api_key,api_secret,format='json')

flickrdata = []
f= open('flickrusernames.txt','r')
data =f.read()
data =  data.split('\n')


for link in data:
    if not 'flickr' in link:
        continue
    else:
        link = link[:-1]
        print flickrapi_call, "::::" ,link
        flickrapi_call+=1
        if flickrapi_call>1798:
            flickrapi_call = 0
            key_count+=1
            if key_count == 8:
                key_count = 0
                print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                print "The 30 mins delay has started to refresh the keys"
                print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                time.sleep(1800)

        username =  link[link.rfind('/')+1:]
        flickr = flickrapi.FlickrAPI(key_list[key_count][0], key_list[key_count][1],format='parsed-json')

        resp= flickr.people.findByUsername(username = username)
        userid = resp['user']['nsid']
        resp = flickr.profile.getProfile(user_id=userid)
        # User not found
        if resp['stat'] == "ok":
            # data ={}
            # data = {
            #  "profile_description" :  resp['profile']['profile_description'],
            #      "city"  :  resp['profile']['city'],
            # "first_name" :  resp['profile']['first_name'],
            #  "last_name" :  resp['profile']['last_name'],
            #    "hometown":  resp['profile']['hometown'],
            #    "twitter" :  resp['profile']['twitter'],
            #  "country" :  resp['profile']['country'],
            # "occupation" :  resp['profile']['occupation']
            # }
            print "This is the key being used", key_count
            flickrdata.append({  resp['profile']['nsid'].encode('ascii','ignore'): resp['profile']})
g= open('flickr2.json','w')
g.write(str(flickrdata))
g.close()
f.close()