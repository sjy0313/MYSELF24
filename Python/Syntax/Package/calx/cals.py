# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:53:33 2024

@author: Shin
"""

# 모듈(module) : cals.py (계산을 하는 목록)
# 일반적으로 컴퓨터 소프트웨어서는 기능의 단위
# 파이썬에서는 함수나 변수, 클래스들을 모아 놓은 파이썬 코드 파일

# 모듈 : cals.py
# 변수
PI = 3.141592
#%%
# 함수
def add(a, b):
    return a + b

def sub(a, b):
    return a - b


#%%
# 모듈 테스트
print("[cals.py] 테스트")
print("더하기:", add(10,20))
print("뺴기:", sub(20,10))


# or 

# __name__: 파이썬 시스템 변수
# __name__{"__main__"} : 해당 모듈이 독립적으로 실행
# __name__("cals") : 종속적인 모듈로서 실행
if __name__=="__main__":
    print(f"[cals.py] __name__: {__name__}")


a = 10
b = 20
print(f"더하기({a} + {b}): ", add(a,b))
print(f"뺴기({b} - {a}): ", sub(b,a))