# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:49:25 2024

@author: Shin
"""

# 리스트에서 모든 요소를 제거 : clear()
# 리스트.clear()

#%%
lst = ['삼성', 'LG', 'SK', 'HD', 'HD']

print(id(lst), lst)

#%%
# del 리스트[:]
del lst[:]
print(id(lst), lst)