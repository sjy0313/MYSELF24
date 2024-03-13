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
# values 리스트 만들기 : dict.values()
dv = student.values()
print('values:', dv)
 # values: dict_values(['홍길동', 34, '한양', False])
#%%
# dict.values()를 튜플로 전환
tv = tuple(dv)
print(type(tv), tv) # <class 'tuple'> ('홍길동', 34, '한양', False)

#%%
# 반복문을 이용하여 목록 얻음 # tab을 통해 4간격 들여쓰기.
for v in tv:
    print(v)
# 홍길동
#34
#한양
#False
#%%
for v in student.values():
    print(v)
#%%
# 튜프을 리스트로 전환
tl = list(dv)
print(type(tl), tl)
#%%
for v in student.values(): 
    print(v)
    

