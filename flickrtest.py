import flickrapi
import webbrowser
import json
api_key = '2b3b4d7eaf7dd7527e42eebd7b66e5e8'
api_secret = '678c6ca91b73eb23'
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


flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')

resp = flickr.profile.getProfile(user_id='8965562@N02')
resp = dict(resp)
# resp = json.loads(resp.decode('utf-8'))

alldata = []
data = {
           "website" :  resp['profile']['website'].encode('ascii','ignore'),
             "city"  :  resp['profile']['city'].encode('ascii','ignore'),
        "first_name" :  resp['profile']['first_name'].encode('ascii','ignore'),
         "last_name" :  resp['profile']['last_name'].encode('ascii','ignore'),
            # "nsid"  :  resp['profile']['nsid'].encode('ascii','ignore'),
           "hometown":  resp['profile']['hometown'].encode('ascii','ignore'),
           "twitter" :  resp['profile']['twitter'].encode('ascii','ignore'),
         "country" :  resp['profile']['country'].encode('ascii','ignore'),
        "occupation" :  resp['profile']['occupation'].encode('ascii','ignore')
        }


print data

alldata.append({resp['profile']['nsid'].encode('ascii','ignore'): data})
g= open('flickrtest.json','w')
g.write(str(alldata))
g.close()