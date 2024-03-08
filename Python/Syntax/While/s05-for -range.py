# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:09:42 2024

@author: Shin
"""

# 반복문 : for 
# 지정된 범위를 반복 
# 범위: range
# 객체: list, tuple, str
# for 변수 in list(tuple, str):
#   수행할 문장
#    ...

# range(시작값,종료값,건너뛰기) : 숫자 발생기(slicing과 유사)
# - 시작값: 기본값 0
# - 종료값: 종료값 - 1
# - 증가값: 건너뛰기
# - 사용 예:
#   range(종료값)
#   range(시작값, 종료값)
#   range(시작값, 종료값, 증가값)    
#%%

m = 10
for n in range(m): # 0부터 m-1까지 반복, m번 반복
    print(n)
#%%
# 1부터 10까지 연속된 숫자의 합계
s = 1
e = 10 + 1
m = range(s, e)   
# 1부터 10까지 연속된 숫자의 합계
m = range(11)
t = 0
for n in m:
    t += n
print(f"{s}부터 {e}까지의 합은?", t) # 1부터 11까지의 합은? 55
#%%
# 1부터 10까지 연속된 숫자의 홀수의 합계
s = 1
e = 10 
j = 2
m = range(s, e+1, j)   
t = 0 
for n in m:
    print(n, end=' ')
    if n != e-1:
      print(', ',end=', ')
    
    t += n
    
print(f"{s}부터 {e}까지의 홀수의 합은?", t)
#%%
# 1부터 10까지 연속된 숫자의 짝수의 합계
s = 2
e = 10 
j = 2
m = range(s, e+1, j)   
t = 0 
for n in m:
    print(n, end='')
    if n != e:
      print(', ',end=', ')
    
    t += n
    
print()
print(f"{s}부터 {e}까지의 짝수의 합은?", t)
    
    
    
    
    
    
    
    
    
    
    
    
    
