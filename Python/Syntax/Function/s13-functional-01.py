# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:14:28 2024

@author: Shin
"""

# 함수형 프로그래밍(functional programming)

#%%
# 글로벌 변수
# 경고창이 호출된 횟수를 카운트
gcount = 0
#%%
# 경고창을 출력하는 함수
def makeAlert(name):
    def alert(message):
        global gcount
        gcount += 1
        print(f"[{name}] gcount({gcount}): {message}")
        
    return alert

#%%
infoAlert = makeAlert("INFO")
warnAlert = makeAlert("WARN")

infoAlert("저승길을 조심하세요.") # [INFO] gcount(1): 저승길을 조심하세요.
infoAlert("행리단길을 조심하세요.") # [INFO] gcount(2): 행리단길을 조심하세요.

warnAlert("공사중, 도로끝") # [WARN] gcount(3): 공사중, 도로끝
warnAlert("홍수롤 도로소실") # [WARN] gcount(4): 홍수롤 도로소실