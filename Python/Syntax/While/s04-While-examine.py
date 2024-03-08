# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:08:44 2024

@author: Shin
"""

# 문제
# while문을 이용하여 해결
# 1부터 100까지의 연속으로 숫자를 1씩 증가시켜
# 3의 배수와 5의 배수를 각각 구해라 
s1 = 1 # 시작
s2 = 2 
c3 = s1 + 2  # 3배수
c5 = s2 + 3 # 5배수 
while True:
    if c3 <= 100 and c5 <= 100:
      break
      c3 = s1 + 2
      c5 = s2 + 3
print(c3)
print(c5)

n = 1
m = 100
m3 = []
m5 = []

while n<= m:
    if n % 3 == 0: # 3배수
      m3.append(n)
      
    if n % 3 == 0:
      m5.append(n)
      
    n += 1

print("3배수:", m3)
print("5의 배수:", m5)

# continue 문을 활용하라
# - 아래 문장을 실행하지 않고 다시 while의 조건식으로 이동
n = 0
m = 100
m3 = []
m5 = []

while n<= m:
    n += 1
    if n % 3 != 0 and n % 5 != 0:
        continue #아래 문장을 실행하지 않고 조건식으로 이동
    if n % 3 == 0: 
      m3.append(n)
      
    if n % 5 == 0:
      m5.append(n)
      
print("3배수:", m3)
print("5의 배수:", m5)

# 만약 무한루프에 빠질 시 keyboardinterrupt