# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:30:02 2024

@author: Shin
"""

# -*- coding: utf-8 -*-
# list()
# 여러 형태의 자료들의 연속된 모임
# 변경가능(mutable)
#%%
lst = [1,3,5,['a','b','c']]
print(lst)
print('요소의 갯수:', len(lst)) # 요소의 갯수: 4

print(type(lst)) # <class 'list'>
print(type(lst[0])) # <class 'int'>
print(type(lst[-1])) # <class 'list'>

#%%
# 맨 마직막 요소의 각 개별요소(문자열이기 떄문에)
lstx = lst[-1]
print(lstx[0])# a
print(lstx[1])# b
print(lstx[2])# c 

print(type(lstx[0])) # <class 'str'>
print(lst[-1][0]) # a































 