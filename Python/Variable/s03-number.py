# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:56:01 2024

@author: Shin
"""

# 숫자형 
# 연산을 수행할 수 있는 자료형
# 정수 : int
# 실수 : float

#%%
# 정수(int) 
#길이 제한이 없다 
#컴퓨터가 수용할 수 있는 한계까지 

n1 = 123456789012345678901234567890
print(n1) # 30자리
n1 = n1 + 1
print(n1)   # 30자리 
#%%
# 4바이트 
b8 = 2 ** 8
print(b8) 256가지의 경우의 수  0~255 (컴퓨터가 처리하는 수)

# 7비트 
b7 = 2 ** 7
print(b7) 128, 0~127 

#%%
# 8바이트 64비트
b64 = 2 ** 64
print("2의 64승?" , b64)
kb = 1000 
mb = 1000 * 1000
gb = mb * 1000
tb = gb * 1000
print("kb:  ", int(b64/ kb))
print("mb:  ", int(b64/ mb))
print("gb:  ", int(b64/ gb))
print("tb:  ", int(b64/ tb))



