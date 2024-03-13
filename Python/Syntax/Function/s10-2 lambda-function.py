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
# 일반함수 : 정의
#두 인자(a,b)를 비교해서 큰 값을 리턴
def max(a, b):
    return a if a > b else b
#%%
# 함수 이름에 None을 할당하면 더 이상 함수를 호출할 수 없음(함수의 위치를 잃어버림)
max = None
# 일반함수 : 호출
max(10, 20)
# TypeError: 'NoneType' object is not callable
#%%
# 람다함수 : 정의 (일반함수와 다르게 여러 라인으로 실행문 작성 불가)
# 파라미터 : a, b
# 실행문 : a if a > b else b 
# 람다함수변수 : lambda_max
lambda_max = lambda a, b: a if a > b else b 
# 람다함수 : 호출
x = 99
y = 98
z = lambda_max(x, y)
print(f"값 {x}와 {y} 중에 큰 값은? {z}") # 값 99와 98 중에 큰 값은? 99
