# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:14:28 2024

@author: Shin
"""

# 함수형 프로그래밍(functional programming)
# 자료 처리를 수학적 함수의 계산으로 취급하고 
# 상태와 가변 데이터를 멀리하는 프로그래밍 패러다임의 하나이다.
#%%
def score(name): # 바깥에 있는 외부함수 정의
    print(f"[score] name({name})")
    
    def minmax(*args): # 내부함수 (정의)
        min = args[0] # 기준값 설정
        max = args[0]
        
        for val in args:
            if val < min:
                min = val
            if val > max:
                max = val
                
        return name, min, max 
    
    return minmax
#%%
# 전용함수
mfunc = score("[중간고사]") # -> def minmax의 리턴값
lfunc = score("[기말고사]")

print(mfunc(70,80,90)) # ('[중간고사]', 70, 90)
print(lfunc(80,90,100)) # ('[기말고사]', 80, 100)
print(mfunc(90,77,65)) # ('[중간고사]', 65, 90)

