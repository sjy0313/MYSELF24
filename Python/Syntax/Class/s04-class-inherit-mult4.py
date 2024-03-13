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
        print(f"[A] self({self}), count={self.cnt}")
             
    def printval(self, val):
        print(f"[A] cnt({self.cnt}), val({val})")

#%%

class B:
    def __init__(self, val):
        self.cnt = val
        
    def count(self, val):
        self.cnt += 1
        print(f"[B] self({self}), count={self.cnt}")
    def printval(self, val):
        print(f"[B] cnt({self.cnt}), val({val})")
        

#%%
# 다중 상속
# 명시하지 않고 부모의 속성이나 메서드를 사용할 떄 기본적으로 선택되는 부모
# 부모는 먼저 상속한 부모의 것을 사용한다.
# 명시적으로 부모 클래스를 지정가능 아래 클래스 C 경우 default class 는 B지만 
# A.count(val)를 활용하여 A클래스의 메서드를 사용할 수 있다.
# 명시적으로 부모 클래스를 지정 : 부모클래스.메서드(self, ...)
# 여러 부모에 동일한 이름으로 있는 속성은 하나로 처리한다.
class C(B, A):
    def count(self, val):
        print(f"[C] self({self}), count={self.cnt}")
        A.count(self, val) # 잊지말고 self 주기(명시적으로 부모지정)
        # 메서드는 명시적지정 가능(self)
        # 다중상속인 경우 명시적으로 부모를 지정해야함.
        #super().count(val) # 부모의 카운트로가라 (안됨.)
        return self.cnt # 어떤 부모의 속성? 부모(B)

class D(A,B):
    def count(self):
        B.count(self)
        return self.cnt # # 어떤 부모의 속성? 부모(A)

#%%
# self: A, B, C의 인스턴스가 하나이다. 즉 C의 인스턴스이다. # __main__.C
c= C(1)
cnt = c.count(7) # C-> A
# [C] self(<__main__.C object at 0x0000018241411ED0>), count=1
# [A] self(<__main__.C object at 0x0000018241411ED0>), count=8
c.printval(10) # [B] cnt(8), val(10)
print('cnt=', cnt) # cnt= 8
#%%

