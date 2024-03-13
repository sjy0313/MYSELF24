# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:28:57 2024

@author: Shin
"""

#dict.update(dict)
# 기존의 딕셔너리에 새로운 딕셔너리를 결합

weeks = {1:'월', 2: '화', 3: '수', 4: '목', 5: '금'}
# update()함수를 이용하여 기존의 딕셔너리에 새로운 딕셔너리 결합
#
sat = {6: '토'}
weeks.update(sat)
print(weeks) # {1: '월', 2: '화', 3: '수', 4: '목', 5: '금', 6: '토'}

#%%
# 딕셔너리에서는 더하기(+)를 지원하지 않음 
sun = {7: '일'}
weeks += sun
# TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'
weeks.update(sun)
print(weeks)
