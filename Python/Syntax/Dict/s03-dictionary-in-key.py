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
    "alive":  False,
}

print(student) # {'name': '홍길동', 'age': 34, 'address': '한양', 'alive': False}

#%%
# 딕셔너리 함수를 이용한 객체 모두 요소 지우기
student.clear()
print(student) # {}
#%%
# 빈 객체를 대입하여 모든 요소 지우기
student = {}
print(student) # {}

#%%
# 해당 키가 존재하는지 조사(확인)
# 결과 
age = 'age'
age_exist = age in student 
print(f"key('{age}')in {student} ->", age_exist) # True


#%%
# dict.get()으로 존재유무를 확인하여 bool(True, False) 처리
survive = 'alive'
survive_exist = student.get(survive) #  != None
print(f"key('{survive}') in {student} -> ", survive_exist)  #  False
# key('생존') in {'name': '홍길동', 'age': 34, 
#'address': '한양', 'survive': False} ->  None

#%%
# 키가 존재하지 않으면 디폴트값을 리턴
# dict.get(키, 디폴트)
lock = '주소'
locd = "위치키 존재하지 않음"
locv = student.get(lock,locd)
print(f"key('{lock}') in {student} -> {locv}")
# key('주소') in {'name': '홍길동', 'age': 34,
# 'address': '한양', 'survive': False} -> 위치키 존재하지 않음


