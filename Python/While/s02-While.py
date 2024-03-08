# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:26:28 2024

@author: Shin
"""


# 반복문 : while
# 조건이 만족하는 동안 반복해서 블럭의 문장을 실행한다
# while 조건식:
#   실행문
#%%
# 문제
# while문을 이용하여 1부터 100까지의 합을 구하라
total= 0
addup= 1
while addup <= 100 :
    total += addup
    addup += 1
print("1부터 100까지의 합은? ", total) # 1부터 100까지의 합은?  5050
# 2
total = 0
addup = 1
while addup >= 1 and addup <= 100:
    message = "1부터 계속 더 해라"
    total += addup
    addup += 1
print(f"뭐해? ({message}) 합은 뭐야?", total)
# 뭐해? (1부터 계속 더 해라) 합은 뭐야? 5050
# 3
n = 0 # 시작값
m = 100 # 종료값
t = 0 # 합계
c = n # 증가값

while c < m:
    c+= 1
    t+= c
print(f"({n})부터 ({m})까지 연속된 수의 합은 ({t})다")

    



        