# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:52:11 2024

@author: Shin
"""
# 자료형 검사 : type()
# 자료형 변환 : bool(논리형), int(정수형), float(실수형), str(문자형)

#%%

# 정수형을 논리형으로 변환
bt = bool(1) 
bf = bool(0)
print(type(bt), bt)  # <class 'bool'> True
print(type(bf), bf)  # <class 'bool'> False

#%%

# 논리형을 정수로 변환 
nt = int(True)
nf = int(False)
print(type(nt), nt) # <class 'int'> 1
print(type(nf), nf) # <class 'int'> 0

#%%

# 문자열을 실수로 변환 
f1 = float("0.1234") # 실수
f2 = float("0.1234e4") # 지수
f3 = float("1234e-4") # 지수 
print(type(f1), f1) # 0.1234
print(type(f2), f2) # 1234.0
print(type(f3), f3) # 0.1234
f4 = float("0.1234x4") # e대신 x가 들어가면 value error 
#%%

# 문자열로 변환 
s1 = str(f1)
print(type(s1), s1) # <class 'str'> 0.1234







