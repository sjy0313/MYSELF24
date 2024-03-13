# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:40:14 2024

@author: Shin
"""
# 1급 시민 = 함수형 프로그래밍
# 함수형 프로그래밍 기법으로 작성하라
# 함수도 변수와 같은 방식으로 취급
# 함수를 변수에 대입가능
# 함수를 리턴 할 수 있다
# 컬렉션에 저장가능
# 문제
# 함수를 이용하여 사칙연산 계산기를 만들라
# 계산기능 : 더하기/빼기/곱하기/나머지/제곱
# - 총합누적, 평균
# - 히스토리 이력

# search -> replace text -> box클릭해서 변수 바꿀 수 있음
#%%
#전역변수(global variable)
#histories = [] # 히스토리 : 표현식 전체를 이력처리 
#total = 0 #총합 누적
#count = 0 #연산 횟수
#%%
# int(input())는 사용자의 숫자 입력을 받아들인 다는 뜻(내장함수)

#%%
# 계산기 (누적함수) op = operator , c = local변수는 함수연산 안에서 정의됨
# op + 가 true라면 c라는 리턴값은 plus(a,b)이다. 
# 연산자별 연산 수행
# global 함수 없애고 진행
# 계산기
def Calc(name):
    histories = [] # 히스토리: 표현식 전체를 이력처리
    total = 0      # 총합누적
    count = 0      # 연산횟수
    
    # 총합
    def tot():
        nonlocal total
        return total
    
    # 평균
    def avg():
        nonlocal total
        nonlocal count
        return total / count
    
    # 재계산(히스토리)
    def recalc(): 
        nonlocal histories
        
        t = 0
        for a, op, b in histories:
            c = comp(a, op, b)
            t += c
            print(f"{c} = {a} {op} {b}: total({t})")
        return t, t / len(histories) # 튜플(총합, 평균)    
    
    def compute(a, op, b):
       nonlocal histories
       nonlocal total
       nonlocal count
       
       c = comp(a, op, b)
       if c == None:
           return 0
       
       # 누적
       count += 1 # 연산횟수 누적
       total += c # 연산결과 누적
       histories.append((a, op, b)) # calc() 함수에 전달된 인자를 보관(튜플)
       return c   # 단위연산 결과 리턴    
    
    def calc(oper, *args):
        if oper == 'tot':
            return tot()
        elif oper == 'avg':
            return avg()
        elif oper == 'recalc':
            return recalc()
        elif oper == 'calc':
            a, op, c = args
            return compute(a, op, c)
        else:
            return None
     
    return calc

#%%

# 더하기
def plus(a, b):
    return a + b

# 빼기
def sub(a, b):
    return a - b

# 곱하기
def mul(a, b):
    return a * b

# 나누기(정수 나누기)
def div(a, b):
    return a // b
# # / 소수점 아래자리까지 리턴을 하지만 // 는 정수로 값을 리턴
# 나머지
def sur(a, b):
    return a % b

# 제곱
def pow(a, b):
    return a ** b

#%%

# 연산자별 연산 수행
def comp(a, op, b):
    if op == '+':
        c = plus(a, b)
    elif op == '-':
        c = sub(a, b)
    elif op == '*':
        c = mul(a, b)
    elif op == '/':
        c = div(a, b)
    elif op == '%':
        c = sur(a, b)
    elif op == '**':
        c = pow(a, b)
    else: # 준비되지 않은 연산자
        return None
    
    return c

#%%

calc = Calc("전자계산기")
calc('calc', 10, '+', 20)      # 30    
calc('calc', 2,  '*', 4)       # 8
calc('calc', 10, '/', 2)       # 5
calc('calc', 2,  '**', 3)      # 8

print("총합:", calc('tot'))    # 51 
print("평균:", calc('avg'))    # 12.75 
print("검산:", calc('recalc')) # (51, 12.75)

#%%

calc2 = Calc("전자계산기2")
calc2('calc', 99, '+', 1)      # 100    

print("총합:", calc2('tot'))    # 100 
print("평균:", calc2('avg'))    # 평균: 100.0
print("검산:", calc2('recalc')) # (51, 12.75)


#%%

print("총합:", calc('tot'))     # 51 
print("총합:", calc2('tot'))    # 100 
#%%
# 나의 과정

def calculator(x, op, y):
     def plus(a, b):
         return a + b
    
     def minus(a, b):
         return a - b
    
     def times(a, b):
         return a * b
    
     def divide(a, b):
         return a / b
    
     def remainder(a, b):
         return a % b
    
     def square(a, b):
         return a ** b
 
     def calN(*args):
        for val in args:
            if isinstance(val, str):
                print(val, end=' ')
            else:
                print(f"{val} ", end='')
        result = calculator(*args)
        print(f"= {result}")
        return result
    
     if op == '+':
       return plus(x, y)
     elif op == '-':
       return minus(x, y)
     elif op == '*':
       return times(x, y)
     elif op == '/':
       return divide(x, y)
     elif op == '%':
       return remainder(x, y)
     elif op == '**':
       return square(x, y)
     else:
       return 0

        
result = calculator(2, '*', 3)
print(result) # 6

      
            
