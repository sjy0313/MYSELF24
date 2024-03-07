# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:24:55 2024

@author: Shin
"""

# 숫자형
x = 10
x
# 정수형(integer)
a = 123
b = -123
c = 0
print(a, b, c)

#%% 셀분리

# 실수형(floating-point)
f = 1.2
p = 3.14
print(f)
print(p)

#%%

# 지수형 
e1 = 4.24e10
e2 = 4.24e-10
print(e1)
print(e2)
#%%
e3 = 1.0e3 # 1.0 x 10의 3승 -> 1000.0
print(e3)
e4 = 1.0e-3 # 1.0 x 10의 -3승 -> 0.001
print(e4)

#%%
# 컴퓨터는 기본적으로 2(0과1로 처리)진수로 처리 
#8진수(octal) :0O, 0o
o1 = 0o177
o2 = 0O177
print(o1) # 127 = 1X8^2+7X8+7 = 127
ox = 0o377
print(ox) # 255 
#%%
# 16진수(0-15)(hexa-decimal) : 0x (뒤에서부터 n번째 자릿수가 n-1승이된다.)
# 0123456789ABCDEF
h1 = 0xff
print(h1) # 255 = 10x16

#4비트(nibble)
h1 = 0xf
print(h1)
h1 # 15
#8비트 
h2 = 0xff
print(h2) # 255 = 15x16^1 + 15x16^0 
#16비트
h3 = 0xffff
print(h3) # 65535
#%%
# 사칙연산
# +, -, *, /
# 제곱 : **
# 몫 : //
# 나머지 : %

x= 10
y= 3
m= x//y
n= x % y
print("몫:", m) # 3
print("나머지:", n) # 1

