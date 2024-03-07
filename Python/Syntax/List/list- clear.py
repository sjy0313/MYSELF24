# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:49:25 2024

@author: Shin
"""

# 리스트에서 모든 요소를 제거 : clear()
# 리스트.clear()

#%%
lst = ['삼성', 'LG', 'SK', 'HD', 'HD']

print(id(lst), lst)

#%%

# clear()
# id는 변하지 않는다.
lst.clear()
print(id(lst), lst)

#%%

# 리스트에 빈 리스트 할당을 해서
# 모든 요소를 지우는 효과냄
# clear()와는 차이가 있다.
# id가 바뀜
lst = []
print(id(lst), lst)