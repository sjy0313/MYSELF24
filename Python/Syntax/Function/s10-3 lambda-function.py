# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:05:28 2024

@author: Shin
"""

# 함수 : 람다 lambda
# inline 함수(익명함수) # 1개의 라인으로 표현
# functional programming에 활용

# 정의와 선언이 동시에 이루짐
# 정의선언 : 함수변수 = lambda parameter : 표현식
# 함수호출 : 함수변수(parameter)
# 결과리턴 : 표현식의 처리 결과를 리턴 

#%%
# 람다함수 정의의 함께 호출하는 방법
# (lambda parameter: expression)(parameter)
x = 10
y = 3
print(f"값 {x} * {y} ->", (lambda a, b : a * b)(x, y)) # 값 10 * 3 -> 30
print(f"값 {x} ** {y} ->", (lambda a, b : a ** b)(x, y)) # 값 10 ** 3 -> 1000
# x,y -> a,b -> a*/**b 호출과정