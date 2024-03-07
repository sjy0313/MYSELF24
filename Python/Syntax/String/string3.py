# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:02:03 2024

@author: Shin
"""

# 문자열 인덱싱
# 문자열은 연속된 문자들의 집합 
# 참조 : 특정한 위치의 문자를 본다 
# 시작위치 : 0부터 시작 
# 참조방법 : 문자열[인덱스]
# 참조범위 : 0 ~ n-1, n=len(문자열)
# 제약사항 : 참조는 할 수 있지만 바꿀 수 없다.(read-only)

#문자열 길이 함수: len()
# 문자열길이 = len(문자열) 

#%%
#문자열의 길이(length)
import string
string.ascii_uppercase # 대문자출력
print(string.ascii_uppercase)
print(string.ascii_lowercase)

s ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sl= len(s)
print(sl,':', s)
#26 : ABCDEFGHIJKLMNOPQRSTUVWXYZ
#%%
#문자열 인덱싱
#참조 :0~25(26-1)
print("첫번쨰 문자: ", s[0]) # 첫번쨰 문자:  A
print("마지막 문자: ", s[sl-1]) # 마지막 문자:  Z

print(s[0], s[1], '...', s[24], s[25]) # A B ... Y Z
print(s[0], s[1], '...', s[sl-2], s[sl-1]) # A B ... Y Z
#%%
# 음수(minus)로 참조가능
# 뒤에서부터 참조 
# 맨 마지막 위치 : -1, len(문자열) -1 
slast1 = s[len(s) - 1]
slast2 = s[-1] 
print(slast1) # Z
print(s[-2]) # Y
print(s[0]) # A

#%%
#제약사항 : 참조는 할 수 있지만 바꿀 수 없다. (read-only)
# TypeError: 'str' object does nto support item assignment 

#%%
# 문자열 전체의 값을 변경은 가능 [내용물이 바뀌어서 id도 변경됨 새로운 메모리에 할당처리]
print(id(s))
s= "abcdefghijklmnopqrstuvwxyz."
print(id(s), s) # 2432597390272 abcdefghijklmnopqrstuvwxyz
# z뒤에 .추가 하니 id변경 2432721493712 abcdefghijklmnopqrstuvwxyz.
