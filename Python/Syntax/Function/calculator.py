# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:40:14 2024

@author: Shin
"""

# 문제
# 함수를 이용하여 사칙연산 계산기를 만들라
# 계산기능 : 더하기/빼기/곱하기/나머지/제곱
# - 총합누적, 평균
# - 히스토리 기능

#%%
totals = [] # 계산결과 누적 히스토리 
total = 0 #총합 누적
count = 0 #연산 횟수
#%%
def plus(a, b):
    return a + b
#%%
def minus(a, b):
    return a - b
#%%
def times(a, b):
    return a * b
#%%
# / 소수점 아래자리까지 리턴을 하지만 // 는 정수로 값을 리턴
def divide(a, b):
    return a // b
#%%
# 나머지
def remainder(a, b):
    return a % b
#%%
def square(a, b):
    return a ** b

# int(input())는 사용자의 숫자 입력을 받아들인 다는 뜻(내장함수)

#%%
# 계산기 (누적함수) op = operator , c = local변수는 함수연산 안에서 정의됨
# op + 가 true라면 c라는 리턴값은 plus(a,b)이다. 
def calc(a, op, b):
    if op == '+':
        c = plus(a,b)
    elif op == '-':
        c = minus(a,b)
    elif op == '*':
        c = times(a,b)
    elif op == '/':
        c = divide(a,b)
    elif op == '%':
        c= remainder(a,b)
    elif op == '**':
        c = square(a,b)
    else: # c가 만들어지지 않는 경우 
        return 0 # calc 함수에서 지원하지 않을 떄(사용한 기호 외를 사용할 떄)
    # 전연변수(함수 밖에 선언되어 있는 변수의 값을 변경하려면)
    global total # 객체형은 global을 명시하지 않아도 수정 가능
    global count
    # 누적
    count += 1 # 연산횟수 누적
    total += c # 연산결과 누적
    totals.append(c) # 계산결과를 보관(히스토리)
    return c # 단위연산결과
#%%
# TypeError: unsupported operand type(s) for +=: 'function' and 'int'
# 연산자(operator)란 피연산자(operands)를 관계지어, 사칙연산을 수행
# a,b = operands/ + - * / = operator 
#%%
# 총합
def tot():
    return total 
# 평균
def avg():
    return total / count
# 재계산(검산)
def recalc():
    t=0
    for n in totals:
        t += n
    return t, t/ len(totals) # 튜플(총합, 평균)


#%%
calc(10, '+', 20)
calc(2, '**', 4)


