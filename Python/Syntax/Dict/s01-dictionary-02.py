# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:20:48 2024

@author: Shin
"""
# ,를 key값과 value값이 달라짐
student = {
    "name": "홍길동",
    "age": 34,
    "address": "한양",
    "live":  False,
}

print(student) # {'name': '홍길동', 'age': 34, 'address': '한양', 'live': False}
#%%
# 예외 프로그램이 종료
# 키가 없으면 : KeyError : 'agex'
age = student['agex']
print("나이:", age)

#%%
age = student.get('age')
print("나이:", age) 
# 키를 찾지 못하면? # 나이: 34
agex = student.get('agex')
print("agex:", agex) # agex: None


#%%
# 키를 이용하여 값을 찾기 
# 값 = dict[키]
print("name:", student["name"])
print("age:", student["age"])
print("address:", student["address"])
print("live:", student["live"])
# name: 홍길동
#age: 34
#address: 한양
#live: False
#%%
# 변경

student['주소'] = "원주"
print("주소:", student["주소"])
#%%
# 추가
# 지정된 키가 없으면 새로 추가 됨 
student['결혼'] =28
print("결혼:", student["결혼"])
#%%
# 삭제: 없는 키를 삭제하려면?
# 예외 발생: KeyError: '전화'
del student['전화']

