# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:35:12 2024

@author: Shin
"""
# 리스트 삭제(delete)
# 삭제 명령어 : del
# del 리스트
# 인덱스 : del list[index]
# 슬라이싱 : del list[start:end]

a = [1,2,3,4,5,[70, 80, 90]]
print(a) # [1,2,3,4,5,[70, 80, 90]]
#%%
#리스트 요소 삭제 : 인덱싱
del a[-1]
print(a) #[1, 2, 3, 4, 5]
#%%
# 리스트 요소 삭제 : 인덱싱
# -1 : 마지막 요소
del a[-1]
print(a) # [1, 2, 3, 4]
#%%
#슬라이싱 기법으로 삭제
del a[2:4] # 2,3번째 삭제(3,4)
print(a) # [1, 2, 5]
#%%
#전체 삭제 
del a[:]
print(a) #[]