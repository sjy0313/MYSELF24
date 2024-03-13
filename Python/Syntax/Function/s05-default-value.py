# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:25:54 2024

@author: Shin
"""

# 함수(Function)
# 기본값 : default value
# 파라미터 : z의 기본값은 5
def move(x, y, z=5):
    print(f"move: x({x}), y({y}), z({z})")
#%%

# 함수 move()를 호출할 떄 z에 해당하는 인자는 생략 가능
move(10, 20) # move: x(10), y(20), z(5)
move(10, 20, 30)# move: x(10), y(20), z(30)
move(x=1, y=2, z=3)#  move: x(1), y(2), z(3)


