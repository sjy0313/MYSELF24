# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:28:50 2024

@author: Shin
"""

# 함수(Function)
# 키워드 매개변수(kwargs)
# 호출할 떄 반드시 인자에 키를 명시해야함.
# 인자: 키=값
#%%
# 파라미터 : dict로 받음
def move(**kwargs):
    print(f"[move] type:{type(kwargs)}: {kwargs}")
    for key in kwargs.keys():
        print(f"key={key}, value={kwargs[key]}")
#%%
move(x=10, y=20, z=30) # [move] type(<class 'dict'>: {'x': 10, 'y': 20, 'z': 30}

#%% 
#move(1,2,3) # TypeError: move() takes 0 positional arguments but 3 were given

move(a=10, b=20, c=30) # type(<class 'dict'>: {'a': 10, 'b': 20, 'c': 30}
#[move] type:<class 'dict'>: {'a': 10, 'b': 20, 'c': 30}
#key=a, value=10
#key=b, value=20
#key=c, value=30