# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:30:27 2024

@author: Shin
"""

# 함수
#%%
# 총점
def total(k, e, m):
    return k + e + m
# 평균
def average(tot, cnt):
    return tot / cnt

#%%
tot = total(70, 80, 90)
avg = average(tot, 3)
print("총점:", tot) # 총점: 240
print("평균:", avg) # 평균: 80.0