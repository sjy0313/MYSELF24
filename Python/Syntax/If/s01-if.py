# -*- coding: utf-8 -*-
# 조건문 : if
# 조건식의 결과는 자료형(bool)이다.
# True or False에 따라서 분기
# block 
#- block의 시작은 콜론(:)
#- 들여쓰기로 블럭을 형성(indent)
#- Tab, Space
# 조건식
# - ==, !=, >, >=, <, <=
# - and, or, not
# - in, not in 
# - is, not is
# - a is b 
# - not a is b
# - a is c
# - not a is c

"""
# if문
if 조건식:
    실행문
elif 조건식:
    실행문
else:
    실행문
"""
val = 10
if val > 10:
    print("값이 10보다 크다")
elif val > 0:
    print("값이 0보다 크다")
else:
    print("값은 0보다 작거나 같다")
#결과 : 값이 0보다 크다. (아래 조건을 만족한다면 elif에서 끝)(:)+indentation잊기말기 
val = 11
if val > 10:
    print("값이 10보다 크다")
    print(f"값은 {val}이다")
elif val > 0:
    print("값이 0보다 크다")
    print(f"값은 {val}이다")
else:
    print("값은 0보다 작거나 같다")
    print(f"값은 {val}이다")
# 값이 0보다 크다
# 값은 10이다

# val = 11일떄
# 값이 0보다 크다
#값이 10보다 크다
#값은 11이다


#%%

pocket = ['paper', 'cellphone', 'money']
# pass : 아무처리를 하지 않고 지나침
# pass 안넣으면 error, if 블럭에는 하나 이상의 실행문이 기술되어야 한다.
# 그런데 아무 처리도 하지 않는 경우 실행문을 생략하고 싶을 떄 pass를 사용한다.
if 'money' in pocket:
    pass
else: 
    print("카드를 꺼내라") 
    
pocket = ['paper', 'cellphone', 'money']
if 'money' not in pocket:
    print('pull out cellphone') 













