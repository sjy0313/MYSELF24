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
        
    def count(self, val):
        self.cnt += val
        
    def printval(self, val):
        print(f"[A] cnt({self.cnt}), val({val})")

#%%

class B:
    def __init__(self, val):
        self.cnt = val
        
    def count(self, val):
        self.cnt += 1
        
    def printval(self, val):
        print(f"[B] cnt({self.cnt}), val({val})")
        

#%%
# 다중 상속
# 명시하지 않고 부모의 속성이나 메서드를 사용할 떄 기본적으로 선택되는 부모
# 부모는 먼저 상속한 부모의 것을 사용한다.
# 명시적으로 부모 클래스를 지정가능 아래 클래스 C 경우 default class 는 B지만 
# A.count(val)를 활용하여 A클래스의 메서드를 사용할 수 있다.
# 여러 부모에 동일한 이름으로 있는 속성은 하나로 처리한다.
class C(B,A):
    def count(self, val): # 메서드
        A.count(val)
        return self.cnt # 어떤 부모의 속성? 부모(B)

class D(A,B):
    def count(self): 
        return self.cnt # # 어떤 부모의 속성? 부모(A)

#%%
c= C(1)
c.printval(10) # [B] cnt(2), val(10)
print(c.count()) # 오버로딩(중복해서 쓰는 것) # A.count(val) C에서 count를 재정의함.
# TypeError: C.count() missing 1 required positional argument: 'val'
# B의 메서드를 출력할 수 있는가?
# 즉 메서드 오버로딩(중복)을 지원x
#%%
d= D(2)
d.printval(20)# [A] cnt(3), val(20) 
print('count:',d.count()) # count: 3
