# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:29:23 2024

@author: Shin
"""

import pandas as pd
df = pd.read_json('./sample.json')
print(df.to_string())


{"employees":[
  { "firstName":"John", "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":"Peter", "lastName":"Jones" }
]}


