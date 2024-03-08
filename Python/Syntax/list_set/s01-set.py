# -*- coding: utf-8 -*-

# 집합 자료형 : set
# set는 key만 있는 dictionary형태
# 중복을 허용x 
# - True는 1과 같은 값으로 취급
# - False는 0과 같은 값으로 취급

# 순서가 없다 (Unordered)
# - 데이터를 넣는 대로 저장x

# 다양한 형태/자료를 지정가능
# 출력된 형태 : {1,3,5}
#%%
s0 = set()
print(s0) # set() [value {}]

dt = {} # 딕셔너리
s1 =set(dt)
print(s1, type(s1)) # set() <class 'set'>

#%%
s2 = {1,3,5,7,9}
print(type(s2), s2)
# <class 'set'> {1, 3, 5, 7, 9}
#%%
# set는 key만 있는 dictionary형태
# 중복을 허용x 
# 지정한 순서가 보장되지 않으며 중복되는 데이터는 하나만 선택된다.
s1 = {3,5,7,9,9,3,7,1}
print(type(s1), s1) # <class 'set'> {1, 3, 5, 7, 9}
#%%
# 여러 자료형을 결합
# - True는 1과 같은 값으로 취급
# - False는 0과 같은 값으로 취급
s2 = {2,4,6,True,"홀수", 0.1234, 0, 1, False}
print(s2) # {0.1234, True, 2, 0, 4, '홀수', 6}
s3 = {2,4,6,True,"홀수", 0.1234, False, 0, 1} # 임의대로 출력하기 때문. 
print(s3) # {0.1234, True, 2, False, 4, '홀수', 6}


