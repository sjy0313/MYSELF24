# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:49:08 2024

@author: Shin
"""

# 리스트에서 요소를 꺼내기 : pop()
# 꺼낸 요소는 삭제가 된다.
# pop(index) : 특정 위치의 요소를 꺼냄


#%%
lst = ['삼성', 'LG', 'SK', 'HD']


#%%

index = 2
value = lst.pop(index)
print(f"{lst}.pop({index}) -> {value}")

#%%

# 인덱스의 범위를 넘어서면 예외발생
# IndexError: pop index out of range
index = 3
value = lst.pop(index)
print(f"{lst}.pop({index}) -> {value}")