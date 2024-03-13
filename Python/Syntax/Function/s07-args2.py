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
        if isinstance(val, int): #( == True가 :뒤에 생략되어있음) val값이 정수
        # val자료형이 정수이면 누적연산 수행
            tot += val
    return tot

#%%
# 가변인자로 호출
print(tots(10)) # 10
print(tots(10,20)) # 30
print(tots(10,20,30)) # 60

#%%
# 튜플
print(tots((99,))) # 0 val이 정수형이 아닌 튜플형인 (99,)이므로 tot의 값이
# 0으로 남게 되고 리턴값으로 0을 반환

#%%
# [주의]
# 튜플을 인자로 보내면 튜플이 하나의 인자로 전달(3개 인자 아님)
tots((10,20,30)) # [tots] type(<class 'tuple'>), ((10, 20, 30),)
