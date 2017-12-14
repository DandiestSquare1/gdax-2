import json, hmac, hashlib, time, requests, base64, authentication
import pandas as pd
from requests.auth import AuthBase

#request
r = authentication.requests.get(authentication.api_url + '/products/'+input('Enter your symbol: ')+'/book?level=2', auth=authentication.auth)

#format json data
data = (json.dumps(r.json()))

#read json into pandas
df = pd.read_json(data, orient='columns')

#change order of columns
df = df[['time','side','size','price','trade_id']]

#print
print (df.head(20))