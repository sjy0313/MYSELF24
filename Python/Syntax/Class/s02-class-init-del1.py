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
# 생성자(constructor) :   __init__(self) 초기화
#   -객체가 생성될 떄 가장 먼저 실행되는 매서드
# 소멸자(destructor)  :  __del__(self) 삭제 / __는(예약된/약속된 속성을 의미)
#   -객체가 소멸될 떄 맨 마지막에 실행되는 매서드

#%%
# 학생 정보를 다루는 전용 클래스
# 속성: 이름, 점수(국어, 영어, 수학) # 자기자신의 식별자 = self(관습적으로 쓰는것임)
# class 만들 떄 class의 첫자는 대문자로 쓰는 것이 관례
class Student:
    def __init__(self, sid= '이름없음', kor=0, eng=0, math=0): 
        print("[생성자], {self}")
        # 생성자(constructor) #속성값을 만들어 준것이기 떄문에 
    # attribute 애러 뜨지 않음. 생성자안에 초깃값을 설정가능 # sid= '애러없음'
        self.sid = sid
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __del__(self): # 소멸자(destructor) 
        print("[소멸자], {self}")
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
        return self.total() // 3 # 맴버의 매서드를 호출: self.매서드()
    
#%%

# 학생(Student) 클래스 선언 (함수 안에서는 self 밖에서는 s1변수 이용)
s1 = Student() # 객체 생성 (s1 = 객체 식별자)
s1.name('길동') # 객체 맴버 매서드에 접근(세터)
#%% 
# 소멸자 호출 방법
# 객체가 생성된 변수에 새로운 객체를 생성
# 2번 이상 연속해서 실행
# 학생(student) 클래스 선언 
s1 = Student('홍길동', 90) # 이름 국어
print(s1.score()) # ('홍길동', 90, 0, 0)

#%%
s1 = Student('감찬', 100, 80) # 이름 국어 영어
print(s1.score(), s1.total(), s1.avg()) # ('감찬', 100, 80, 0) 180 90
#%%
s1 = Student('순신', 100, 80, 90) # 이름 국어 영어 수학
print(s1.score(), s1.total(), s1.avg())# ('순신', 100, 80, 90) 270 90 



