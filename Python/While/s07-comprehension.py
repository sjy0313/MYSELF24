# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:25:05 2024

@author: Shin
"""

# list comprehension(내포)
# 좀 더 편리하고 직관적인 프로그램을 만들 수 있다.
# 리스트(lst)에서 하나씩 꺼내어 10을 곱하여
# 리스트 구성
lst = [1,2,3,4,5]
lstx = [n * 10 for n in lst]
print(lstx) # [10, 20, 30, 40, 50]
#%%
# 리스트(lst)에서 짝수만 구해서 3을 곱하여
# 리스트 구성 
even = [n * 3 for n in lst if n % 2 == 0]
print(even) # [6, 12]

# 짝수
even = []
for n in lst: 
    if n % 2 == 0:
       even.append(n * 3)
print(even) # [6, 12]
#%%
# 리스트(lst)에서 홀수만 구해서 3을 곱하여 리스트를 구성
odd = []
for n in lst:
    if n % 2 == 1: # 홀수
       odd.append(n * 3)
print(odd) # [3, 9, 15]

#%%
# tuple comprehension
# generator
teven = (n * 3 for n in lst if n % 2 == 0)
print(type(teven), teven)
# <class 'generator'> <generator object <genexpr> at 0x0000020E7D33BAC0>
# 명시적으로 tuple 함수를 사용해야 한다. 
tp = tuple(n * 3 for n in lst if n % 2 == 0)
print(type(tp), tp) # <class 'tuple'> (6, 12)
