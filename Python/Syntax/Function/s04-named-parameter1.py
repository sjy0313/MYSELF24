# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:28:31 2024

@author: Shin
"""

# 함수(function)
# 매개변수를 지정하여 호출하기 
# 함수를 호출할 떄 함수에 정의되어 있는 parameter명시적으로 지정하여 호출 
# 인자의 순서를 무시하고 전달할 수 있다. (중요)
#%%
# 함수 정의 
def move(x,y,z):
    print(f"x={x}, y={y}, z={z}")

#%%
# 함수 호출 순서대로 인자를 지정
move(10, 20, 30)  # x=10, y=20, z=30

#%%
# 함수 호출
# 매개변수를 지정하여 호출/ 매개변수 전체의 이름 지정
move(z=30, x=10, y= 20)
#%%
# 매개변수를 일부만 지정하여 호출하기 
move(10, z=30, y=20) # x 생략
move(10, 20, z=30) # x, y 생략 
#%%
# move(z=30, 10, 20) # x, y 생략
# SyntaxError: positional argument follows keyword argument 
# 생략하는 경우 먼저 생략 된 것을 앞쪽으로 지정 필요 위 함수에서는 10 , 20
# move(y=20, 10, z=30) # x 생략
# move(10, y=20, 30) # x, y 생략