# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:55:45 2024

@author: Shin
"""

# - 키(KEY)는 변한지 않는 값을 사용해야함
# - 리스트(list)는 사용x(값 변경 가능) / 중복 허용 x

dt = {}
lk = [10,20,30]
dt[lk] = '숫자'
# TypeError: unhashable type: 'list' 
# hashable 하기 위해서는 immutable 해야한다/ 
# 즉 리스트의 데이터 구조는 mutable 하기 때문에 위같은 
# 오류가 출력된다.  
#%%
# 튜플은 키로 사용가능 
tk = (10,20,30)
dt[tk] = "숫자"
print(dt) 
# {(10, 20, 30): '숫자'}
