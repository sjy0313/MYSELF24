# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:38:34 2024

@author: Shin
"""

# json format
json_data ='''
{"employees":[
  { "firstName":"John", "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":"Peter", "lastName":"Jones" }
]}
'''

import json
#key : employees
#value : list
# json -> dict
json_dict = json.loads(json_data)
print(json_dict)

#%%
import pandas as pd
df = pd.DataFrame(json_dict)
print(df)
'''
employees
0     {'firstName': 'John', 'lastName': 'Doe'}
1   {'firstName': 'Anna', 'lastName': 'Smith'}
2  {'firstName': 'Peter', 'lastName': 'Jones'}
'''

for dx in range(len(df)):
    rows = df.iloc[dx,:]
    print(rows) # series
'''
employees    {'firstName': 'John', 'lastName': 'Doe'}
Name: 0, dtype: object
employees    {'firstName': 'Anna', 'lastName': 'Smith'}
Name: 1, dtype: object
employees    {'firstName': 'Peter', 'lastName': 'Jones'}
Name: 2, dtype: object
'''
for dx in range(len(df)):
    rows = df.iloc[dx,:]
    
    print(type(rows.values[0]),rows.values[0]) # dict
# [{'firstName': 'Peter', 'lastName': 'Jones'}]

    
    

