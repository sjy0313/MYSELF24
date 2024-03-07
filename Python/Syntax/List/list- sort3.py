# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:38:24 2024

@author: Shin
"""
# 리스트 정렬(sort) : sort()
# 오름차순(ascending) :  작은값 -> 큰값
# 내리차순(descending) : 큰값 -> 작은값
# None = 리스트.sort() 
# 기본 : 오름차순
# 리턴 : None
# 원본이 변경, 요소의 위치가 바뀐다.
# 제약조건: 리스트의 자료형 모두 동일해야 한다.

#%%
lst = ['a', 'Abc', 'B', 99, 10, 88]

# 자료형이 다른 경우에는 정렬을 할 수 없다.
# TypeError: '<' not supported between instances of 'int' and 'str'
lst.sort()

#%%
#대문자는 소문자보다 ASCII 코드값이 작다.
sb = 'A' < 'abc'
print(sb) # True

#%%
sbx = 'ABc' < 'ABd'
print(sbx) # True 
#%%
# TypeError: '<' not supported between instances of 'str' and 'int'
ob = 'a' < 123
print(ob)
