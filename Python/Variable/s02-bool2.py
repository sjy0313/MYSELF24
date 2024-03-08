# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:18:42 2024

@author: Shin
"""
# 논리형(boolean) : bool 
#%%
# 논리형의 크기 비교
# True : 1
# False : 0
print(True > False) # True
print(False < True) # False 

# bool(값) : 해당하는 값을 논리형으로 변환
t1 = bool(1)
t2 = bool(-1)
t3 = bool(' ')
print(t1) # True
print(t2) # True 무효의 값
print(t3) # True 빈 문자열
f1 = bool(0)
f2 = bool(None) # 무효의 값
f3 = bool(' ') # 빈 문자열
print(f1) # False
print(f2) # False
print(f3) # False


#%%
# is : ==
# not is : !=


