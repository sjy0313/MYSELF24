# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:37:54 2024

@author: Shin
"""
# 람다 함수 응용 
# 파라미터 
# what : 문자열
# func : 함수
# a, b : 계산 할 데이터
def calc(what, func, a, b):
    print(f"calc({what}): ", func(a,b)) # (def add에)심부름 역할
#%%
# 일반 함수(재활용가능 함수):
# 덧셈용함수
def add(a,b):  
    return a + b
# 뺼샘용함수
def sub(a,b):  
    return a - b
# 곱셈용함수
def mul(a, b):
    return a * b


#%%
calc("덧셈", add, 10, 20) # calc(덧셈): 30
calc("뺄셈", sub, 10, 6) # calc(뺄셈):  4
calc("곱셈",mul, 10, 3) # calc(곱셈):   30
#%%
# 람다함수 사용(일회용함수)
calc("덧셈", lambda a,b: a + b, 10, 20) # 30
calc("덧셈", lambda a,b: a + b, 10, 6)  #  4
calc("덧셈", lambda a,b: a + b, 10, 3)  # 30
#%%