# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:53:09 2024

@author: Shin
"""

#클래스(class) : 상속(inheritance)

#정의
"""
class 자식클라스(부모클라스):
    ...
"""

#%%

class Student:
    def __init__(self, sid= '이름없음', kor=0, eng=0, math=0): 
        print(f"[Student]생산자: {self}")
        # 생성자(constructor) #속성값을 만들어 준것이기 떄문에 
    # attribute 애러 뜨지 않음. 생성자안에 초깃값을 설정가능 # sid= '이름없음'
        self.sid = sid
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __del__(self): # 소멸자(destructor) 
        print("f[Student]소멸자: {self}")
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
# 상속
# 자신의 생성자를 정의하면 
# 더 이상 부모의 생성자가 자동으로 호출되지 않는다.
class School(Student):
    def __init__(self):
        print(f"[School] 생산자 {self}")

#%%

# 학교 클라스
# school 생성자가 생겼지만 출력값 attribute error 속성값들이 안만들어짐.
# 자식이 생성자를 정의하여 더 이상 부모의 생성자가 자동으로 호출되지 않아
# 자식 생성자에 정의 되어 있는 속성들이 만들어지지 않는다.
# 그래서 아래와 같은 오류 발생.
# 해결법은 자식 생성자에 속성값 할당/ 부모 속성값 호출
# AttributeError: 'School' object has no attribute 'sid'
sc = School()
print(sc.score()) # ('애러없음', 0, 0, 0)
#%%

sc= School('전교생')
print(sc.score()) # ('전교생', 0, 0, 0)
#%%
# 학생(Student) 클래스 선언 (함수 안에서는 self 밖에서는 s1변수 이용)
s1 = Student() # 객체 생성 (s1 = 객체 식별자)
s1.name('길동') # 객체 맴버 매서드에 접근(세터)
#%% 
s1 = Student('홍길동', 90) # 이름 국어
print(s1.score()) # ('홍길동', 90, 0, 0)

#%%
s2 = Student('감찬', 100, 80) # 이름 국어 영어
print(s2.score(), s2.total(), s2.avg()) # ('감찬', 100, 80, 0) 180 90
#%%
s3 = Student('순신', 100, 80, 90) # 이름 국어 영어 수학
print(s3.score(), s3.total(), s3.avg())# ('순신', 100, 80, 90) 270 90 



