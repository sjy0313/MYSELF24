# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:32:18 2024

@author: Shin
"""

# 문자열 포멧팅(string formatting)
# 문자열 포멧 코드 
""" 
%s : 문자열 string
%c : 문자 character 
%d : 정수 10진수, decimal
%f : (부동소수)실수(float)
%o : 8진수 octal
%x : 16진수 hexa-decimal
%% : Literal% (문자 % 자체)
""" 
# 형식 :
# 포멧문자열 % 변수
# 포멧문자열 % (변수, ...)
#%%
# 정수 %d 
num = 99 
print("이 숫자는 정수 %d 입니다."%num) # 포멧 코드
print("이 숫자는 정수 {0}입니다.".format(num)) # 문자열 함수 : 문자열.format()
print(f"이 숫자는 정수 {num} 입니다.") # f 포멧 

#%%
# 문자열
# 포멧 코드가 다중인 경우는 괄호에 포멧에 대응하는 변수를 나열하여 지정한다 
name = '홍길동'
age = 23
# userfmt = "이름이 (%s)인 사람의 나이는 (%d)세 입니다." %(name, age)
# userfmt = "이름이 (%d)인 사람의 나이는 (%d)세 입니다." %(name, age)
# print(userfmt) # #TypeError: %d format: a real number is required, not str 
userfmt = "이름이 (%s)인 사람의 나이는 (%f)세 입니다."  %(name, age)
print(userfmt)
# 이름이 (홍길동)인 사람의 나이는 (23.000000)세 입니다.

#%%

# %를 문자 그대로 출력하기 위해서는? 
# '%%'와 같이 연속해서 기술한다.

sv = 50
# print("오늘 눈이 올 확률은 (%d)% 입니다" % sv)
# TypeError: not enough arguments for format string
# 문자열 포멧에 %가 나오면 이어서 해당하는 포멧코드를 기대 
print("오늘 눈이 올 확률은 (%d)%% 입니다" % sv)

