# -*- coding: utf-8 -*-
# 집합 자료형(set)
# 교집합 : &
# 메소드: set.intersection(set2)
#%%
s1 = set('123456') # {'6', '5', '4', '2', '3', '1'}
s2 = set('456789') # {'6', '9', '8', '5', '4', '7'}
print(s1)
print(s2)

# 양쪽 모두 존재하는 값 선택
s3 = s1 & s2
print(s3) # {'6', '4', '5'}
#%%

s4 = s1.intersection(s2)
print(s4)  # {'6', '4', '5'}
