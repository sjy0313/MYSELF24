# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:44:25 2024

@author: Shin
"""

# 리스트에서 요소를 꺼내기 : pop()
# 꺼낸 요소는 삭제가 된다.
# pop(0)
# 선입선출 : FIFO(First In First Out), 큐(Queue)

#%%
lst = ['삼성', 'LG', 'SK', 'HD']

#%%

# 참조 : 인덱싱을 해서 해당하는 위치의 값을 확인
print(lst[0]) # 삼성
lg = lst[1]
print(lg)     # LG

print(lst)    # 원본의 변화는 없다.

#%%

# 선입선출 : FIFO(First In First Out), 큐(Queue)

print("# pop()")
print(lst.pop(0)) # 삼성
print(lst.pop(0)) # LG
print(lst.pop(0)) # SK
print(lst.pop(0)) # HD

print('원본:', lst) # []

#%%

# 꺼낼 데이터가 없으면 예외발생 : IndexError
# IndexError: pop from empty list
print(lst.pop(0))