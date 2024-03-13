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
    print(f"[tots] type({type(vals)}), {vals}")
#%%
# 가변인자로 호출
tots(10)
tots(10,20)
tots(10,20,30)
#[tots] type(<class 'tuple'>), (10,)
#[tots] type(<class 'tuple'>), (10, 20)
#[tots] type(<class 'tuple'>), (10, 20, 30)
#%%
# 튜플
tots((99,)) # [tots] type(<class 'tuple'>), ((99,),)

tots(99,) # [tots] type(<class 'tuple'>), (99,)
#%%
# [주의]
# 튜플을 인자로 보내면 튜플이 하나의 인자로 전달(3개 인자 아님)
tots((10,20,30)) # [tots] type(<class 'tuple'>), ((10, 20, 30),)
