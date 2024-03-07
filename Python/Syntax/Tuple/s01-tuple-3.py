# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:30:16 2024

@author: Shin
"""
# 빈 튜플
tx = tuple()
#%%
t3 = tuple(1,3,5)
#TypeError: tuple expected at most 1 argument, got 3 
t4 = tuple(1,3,5,)
#%%
t3 = tuple((1,3,5))
print(type(t3), t3) # <class 'tuple'> (1, 3, 5)
#%%
# 튜플의 요소를 모두 지움
t3 = ()
#%%
# 리스트와 같이 삭제 명령어를 사용하여 요소를 지울 수 없다
del t3[:]
# TypeError: 'tuple' object does not support item deletion
#%%
# 변수 제거 del 해당튜플
# 문제
# 튜플 (1,3,5,7,9)에서 인덱스 2번째의 값 5를 10으로 바꿔라 
tup = (1,3,5,7,9)
print(type(tup), tup) # <class 'tuple'> (1, 3, 5, 7, 9)

tup1 = tup[:2] + (10,) + tup[3:]
print(tup1) # (1, 3, 10, 7, 9)
# 새롭게 튜플 제구성
tv= 10 # 바꿀 값
tx= 2  # 바꿀위치
tp= (1,3,5,7,9)
tp1 = tp[:tx]
tp2 = tp[tx+1:]
tp = tp1 + (tv,) + tp2
print(tp)
#%%
# 튜플 리스트 객체로 만든 후에 다시 튜플 객체로 전환 
tl = list(tp) # 튜플을 리스트 객체로 생성
tl[tx] = tv
tp = tuple(tl) # 리스트 객체를 튜플 객체로 전환
print(tp)

