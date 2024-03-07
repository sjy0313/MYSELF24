# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:14:47 2024

@author: Shin
"""
# 리스트 슬라이싱
# 리스트[시작위치:종료위치]
# 시작위치: 0부터 시작 
# 종료위치: n - 1
#%%
# [이름, [국어,영어,수학], 총점, 평균]
sb = ['이름','국어', '영어', '수학', '총점', '평균']
hl = ['홍길동', 70,80,90, 0, 0.0]

hl[4] = hl[1] + hl[2] + hl[3]  # 총점
hl[5] = hl[4] / 3 # 평균


print("학생의 점수")
print(f"{sb[0]}:", hl[0])
print(f"{sb[1]}:", hl[1])
print(f"{sb[2]}:", hl[2])
print(f"{sb[3]}:", hl[3])
print(f"{sb[4]}:", hl[4])
print(f"{sb[5]}:", hl[5])

#%%
score = hl[1:4]
tot = sum(score)
avg = tot / len(score)
print("점수 : ", score) # [70, 80, 90]
print("총점 : ", tot) # 240
print("평균 : ", avg) # 80.0