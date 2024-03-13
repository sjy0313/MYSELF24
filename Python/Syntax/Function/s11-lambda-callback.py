# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:37:54 2024

@author: Shin
"""
# 람다 함수 응용 
# 파라미터 
# what : 문자열
# func : 함수
# vals : 가변인자(계산 할 데이터)
def calc(what, func, *vals):
    print(f"calc({what}): ", func(*vals)) # (def add에)심부름 역할
#%%
def add(*vals):
    tot = 0
    for val in vals:
        tot += val
    return tot

func = add # (함수를 변수에 할당)
print("func:", func(1,2,3,4,5)) # func: 15
#%%
calc("홀수", add, 1,3,5,7,9)  # calc(홀수):  25
calc("짝수", add, 2,4,6,8,10) # calc(짝수):  30