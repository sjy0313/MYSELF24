# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:51:22 2024

@author: Shin
"""

# 함수(Function)
# 가변인자
# parameter인자의 갯수가 가변일 떄 
#%%
# 가변인자로 전달하면 튜플로 받음
# 가변인자형은 파라미터 변수앞에 아스터리스크(*)를 붙임
def tots(*vals):
    print(f"[tots] type({type(vals)}), {vals}") # tuple
    tot = 0
    for val in vals:
        tot += val
    return tot

#%%
# 가변인자로 호출
print(tots(10)) # 10
print(tots(10,20)) # 30
print(tots(10,20,30)) # 60

#%%
# 튜플
# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
tots((99,))

#%%
# [주의]
# 튜플을 인자로 보내면 튜플이 하나의 인자로 전달(3개 인자 아님)
tots((10,20,30)) # [tots] type(<class 'tuple'>), ((10, 20, 30),)
