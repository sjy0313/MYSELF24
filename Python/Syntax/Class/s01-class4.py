# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:53:09 2024

@author: Shin
"""

#클래스(class) = 사용자가 만들어내 자료형
# 객체지향 프로그래밍: 객체, 인스턴스
# 클래스: 속성, 함수를 하나의 묶음으로 처리
# 속성: 동일한 자료들의 그룹, 맴버 변수, 공개(정보은폐를 지원x)
# 함수: 맴버 함수, 매서드, 맴버 변수에 접근할 수 있는 함수
# self: 생성된 객체의 식별자 
# 매서드를 호출할 떄는 self를 생략
# 맴버변수(속성):
#   -맴버변수가 생성: self.이름 = 초깃값
#   -맴버변수가 참조: self.이름
# 생성자(constructor)
#   -객체가 생성될 떄 가장 먼저 실행되는 매서드


#%%
# 학생 정보를 다루는 전용 클래스
# 속성: 이름, 점수(국어, 영어, 수학) # 자기자신의 식별자 = self(관습적으로 쓰는것임)
# class 만들 떄 class의 첫자는 대문자로 쓰는 것이 관례
class Student:
    def __init__(self): # 생성자(constructor) #속성값을 만들어 준것이기 떄문에 
    # attribute 애러 뜨지 않음.
        self.sid = '이름없음'
        self.kor = 0
        self.eng = 0
        self.math = 0
  # 전형함수(함수내부적으로 처리)      
    def name(self, val):
        self.sid = val
    
    def korean(self, val):
        self.kor = val
    
    def english(self, val):
        self.eng = val
        
    def maths(self, val):
         self.math = val
         
    def score(self):
        return self.sid, self.kor, self.eng, self.math
    
    def total(self):
        return self.kor + self.eng + self.math
    
    def avg(self):
        #return total() /3 (x)
        return self.total() / 3 # 맴버의 매서드를 호출: self.매서드()
    
#%%
# 학생(Student) 클래스 선언 (함수 안에서는 self 밖에서는 s1변수 이용)
s1 = Student() # 객체 생성 (s1 = 객체 식별자)
s1.name('길동') # 객체 맴버 매서드에 접근(세터)

s2 = Student()
s2.name('순신')
# 객체의 속성값을 접근하여 변경 가능 
s1.sid = '고길동' 
s2.sid = '고길동' 
print('s1:', s1.sid) # s1: 고길동
print('s2:', s2.sid) # s2: 순신
# 서로 다른 객체(id가 다르다)
print("s1 == s2 ?", s1 == s2) # s1 == s2 ? False
#%%
# ID 가 다름.
print(type(s1), hex(id(s1)), s1)
print(type(s2), hex(id(s2)), s2) 

