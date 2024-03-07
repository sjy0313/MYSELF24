# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:05:15 2024

@author: Shin
"""

# 튜플
# 언패킹(unpacking) 2개이상으로 받아야함
jobs = ('요리사', '교사', '사무원')

chef, teacher, officer = jobs
print(chef) 
print(teacher)
print(officer)
#%%
# 변수 하나로 튜플로 받으면 언패킹이 아니라 
# 새로운 변수에 참조를 할당
jobx = jobs
print(type(jobx), jobx) # <class 'tuple'> ('요리사', '교사', '사무원')
#%%
# 언패킹(unpacking)
# 요소의 개수가 일치해한다
# 생략 : 언더스코어 (_)

_, _, off = jobs
print(off) #사무원
cf,_,_ = jobs
print(cf) # 요리사
_,tc,_ = jobs
print(tc) # 교사
#%%
# 언패킹(unpacking)
# 갯수가 일치x
# ValueError: too many values to unpack (expected 2)
c,t = jobs
#%%
# 언패킹 순서는 개발자가 지정
student = ('홍길동', 34, 'A+')
age, name, grade = student
print(age)# 홍길동
print(name)# 34
print(grade)# A+







#%%
# 인덱스 참조 : 튜플도 리스트처럼
print(jobs[0])
print(jobs[1])
print(jobs[2])