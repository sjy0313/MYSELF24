# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:19:55 2024

@author: Shin
"""

# 리스트 정렬(sort) : sort()
# 오름차순(ascending) :  작은값 -> 큰값
# 내리차순(descending) : 큰값 -> 작은값
# None = 리스트.sort() 
# 기본 : 오름차순
# 리턴 : None
# 원본이 변경, 요소의 위치가 바뀐다.

score = [99,67,100,56,90,70]

#%%
# 오름차순
# score.sort() 
print(score) # [56, 67, 70, 90, 99, 100]

#%%
# 내림차순: 
#  - 먼저 sort()를 하여 오름차순으로 정렬 후
#  - reverse()를 하여 반전하여 내림차순 효과를 낸다.
score.sort()
score.reverse()
print(score) # [100, 99, 90, 70, 67, 56]