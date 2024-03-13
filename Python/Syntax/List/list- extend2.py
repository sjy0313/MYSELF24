# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:34:43 2024

@author: Shin
"""

# 리스트 확장 : extend()
# 기존에 있는 리스트에 요소를 추가하여 확장
# 다수 append()를 하나로 처리하는 효과
# 추가 리스트는 개별적으로 하나씩 append()가 된다.
# 리턴 : None

lst = ['삼성', 'SK', 'LG']
elt = ['APPLE', 'HD']
lst.extend(elt)
print(lst)
rt = lst.extend(elt)
print("리턴:", rt) # 리턴: None

#%%
print('lst:', lst.extend(elt)) # lst: None
print(lst) # ['삼성', 'SK', 'LG', 'APPLE', 'HD']

#%%
# 메모리 내부에서 확장하고 사라진다.
# 리턴값이 없으므로
abc = ['ABC'].extend(elt)
print(abc) # None

#%%

elt.extend(['ABC'])
print(elt) # None
#%%
#확장시킬 변수를 만들고 리턴을 받아 
#기존 변수에 할당을 해서는 안된다.
abc = ['ABC']
abc = abc.extend(elt)
print(abc) # None



