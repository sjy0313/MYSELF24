# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:20:48 2024

@author: Shin
"""
# p98
# ,를 key값과 value값이 달라짐
student = {
    "name": "홍길동",
    "age": 34,
    "address": "한양",
    "survive":  False,
}

print(student) # {'name': '홍길동', 'age': 34, 'address': '한양', 'survive': False}

#%%
# Key 리스트 만들기 : dict.keys()
dk = student.keys()
print('keys:', dk)
# key만 입력시 
# 속성오류:  AttributeError: type object 'tuple' has no attribute 'tk'
#%%
# dict.keys()를 튜플로 전환
tk = tuple(dk)
print(type(tk), tk)
# <class 'tuple'> ('name', 'age', 'address', 'survive')

#%%
# 반복문을 이용하여 목록 얻음 # tab을 통해 4간격 들여쓰기.
for k in tk:
    print(k)
#%%
for k in student.keys():
    print(k)






