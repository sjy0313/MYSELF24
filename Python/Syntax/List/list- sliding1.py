# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:01:09 2024

@author: Shin
"""

# 리스트 슬라이싱
# 리스트[시작위치:종료위치]
# 시작위치: 0부터 시작 
# 종료위치: n - 1

lst = [0,1,2,3,4,5,6,7,8,9]

print(lst[:])  # 전체
print(lst[3:7]) # [3, 4, 5, 6] 

# 마지막 요소 제외 
print(lst[:-1]) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 마지막 요소만 슬라이싱
print(lst[-1:]) # [9]
print(lst[-1:len(lst)]) #  [9]
print(lst[len(lst)-1:len(lst)]) # [9] : 9~10
#%%

# 홀수 추출
odd = lst[1::2]
print(odd) # [1, 3, 5, 7, 9]
# 짝수 추출
even = lst[0::2]
print(even) # [0,2,4,6,8]