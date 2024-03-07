# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:06:02 2024

@author: Shin
"""

# 문자열 연산
# - 더하기(+)
# - 곱하기(*)

# 문자열 더하기(붙이기)
hello = "Hello"
world = "World"
helloworld= hello + ', ' + world + '!'
print(helloworld) #Hello, World!
#%%
# 복합대입 연산자(+=)
hw2 = ''
hw = '' # 빈 문자열
hw += hello
hw += ', '
hw += world
hw += '!'
print(hw) # Hello, World!
#%%
# hw2 = hw2 + 
hw2 = ''
hw2 = hw2 + hello
hw2 = hw2 + ', '
hw2 = hw2 + world
hw2 = hw2 + '!'
print(hw2) # Hello, World!
