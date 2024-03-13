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
# 가변 parameter 앞에 일반 parameter 지정가능
#def tots(title, *vals):
def tots(*vals, title): 
    print(f"[{title}]{vals}", end=": ") # tuple
    tot = 0
    for val in vals:
        if isinstance(val, int): #( == True가 :뒤에 생략되어있음) val값이 정수
        # val자료형이 정수이면 누적연산 수행
            tot += val
    return tot

#%%
# 가변인자로 호출
print(tots("홀수", 1,3,5,7,9))  # [홀수](1, 3, 5, 7, 9): 25
print(tots("짝수", 2,4,6,8,10)) # [짝수](2, 4, 6, 8, 10): 30
# 가변인자를 다른 인자 뒤로 지정할 떄 error
print(tots("홀수", 1,3,5,7,9)) 
#TypeError: tots() missing 1 required keyword-only argument: 'title'
