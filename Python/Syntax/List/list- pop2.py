# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:48:38 2024

@author: Shin
"""

# 리스트에서 요소를 꺼내기 : pop()
# 꺼낸 요소는 삭제가 된다.
# pop() : 맨 마지막 요소를 꺼냄
# 후입선출 : LIFO(Last In First Out), 스택(Stack) 

#%%
lst = ['삼성', 'LG', 'SK', 'HD']

#%%

print(lst.pop()) # HD
print(lst.pop()) # SK
print(lst.pop()) # LG
print(lst.pop()) # 삼성

#%%

# IndexError: pop from empty list
print(lst.pop())