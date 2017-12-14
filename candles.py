import json, hmac, hashlib, time, requests, base64, authentication
import pandas as pd
from requests.auth import AuthBase

#request
r = authentication.requests.get(authentication.api_url + '/products/'+input('Enter your symbol: ')+'/book?level=2', auth=authentication.auth)

#format json data
data = (json.dumps(r.json()))

#read json into pandas
df = pd.read_json(data, orient='columns')

#define columns
df.columns=['time', 'low', 'high', 'open', 'close', 'volume']

#convert time to YYYY-MM-DD HH:MM:SS
df['time'] = pd.to_datetime(df['time'], unit='s')

#print
print (df.head(20))