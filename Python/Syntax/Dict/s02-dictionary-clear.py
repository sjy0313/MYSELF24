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
# 딕셔너리 함수를 이용한 객체 모두 요소 지우기
student.clear()
print(student) # {}
#%%
# 빈 객체를 대입하여 모든 요소 지우기
student = {}
print(student) # {}
