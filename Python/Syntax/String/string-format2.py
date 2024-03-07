# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:14:43 2024

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

# 문자(character) : 단일 문자
# 'a', 'A', '한', '#', 'X'
#%%
# 문자열을 포멧(%c)에 전달하면?
abc = "abc"
#TypeError: %c requires int or char
#print("문자열 (%s)를 포맷코드(%c)에 전달하면 오류발생" % (abc,abc))

#%%
a = 'a'
print("문자포멧 : (%c)" %a)  # 문자포멧 : (a) # a앞 % 안붙여주면 (%c) a로 출력
av = ord(a) # 문자에 해당하는 ASCII 코드 값
print("문자포멧 : (%c)의 ASCII 값은 (%d)이다." % (a, av)) # 문자포멧 : (a)의 ASCII 값은 (97)이다.

#%%
# 한글
hangeul = '한'
hancode = ord(hangeul)
hanhexa = hex(hancode)
print(type(hanhexa), hanhexa)  # <class 'str'> 0xd55c

print("문자 ('%c')의 코드 값은 (%d)(0x%x)(%s)이다." % (hangeul,hancode, hancode, hex(hancode)))
# 문자 ('한')의 코드 값은 (54620)(0xd55c)(0xd55c)이다.

#hex() 함수와 동일한 기능
hexastr = "0x%x" % hancode
print(hexastr)