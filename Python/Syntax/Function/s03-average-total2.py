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
#%%
# 다중 리턴
# 총점, 평균을 리턴하는 함수
def totavg(k, e, m):
    tot =  k + e + m
    avg = tot / 3
    return tot, avg 
#%% 
tot, avg = totavg(70,80,90)
print("총점:", tot) 
print("평균:", avg)

#%%
score = totavg(70,80,90)
print("총점:", tot) 
print("평균:", avg)

#%%
score = totavg(70,80,90)
print("점수:", type(score), score)
print("총점:", score[0]) 
print("평균:", score[1])
#

#%%
# 총점은 받지 않고 평균만 받음 (_ = 생략)
_, sa = totavg(70,80,90)
print("평균:", sa)
# 평균은 받지 않고 총점만 받음
st, _ = totavg(70,80,90)
print("총점:", st)
