# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:12:32 2024

@author: Shin
"""
# 함수
# 함수정의와 호출은 전달되는 순서, 자료형을 맞춰야 한다.
#%%
# 함수 정의 (return value 존재할 떄) 
def add(a, b):
    return a + b 
#%%
def mul(a, b): 
    c = a * b
    return c # 결과리턴
#%%
# 함수호출
print(add(1,2)) # 3
print(add(10,20)) # 30

#%%
print(add('ABC', 'DEF')) # ABCDEF
print(mul('*', 10))  # **********
# TypeError: can't multiply sequence by non-int of type 'str 문자열의 곱 안됨.
# 문자열 + 숫자도 결합안됨.
