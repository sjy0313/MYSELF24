# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:06:02 2024

@author: Shin
"""
# map()
# map(func, iterable) # 반복가능한 데이터를 입력받는다.
# filter는 개수가 바뀌는 반면에 map()은 각 요소에 함수f를 적용한 결과를 리턴

#%%
# lambda function
lst = [1,3,5,7,9]
# 각 요소에 2를 곱한 결과를 리턴
lstm = map(lambda x: x * 2, lst)
lstx = list(lstm)
print(lstx)
# [2, 6, 10, 14, 18]
# 입력한 데이터의 갯수와 처리 결과의 갯수가 동일


def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result 

result = two_times([1,2,3,4])
print(result) # [2, 4, 6, 8]
