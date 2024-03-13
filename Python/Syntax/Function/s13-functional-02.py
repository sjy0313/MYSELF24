# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:14:28 2024

@author: Shin
"""

# 함수형 프로그래밍(functional programming)

#%%
# 글로벌 변수
# makeAlert()에 의해서 만들어진 함수별로 호출된 횟수를 카운트하라.

# 전역변수
gcount= 0

#%%
# 방법1
# 경고창을 출력하는 함수 # 전역 변수를 쓰지않고 지역변수를 사용하여 해결
def makeAlert(name):
    count = 0 
    def alert(message): 
        nonlocal count # 외부함수에 선언 지역변수를 사용
        count += 1
        print(f"[{name}] count({count}): {message}")
    
    return alert
# SyntaxError: incomplete input 전역변수 global count를 썼을 떄
# nonlocal count 


#%%
infoAlert = makeAlert("INFO")
warnAlert = makeAlert("WARN")

infoAlert("저승길을 조심하세요.") # [INFO] count(1): 저승길을 조심하세요.
infoAlert("행리단길을 조심하세요.") # [INFO] count(2): 행리단길을 조심하세요.

warnAlert("공사중, 도로끝") # count 1
warnAlert("홍수롤 도로소실") # count 2

infoAlert("요철을 주의하세요!") # [INFO] count(3): 요철을 주의하세요!

# warnAlert와 infoAlert는 서로 독립적으로 움직이고 있다.

#%%
# 방법 2 
gcount = {'INFO':0, 'WARN':0 }
#%%
# 경고장을 출력하는 함수
def makesAlert(name, count):
    def alert(message): 
        count[name] += 1
        print(f"[{name}] count({count[name]}): {message}")
    
    return alert
#%%
infoAlert = makesAlert("INFO", gcount)
warnAlert = makesAlert("WARN", gcount)
infoAlert("저승길을 조심하세요.")
infoAlert("행리단길을 조심하세요.")
warnAlert("공사중, 도로끝")
warnAlert("홍수롤 도로소실")
infoAlert("요철을 주의하세요!")

print("gcount: ", gcount) # gcount:  {'INFO': 3, 'WARN': 2}

