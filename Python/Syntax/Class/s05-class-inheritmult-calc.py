# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:08:43 2024

@author: Shin
"""

# [전자] 전자계산기
# 1. 다중 상속을 이용하라
# 2. 사칙연산을 수행하는 클래스를 각각 정의
#   -덧셈/뺄샘/곱셈/나눗셈 클래스
# 3. 최하위 클래스에서 다중상속하여 통합
#   -총합, 평균처리

#%%
class Calculator :
    def __init__(self):
        self.tot = 0
        self.cnt = 0
        self.histories = []
        
    def plus(self, a, b):
        return a + b
    
    def minus(self, a, b):
        return a - b
    
    def times(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            print("Error: Integer ONLY available" )
            return None
        return a / b
    
    def calculate(self,op,*args):
        
     if op == '+':
       result = self.plus(*args)
     elif op == '-':
       result = self.minus(*args)
     elif op == '*':
       result = self.times(*args)
     elif op == '//':
       result = self.divide(*args)
     else:
         print("Error: We do not support any following op")
         return None
     
     self.tot += result
     self.cnt += 1
     
     return result
 
    def total(self):
        return self.tot
    
    def average(self):
        if self.cnt == 0:
            return 0
        return self.tot / self.cnt
    
    def calc(self, a, op, b):        
      c = self.histories(a, op, b)
      if c == None:
          return 0
      self.cnt += 1 
      self.tot += c
      self.histories.append((c, a, op, b)) 
      
      return c 
    
Calculators = Calculator()
Calculators.calculate('+', 5, 3) # 8
Calculators.calculate('*', 4, 3) # 12

print("Total: ", Calculators.total()) # Total:  20
print("Average: ", Calculators.average()) # Average:  10.0
print("Histories:", Calculators.histories)    
    

