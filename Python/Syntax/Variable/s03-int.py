# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:32:00 2024

@author: Shin
"""

# 정수(int)
a = 1234
b ='1234' # 문자열(string), str

# TypeError: unsupported operand type(s) for +: 'int' and 'str
c = a + b 


print(type(a), a) # <class 'int'> 1234
print(type(b), b) # <class 'str'> 1234
print(c)

#%%
# 문자열을 연산이 가능한 정수로 변환
# 조건 문자열이 숫자 형태인 경우만 정수로 변환이 가능

d = int(b)
e = a + d
print(e) # 2468
