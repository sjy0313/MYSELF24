# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:33:48 2024

@author: Shin
"""

# 인스턴스(instance)
# -> 데이터가 특정한 자료형으로 객체(object)화 된 상태
# 객체(object)
# -> 고유한 자료의 실체(변수는 실체를 지칭)
#%%
# 자료형(type)
pi = 3.14 # 이 자료형의 성격은 실수형
print(type(pi), pi) # <class 'float'> 3.14  실수형

pt = type(pi)
print(pi, type(pt))  # 3.14 <class 'type'> 타입형 

#%%
# isinstance()
# pi 객체가 자료형(float)으로 인스턴스화 되었는가? 
print(isinstance(pi, float))  # True
