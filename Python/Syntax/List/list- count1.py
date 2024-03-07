# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:15:34 2024

@author: Shin
"""

# 리스트에서 해당하는 값을 포함하는 갯수 세기 : count()
# 갯수 = 리스트.count(값)
# 리턴 : 해당하는 값과 일치하는 요소의 갯수, 없으면 ZERO(0)

lst = ['삼성', 'SK', 'LG', 'APPLE', 'HD', 'LG']

value = 'LG'
count = lst.count(value)
print(f"{lst}.count('{value}')?", count)
# ['삼성', 'SK', 'LG', 'APPLE', 'HD', 'LG'].count('LG')? 2
#%%

value = 'IBM'
count = lst.count(value)
print(f"{lst}.count('{value}')?", count)    