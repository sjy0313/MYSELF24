# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:25:54 2024

@author: Shin
"""

# 함수(Function)
# 기본값 : default value
# 기본값 지정은 파라미터의 뒤에서부터 지정해야 한다. 

#%%
# SyntaxError: non-default argument follows default argument
"""
def move(x=10, y, z=5):
    print(f"move: x({x}), y({y}), z({z})")
"""
#%%
def move(x, y=20, z=5):
    print(f"move: x({x}), y({y}), z({z})")
#%%
#
move(10) # x(10), y(20), z(5)

