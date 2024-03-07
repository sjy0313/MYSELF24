# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:04:14 2024

@author: Shin
"""

# 문자열 삽입 
# 결과= 삽입할문자열.join(원본문자열)

s = " Python is the best choice "
".".join(s) # ' .P.y.t.h.o.n. .i.s. .t.h.e. .b.e.s.t. .c.h.o.i.c.e. '

#%%
# 문제 : 아래 전화번호를 점(.) 대신에 하이픈(-)으로 대체하라
hp = "010.1234.1234"
hp.replace('.', '-') # '010-1234-1234' str.replace()함수 이용
hl = "010 1234 1234"
"-".join(['010', '1234', '1234']) # '010-1234-1234' 

t1=hl.split() # ['010', '1234', '1234']
tx= '-'.join(t1) 
