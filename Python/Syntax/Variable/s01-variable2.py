# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:20:54 2024

@author: Shin
"""

# 변수(Variable)
# a, b의 값을 서로 교체 
a = 10 
b = 20
a = b
print('a=', a) # a= 20
print('b=', b) # b= 20

#%%
a = 10 
b = 20
print("# 교환 후")

c = a # a를 임시변수 c에 대피
a = b
b = c

print('a=', a) # a= 20
print('b=', b) # b= 10
#%%

print("# 원상복구")
# 동시에 처리가 되므로 a의 값을 대피 시키지 않아도 된다. 
a, b = b, a # python/ golang만 지원 

print('a=', a) # a= 20
print('b=', b) # b= 10
#%%

mx = 10, 20, 30
m1, m2, m3 = mx #unpacking
print('mx:', mx)  # (10, 20, 30)
print(m1, m2, m3) 
print(mx[0], mx[1], mx[2])






















