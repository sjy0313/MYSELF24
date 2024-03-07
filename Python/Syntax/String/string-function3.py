# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:11:02 2024

@author: Shin
"""

# 문자열 함수

# 문자열의 위치 : find()
# 처음 만나는 문자열의 위치
# 결과 :  
#   성공: 0부터 
#   실패: -1(찾지 못하면)

s = "Python is the best choice"
print("0123456789" * 4)
print(s)

ipos = s.find('i')
kpos = s.find('k')

print(f"'{s}.find('i') : ", ipos) #'Python is the best choice.find('i') :  7
# 'Python is the best choice.find('i') :  7
print(f"'{s}.find('k') : ", kpos) # 'Python is the best choice.find('k') :  -1

#%%
# 문자열 탐색 
print(f"'{s}.find('is') : ", s.find('is')) # :  7
print(f"'{s}.find('the') : ", s.find('the'))  # : 10

#%%
#문제 (단, find함수를 이용하라)
#문자열 연속해서 찾기, 문자열 변수(s)에서 지정된 문자('t')의 위치를 모두 찾아라
s = "Python is the best choice"
print("0123456789" * 4)
print(s)
findstr = 't'
print(f"문자열 ('{s}')에서 문자열('{findstr}')의 갯수는?", s.count(findstr))
# 문자열 ('Python is the best choice')에서 문자열('t')의 갯수는? 3
# 분활
t1= s.find(findstr)
print(t1) #  2
s1= s[t1+1:] # 슬라이싱
t2= s[t1+1:].find(findstr) + t1 + 1 
print(t2)
s2= s[t2+1:] # 슬라이싱
t3= s[t2+1:].find(findstr) + t2 + 1
print(t1, t2, t3)

#%%
# str.find(sub[, start[, end]])
# 결과 = 문자열.find(찾을 문자열, 시작위치[,종료위치])
t1= s.find(findstr) 
t2= s.find(findstr, t1 + 1)
t3= s.find(findstr, t2 + 1)
print(t1, t2, t3) # 2 10 17