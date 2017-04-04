import flickrapi
import webbrowser
import json
import time
flickrapi_call = 0
key_count  = 0

api_key100 = '2b3b4d7eaf7dd7527e42eebd7b66e5e8'
api_secret100 = '678c6ca91b73eb23'

api_key1 = '0930efb0108ba641e1a9227e3a288711'
api_secret1 = '9c7fa568e1a1c156'

api_key2 = '27ccfa8191c137ba7cf3caac08df1867'
api_secret2 = '16f16cb7e9282c06'

api_key3 = '979f430d1a94852bb4b30bcbd3aa4267'
api_secret3 = '00f656b082ea420b'

api_key4 = 'b81f4cb4a57847a472b3dab2c19e64ed'
api_secret4 = '7a418b250a7dedb0'

api_key5 = 'ecdad53eb5ce7696e26794910df42442'
api_secret5 = 'd8ae6a5ca3da64ee'

api_key6 = 'd2ebd8db92be92d8bfa0927c954606cd'
api_secret6 = 'a9122939c82ad2ef'

api_key7 = '43133ed8c1048410a0fe5e466fef7b49'
api_secret7 = '7dfe2e8548905b88'

api_key8 = '2a6fa38766181be9dc43dcb7199c8101'
api_secret8 = '6903c641681f518c'

api_key9 = 'b9e0ab0e506abf9d201c7dd72cbaaeb0'
api_secret9 = '1abf5f6e360f5942'

api_key10 = 'b993247a26d8d0213aee608924f34ce0'
api_secret10 = 'ca2f2b4f477649ae'

api_key11 = '7e078136f49c696ed84b0c7e58fb43d4'
api_secret11 = '9be4f25b1b887e51'

api_key12 = '4b4481899eb31b97beccdc6e4f719bf3'
api_secret12 = '3ef5cc139ecf794f'

api_key13 = 'cc36816ff9611e73a0ce5a87440f9d5c'
api_secret13 = 'c2fbf0fc7706e660'

api_key14 = '977b181d7cf823072121ce9b7edcb3f4'
api_secret14 = 'f3d73f4052b09afe'

api_key15 = 'feabd79fc61e28ace34d1f9c7d2bc7cb'
api_secret15 = 'd3e87445e822ec53'

api_key16 = 'bf4116363fd8726409207f0e808cc01b'
api_secret16 = '3e2fe6ca53b5aa53'

api_key17 = '47c279082e9b138d57746d91e6a28c6f'
api_secret17 = '32154a07aab5e678'



key_list=[
[api_key1,  api_secret1],
[api_key2,  api_secret2],
[api_key3,  api_secret3],
[api_key4,  api_secret4],
[api_key5,  api_secret5],
[api_key6,  api_secret6],
[api_key7,  api_secret7],
[api_key8,  api_secret8],
[api_key9,  api_secret9],
[api_key10,  api_secret10],
[api_key11,  api_secret11],
[api_key12,  api_secret12],
[api_key13,  api_secret13],
[api_key14,  api_secret14],
[api_key15,  api_secret15],
[api_key16,  api_secret16],
[api_key17,  api_secret17],
[api_key100,  api_secret100],
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
f= open('flickr_getnsid.json','r')
data =json.load(f)
for i in range(len(data)):
    print i
    flickrapi_call+=1
    if flickrapi_call>3599:
        flickrapi_call = 0
        key_count+=1
        if key_count == 18:
            key_count = 0
            print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
            print "The 15 mins delay has started to refresh the keys"
            print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
            time.sleep(900)

    try:
        flickr = flickrapi.FlickrAPI(key_list[key_count][0], key_list[key_count][1],format='parsed-json')
        userid = data[i].values()[0].encode('ascii','ignore')
        resp = flickr.profile.getProfile(user_id=userid)
        print "This is the key being used", key_count
        flickrdata.append({  data[i].keys()[0].encode('ascii','ignore'): resp['profile']})

    except Exception:
        pass
        
    
g= open('flickr_username.json','w')
for data in flickrdata:
    g.write(str(data)+'\n')

g.close()
f.close()
