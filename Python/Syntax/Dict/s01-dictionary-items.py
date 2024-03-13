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
# Key, Values 쌍으로 얻기 : dict.items()
# 리턴: 
    
items = student.items()
# {'name': '홍길동', 'age': 34, 'address': '한양', 'survive': False}    
print(type(items), items) # dict_items
# <class 'dict_items'> 
"""
dict_items(
    [('name', '홍길동'), 
     ('age', 34), 
     ('address', '한양'), 
     ('survive', False)])
"""
#%%
# dict_items -> list
# 리스트 객체로 전환
lst = list(items)
print(lst)
# [('name', '홍길동'), ('age', 34), ('address', '한양'), ('survive', False)]
# unpacking (튜플을 언패킹한 것)
print(" lst[0]:", type(lst[0]), lst[0]) #  lst[0]: <class 'tuple'> ('name', '홍길동')
key, value = lst[0]
print("lst[0]:", key, value)