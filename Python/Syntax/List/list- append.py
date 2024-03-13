# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:33:49 2024

@author: Shin
"""

# 리스트 추가 : append()
# 기존에 있는 리스트에 요소를 추가하여 확장(extend)
# 기존에 있는 리스트에 하나의 요소를 추가(append)
# 리스트 객체 자체를 변경
# 리턴값?

lst = ['삼성', 'SK', 'LG']
rt = lst.append(['APPLE', 'HD'])
             
print("append() 함수의 리턴값?", rt)  # None
# garbage collection. isenabled() 
#-- Returns true if automatic collection is enabled. GC로 rt값 복원가능
lst.append(['APPLE', 'HD'])
print(lst) ['삼성', 'SK', 'LG', ['APPLE', 'HD']]

# 다수 append()를 하나로 처리하는 효과
# 추가 리스트는 개별적으로 하나씩 append()가 된다.

lst = ['삼성', 'SK', 'LG']

lst.extend(['APPLE', 'HD'])

print(lst) # ['삼성', 'SK', 'LG', 'APPLE', 'HD']

lst += ['NC', 'ABC']

print(lst) # ['삼성', 'SK', 'LG', 'APPLE', 'HD', 'NC', 'ABC']

#%%
lst.append('IBM')
print(lst) # ['삼성', 'SK', 'LG', ['APPLE', 'HD'], 'IBM']
lst.append(['DB'])
print(lst) # ['삼성', 'SK', 'LG', ['APPLE', 'HD'], 'IBM', ['DB']]
# 개별 요소로서 추가됨