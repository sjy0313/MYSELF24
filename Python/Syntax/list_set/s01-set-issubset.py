# -*- coding: utf-8 -*-
# 집합 자료형(set)
# 부분집합
# bool = a.issubset(b)

#%%

a = {'서울', '대전', '대구', '부산', '제주'}
b = {'서울', '대전', '대구', '부산', '전주', '목포'}
c = {'서울', '대전', '대구', '부산'}
d = {'서울', '대전', '대구', '부산'}

# a는 b의 부분집합인가? 
# 결과 : False
# 이유 : a('제주')는 b에 없다
sab = a.issubset(b)
print(sab) # False
#%%
# c는 b의 부분집합?
scb = c.issubset(b)
print(scb)  # True
# c는 a의 부분집합?
sca = c.issubset(a)
print(sca) # True

#%%
# 서로 같으면 부분 집합인가? 
# c와 d는 서로 같다
# 결과 : True
print('c는 d의 부분집합?', c.issubset(d)) # c는 d의 부분집합? True
