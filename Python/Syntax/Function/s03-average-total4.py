# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:30:27 2024

@author: Shin
"""

# 함수
#%%
def total(k, e, m):
    return k + e + m
# 평균
def average(tot, cnt):
    return tot / cnt

#%%
tot = total(70, 80, 90)
avg = average(tot, 3)
#%%
#%%
tot, avg = total(70, 80, 90)
print("총점:", tot) 
print("평균:", avg)
#%% 
# 다중 리턴
# 국어, 영어, 수학 점수는 0부터 100까지
# 총점, 평균을 리턴하는 함수
def totavg(k, e, m):
    if k<0 or k>100:
        print(f"국어점수{(k)}가 점수 구간을 벗어났습니다.")
        return None 
    if e<0 or e>100:
        print(f"영어점수{(k)}가 점수 구간을 벗어났습니다.")
        return # 값을 리턴하지 않음 
    if m<0 or m>100:
        print(f"수학점수{(k)}가 점수 구간을 벗어났습니다.")
        return tuple((-1,-1)) # 튜플로 리턴(명시적) 
    tot =  k + e + m
    avg = tot / 3
    return tot, avg 


#%% 
# 국어점수가 구간을 벗아남
# 리턴: None, None
score = totavg(700,80,90)
print("총점:", tot) # none 
print("평균:", avg) # none

#%%
# 영어점수가 구간을 벗어남
# 리턴: None
val = totavg(70, -1, 90)
print("점수:", val) #none

# 조건부 연산자를 사용하여 처리
print("총점:", val[0] if val != None else 'Error') # Error
print("평균:", val[1] if val != None else 'Error') # Error

# 수학점수가 구간을 벗어남
# 리턴: tuple
val = totavg(70,80,-1)
print("점수:", val) # 

