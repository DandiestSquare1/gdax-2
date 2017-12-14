import json, hmac, hashlib, time, requests, base64, authentication
import pandas as pd
from requests.auth import AuthBase

#request
r = authentication.requests.get(authentication.api_url + '/products/'+input('Enter your symbol: ')+'/book?level=2', auth=authentication.auth)

#format json data
data = (json.dumps(r.json()))

#parse json
parsed_json = json.loads(data)

#create list
types=[]
variables=[]

#loop to retrieve data
for key, value in parsed_json.items():
    types.append(key)
    variables.append(value)
    
#create df
df_types=pd.DataFrame(types)

#create df
df_variables=pd.DataFrame(variables)

#concat dfs
df=pd.concat([df_types, df_variables], axis=1)

#transpose df
df=df.T

#capture column name
df.columns=df.iloc[0]

#reset index
df.reset_index(inplace=True,drop=True)

#drop row 
df.drop(df.index[0], inplace=True)
    
#reset index
df.reset_index(inplace=True, drop=True)

#print
print (df)