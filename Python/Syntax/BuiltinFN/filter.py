# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:27:51 2024

@author: Shin
"""

# filter(함수, 반복가능한데이터)
# 반복 가능한 데이터를 지정된 함수로 호출 했을 때 
# 리턴 값이 참인 것만 묶어서 걸러낸다.
#%%
# 리스트에서 양수만 필터링헤서 리턴하는 함수
def positive(lst):
    result = []
    for i in lst:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,7,86])) # [1, 2, 7, 86]

#%%

# 위는 비효율적임
x = 10 
b = x > 0
print(b) 
#%%
# x가 0보다 크면 True, 작거나 같으면 false , True인 경우 함수의 결과 출력.
def posfunc(x):
    return x > 0

lst1 = [1,-3,2,0,-5,7,86]
lst2 = [-1,-2,-99]

fr1 = filter(posfunc, lst1)
fr2 = filter(posfunc, lst2)
print(fr1)
print(fr2)
#[1, 2, 7, 86]
#True
#필터 객체 출력<filter object at 0x0000024EDADF6B30>

lst1 = list(fr1) # 필터객체의 결과를 리스트로 변환
lst2 = list(fr2) 
print(lst1) # [1, 2, 7, 86]
print(lst2) # []
#%%
# 람다함수 이용(일회용함수)
lst = [1,-3,2,0,-5,7,86]
lstx = list(filter(lambda x: x>0, lst))
print(lstx) # [1, 2, 7, 86]
