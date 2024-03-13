# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:15:25 2024

@author: Shin
"""

# 다중상속
# 상속: 속성, 메서드를 상속
# 상속된 부모 클래스에서 동일한 메서드가 있으면? (기본적으로 선택되는 클래스는 첫번 쨰임)
# 원하면 두번 쨰 클래스도 선택하여 메서드 및 속성 활용가능 
# -> 먼저 상속된 클래스의 메서드가 사용됨.
# -> 먼저 상속된 클래스의 속성을 사용한다
#%%
# ex.
class A:
    def __init__(self, val):
        self.cnt = val
        
    def printval(self, val):
        self.cnt += 1 
        print(f"[A] cnt({self.cnt}), val({val})")
#%%

class B:
    def __init__(self, val):
        self.cnt = val
    
    def printval(self, val):
        self.cnt += 1 
        print(f"[B] cnt({self.cnt}), val({val})")
        

#%%
# 다중 상속
# 명시하지 않고 부모의 속성이나 메서드를 사용할 떄 기본적으로 선택되는 부모
# 부모는 먼저 상속한 부모의 것을 사용한다.
class C(B,A):
    def count(self): # 메서드
        return self.cnt # 어떤 부모의 속성? 부모(B)

class D(A,B):
    def count(self): 
        return self.cnt # # 어떤 부모의 속성? 부모(A)

#%%
c= C(1)
c.printval(10) # [B] cnt(2), val(10)
print(c.count()) # 2
#%%
d= D(2)
d.printval(20)# [A] cnt(3), val(20) 
print('count:',d.count()) # count: 3
