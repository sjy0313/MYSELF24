# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:36:44 2024

@author: Shin
"""

# 반복문: for
# 데이터: 리스트[튜플, ...]
a = [(1,2), (3,4), (5,6)]
# p142
for (first, last) in a:
    print(first, last)
    # 1 2
    # 3 4
    # 5 6
#%%
for (first, last) in a:
    print(first, last)
#%%
for t in a:
    first, last = t
    print(t, ':', first, last)