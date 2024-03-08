# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:07:01 2024

@author: Shin
"""

#문제
# 지갑에 아래와 같은 돈을 가지고 있다
# 총금액 얼마인가 
# 각각의 금액을 변수에 담아서 연산을 수행하라
# 1만원 4장
# 1000원을 3장 
# 100원 9개
# 10원 6개 

a = 10000 * 4
b = 1000 * 3
c = 100 * 9
d = 10 * 6
total = 10000 * 4 + 1000 * 3 + 100 * 9 + 10 * 6 
e = a+b+c+d
print(e)
print(total) # 43960
# 총금액에서 15000원짜리 2개를 지출하고 남은 금액은 얼마인가 
spent = 15000 * 2
print(total-spent)
 # 13960
# 한달 급여가 400만 
# 분기별 보너스는 월급여의 30% 지급
# 세금은 월 급여의 3%
# 보너스에 대한 세금X 
# 월 세후 수령액은 얼마? 
# 연 총세금은 얼마? 
# 세후 연수령액은 얼마? 
salary = 400
bonus = salary * (3/10) # bonus = salary * 0.3
tax = salary * (3/100)  # tax = salary * 0.03
# 월 세후 수령액 
print(salary-tax) # 388.0
# 보너스
print(salary * (3/10)) # 120.0
# 연 총세금
print(tax * 12) # 144.0
# 세후 연수령액
print((salary-tax) * 12 + bonus * 4) #5136
 















