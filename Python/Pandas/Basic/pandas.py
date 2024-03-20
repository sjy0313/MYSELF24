# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:15:17 2024

@author: Shin
"""
# Pandas 

import pandas as pd 

# dict 
dx = {'a':1, 'b':2, 'c':3}

# 시리즈 : 1차원
# index, value(로 구성)
sr = pd.Series(dx) # 딕셔너리 -> 판다스(시리즈) 객체 생성
print(type(sr), sr) # (3,)
"""
a    1
b    2
c    3
dtype: int64
"""
