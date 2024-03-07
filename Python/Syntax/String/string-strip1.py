# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:34:20 2024

@author: Shin
"""
#strip
s = " Python is the best choice "
s.lstrip() # 'Python is the best choice '
s.rstrip() # ' Python is the best choice'
s.strip() # 'Python is the best choice'
#replace
#문자열.replace(바뀔 문자열, 바꿀 문자열)
s.replace('Python', 'banana') # ' banana is the best choice '
s.lower() #' python is the best choice '
s.upper() # ' PYTHON IS THE BEST CHOICE '
".".join(s) # ' .P.y.t.h.o.n. .i.s. .t.h.e. .b.e.s.t. .c.h.o.i.c.e. '
# split
# 문자열 나누기 
# 리스트 = 원본문자열.split(분활문자열)
# 원본 문자열을 분활 문자열로 나누어 결과를 리스트로 리턴 
# s.split() -> 공백/tab/enter를 기준으로 문자열을 나누어줌.

s.split()  # : ['Python', 'is', 'the', 'best', 'choice']
s.split('the') # [' Python is ', ' best choice ']

tel ="010-1234-5678"
tls = tel.split('-')

print(type(tls), tls)  # <class 'list'> ['010', '1234', '5678']

print(tls[0]) # '010'

print(f"{tls[0]}- ...-{tls[2]}")
print("{0}-{1}-{2}".format(tls[0], tls[1], tls[2])) # 010-1234-5678 
print("{}-{}-{}".format(tls[0], tls[1], tls[2])) 

#%%

tel ="010.1234.5678"
tls = tel.split('.')
print(tls) ['010', '1234', '5678']

print(type(tls), tls) 

print(tls[0]) 

print(f"{tls[0]}- ...-{tls[2]}")
print("{0}-{1}-{2}".format(tls[0], tls[1], tls[2])) 
print("{}-{}-{}".format(tls[0], tls[1], tls[2])) 

#%%

# 문자열 : immutable(불변)
# 문자열 관련 함수를 실행해도 원본의 변화는 없다 
so = 'abc'
up = so.upper()
print(up)  # 'ABC'


















