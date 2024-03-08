# -*- coding: utf-8 -*-
# 집합 자료형(set)
# 차집합 : -
# 메소드: set.difference()
#%%
s1 = set('123456') 
s2 = set('456789') 
print(s1)
print(s2)

# a - b
# a에서 b를 제외한 나머지 요소
s3 = s1 - s2
print(s3) # {'1', '2', '3'}
s4 = s2 - s1
print(s4) # {'9', '8', '7'}

#%%
s5 = s1 - s2
s5 = s1.difference(s2)
print(s5) # {'1', '2', '3'}