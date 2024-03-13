# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:02:49 2024

@author: Shin
"""

# 함수 function
# 1. 함수 호출 전 정의 되어있어야함
# 2. 리턴값이 업는 경우, 리턴값을 받으면 none출력
# 3. 함수 정의에서 리턴값이 없으면 return을 생략하면 된다.
# 4. 함수 정의에서 parameter가 없으면 함수() 형태로 parameter 생략

# 함수 장점: 
# 1. 모듈화 : 기능별로 분리
# 2. 블랙박스화 : 처리과정보다는 결과
# 3. 코드의 재사용

# 매개변수와 인수
# 매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수, 함수 정의
# 인자를 입력받은 변수 
# 인자(arguments) : 함수를 호출할 떄 전달하는 입력값, 함수 호출

# API(application programming (연결)interface) 고유한 기능을 가진 모든 소프트웨어 
# 멀터텝에서의 콘센트(= API) 
# WBS(work-breakdown structure)작업 분업/분활 구조(작업구조를 분할해서 프로젝트 관리)
"""
함수정의

def 함수명(파라미터):
    명령문
    return 리턴값
"""
#%%
# 함수가 정의 되기전에 호출되면 오류
# NameError: name 'hello' is not defined
# hello()
#%%
#함수 정의: 한 번만 호출 ( ; = 실행문의 끝을 의미 줄끝에 생략되어있음)
#함수이름 : hellocnt / parameter : 문자열, 출력횟수 / return value : 없음(none)
def hellocnt(msg, cnt): 
    print(f"[hellox] msg({msg}), cnt({cnt})")
    for n in range(cnt):
        print(f"[{n}]: {msg}")
        
#%%
#함수호출 (interface(연결) 이 중요함)
# 인자는 순서대로 함수의 파라미터로 전달됨.
hellocnt("Hello, World.", 10) # Hello, World. 10번 찍힘.
# hellocnt(10, "Hello, World.") # 인자의 순서를 바꾸면 잘못된 처리를 함.

#%%
# 함수 정의에 리턴값이 없는데 
# 함수 호출에서 리턴을 받으면? 
rt = hellocnt("Hello, World.", 10)
print("리턴:", rt) # 리턴: None






