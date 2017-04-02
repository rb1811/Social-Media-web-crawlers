import flickrapi
import webbrowser
import json
flickrapi_call = 0
key_count  = 0

api_key9 = '56c41279d606ae3eaab92bcdb15bab81'
api_secret9 = '8ec9b02a2f2ef7fa'

api_key1 = 'bce2d6e48622524bd22fc0cb7ab14b69'
api_secret1 = '9801ec1c2ecda219'

api_key2 = 'c48f2ea76f8ee62fb89f907c818b832d'
api_secret2 = 'd9e4c90cb0dab779'

api_key3 = '8252ed55681ccb864f8a290b3e9d6514'
api_secret3 = 'bd3d05814b4f237e'

api_key4 = 'ae1aced634b44c36ae55ebb1bd49eefa'
api_secret4 = 'f9836fb70ee23906'

api_key5 = 'e849124f2f9de75f83fe135978b802ea'
api_secret5 = '7c4f0b8bf4513419'

api_key6 = '753586005eb97613534335acb108e8da'
api_secret6 = 'dc370061e25e64a1'

api_key7 = 'd4d8834b96d56ded7180782ef2d6e132'
api_secret7 = '0ca1735df4a55a81'

api_key8 = '7cfe7755f9814341deb4bc3693dd48c2'
api_secret8 = 'e053212bc2d7a913'

key_list=[
[api_key8,  api_secret8],
[api_key7,  api_secret7],
[api_key6,  api_secret6],
[api_key5,  api_secret5],
[api_key2,  api_secret2],
[api_key1,  api_secret1],
[api_key3,  api_secret3],
[api_key9,  api_secret9],

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
f= open('flickrnsid.txt','r')
data =f.read()
data =  data.split('\n')


for link in data:
    if not 'flickr' in link:
        continue
    else:
        link = link[:-1]
        print flickrapi_call, "::::" ,link
        flickrapi_call+=1
        if flickrapi_call>3598:
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

        resp = flickr.profile.getProfile(user_id=str(username))
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
g= open('flickr_nsid.json','w')
for data in flickrdata:
    g.write(str(data)+'\n')
g.close()
f.close()