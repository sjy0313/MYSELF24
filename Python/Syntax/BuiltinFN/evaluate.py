# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:19:01 2024

@author: Shin
"""

# eval : evaluate의 약자
# 문자열로 구성된 표현식(expression)을 입력으로 받아서 실행
# 문자열로 구성된 파이썬 코드 실행 
# 파이썬 코드를 외부에 만들어 놓고 읽어서 동적으로 처리할 때 사용

expr = "10 + 20"
print(expr) # 10 + 20  #문자열 출력
print(eval(expr)) # 30 #처리결과
print(eval("divmod(10,3)")) # (3, 1) divmod는 2개 숫자 10,3을 입력받고 10/3 
# 몫과 나머지를 튜플로 리턴한다.
#%%
a = 3
b = 5
c = a * b
x = eval("f'c={c}'")
print(x) # c=15

