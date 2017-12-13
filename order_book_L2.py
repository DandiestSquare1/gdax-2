import json, hmac, hashlib, time, requests, base64, authentication
import pandas as pd
from requests.auth import AuthBase

#request
r = authentication.requests.get(authentication.api_url + '/products/'+input('Enter your symbol: ')+'/book?level=2', auth=authentication.auth)

#format json data to include "
data = (json.dumps(r.json()))

#read json into pandas
df = pd.read_json(data, orient='columns')

#change order of columns
df = df[['bids','asks']]

#create list
bid_price=[]
bid_volume=[]
bid_order=[]
ask_price=[]
ask_volume=[]
ask_order=[]

#loop to retrieve data
for i in range(len(df)):
    bid_price.append(float(df['bids'][i][0].lstrip("'").rstrip("'")))
    bid_volume.append(float(df['bids'][i][1].lstrip("'").rstrip("'")))
    bid_order.append(df['bids'][i][2])
    ask_price.append(float(df['asks'][i][0].lstrip("'").rstrip("'")))
    ask_volume.append(float(df['asks'][i][1].lstrip("'").rstrip("'")))
    ask_order.append(df['asks'][i][2])
    
#create df
df=pd.DataFrame({"bid_price":bid_price, "bid_volume":bid_volume, "bid_order":bid_order, "ask_price":ask_price, "ask_volume":ask_volume, "ask_order":ask_order})

#reorganize df
df=pd.DataFrame(df, columns=["bid_price", "bid_volume", "bid_order", "ask_price", "ask_volume", "ask_order"])

#print
print (df.head(10))