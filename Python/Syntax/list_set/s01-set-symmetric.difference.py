# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:29:56 2024

@author: Shin
"""

# 집합 자료형(set)
# 대칭 차집합(symmetric difference)
# 한 쪽에는 있지만 양쪽 모두에 있지 않은 요소
# 대칭 차집합: ^(circumflex) 
# 메소드: set.symmetric.difference()

a = {'서울', '대전', '대구', '부산', '제주'}
b = {'서울', '대전', '대구', '부산', '전주', '목포'}
c = {'서울', '대전', '대구', '부산', '제주'}

# 메서드
sd1 = a.symmetric_difference(b)
print(sd1) # {'제주', '전주', '목포'}
# 대칭 차집합 : ^(circumflex)
sd2 = a ^ b
print(sd2) # {'제주', '전주', '목포'}

#%%
# 문제
# 위의 세트(set) a,b를 차집합 합집합 결합하여 대칭 차집합을 구하라
 # 정답 : {'제주', '전주', '목포'}
a = {'서울', '대전', '대구', '부산', '제주'}
b = {'서울', '대전', '대구', '부산', '전주', '목포'}

p1 = b.difference(a)
print(p1) #{'목포', '전주'}
p2 = a.difference(b)
print(p2) # {'제주'}
p4 = p1 | p2
print(p4) # {'목포', '제주', '전주'}

print(b-a) # {'목포', '전주'}
print(a-b) #{'제주'}
sdx = (b-a) | (a-b)
print(sdx) # {'목포', '제주', '전주'}
