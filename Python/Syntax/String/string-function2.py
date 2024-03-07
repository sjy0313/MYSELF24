# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:16:56 2024

@author: Shin
"""

# 문자열 함수
# 문자 개수 세기 : count()
s = "hello world"
l = 'l'
c = s.count(l)
print(f"문자열('{s}')에 문자 ('{l}')는 ({c})개 있다.")
# 문자열('hello world')에 문자 ('l')는 (3)개 있다.
print(f"문자열(\"{s}\")에 문자 ('{l}')는 ({c})개 있다.")
# 문자열("hello world")에 문자 ('l')는 (3)개 있다.
print(f'문자열("{s}")에 문자 ("{l}")는 ({c})개 있다.')
# 문자열("hello world")에 문자 ("l")는 (3)개 있다.
print(f'문자열("{s}")에 문자 (\'{l}\')는 ({c})개 있다.')
# escape sequence (string2.py 참조)
#\(백슬래시) 뒤에 문자나 숫자가 오는 조합을 이스케이프 시퀀스(escape sequence)
# \\ (백슬래시), \', \" , \n(새줄)
#%%
# attributerror 가 호출되면 존재하지 않은 함수임 
n= 100
n.count('0')
# AttributeError: 'int' object has no attribute 'count' 문자열만의 전용함수임을 알려줌
s.count('0')
#%%

tel = "010-1234-5678"
telcnt = tel.count('-')
print(f"'{tel}'.count('-') : {telcnt}개")
# 010-1234-5678'.count('-') : 2개

#%%
# 문자열을 변수에 담지 않고 직접 
spcnt = "Welcome to korea". count(' ')
print("공백 갯수: ", spcnt)
# 공백 갯수:  2