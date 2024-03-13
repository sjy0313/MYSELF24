# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:53:09 2024

@author: Shin
"""

#클래스(class)
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
    
#%%
# 학생(Student) 클래스 선언
s1 = Student() # 객체 생성 (s1 = 객체 식별자)
print(s1.score()) # ('이름없음', 0, 0, 0)
#%%

# 객체 식별자가 없기 떄문에 출력 안됨.
Student.score() 
# TypeError: Student.score() missing 1 required positional argument: 'self'
Student.score(s1) # ('이름없음', 0, 0, 0)

#%%

s1.name('길동') # 객체 맴버 매서드에 접근(세터)
s1.korean(90) # 매서드를 호출할 떄는 self를 생략
s1.english(80)
s1.maths(70)
print(s1.score())  # ('길동', 90, 80, 70)
print(Student.score(s1)) # ('길동', 90, 80, 70)
