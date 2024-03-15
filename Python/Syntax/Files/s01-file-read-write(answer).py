# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:52:21 2024

@author: Shin
"""

# 파일 입출력
# 
# [문제]
# 1. 이름,국어,영어,수학,과학 점수를 텍스트 파일로 생성
#    - 아래와 같이 텍스트 편집기로 작성
#    예시) 
#        이름,국어,영어,수학,과학
#        홍길동,100,90,80,70
#        이순신,100,90,80,70
#        강감찬,100,90,80,70
#
# 2. 생성된 파일을 읽어서 총점, 평균을 구한다.
#        이름,국어,영어,수학,과학,총점,평균
#        홍길동,100,90,80,70,340,85
#        이순신,100,90,80,70,340,85
#        강감찬,100,90,80,70,340,85
#
# 3. 위에서 처리한 성적을 새로운 파일에 저장한다.
# 4. 파일이 없는 경우 예외처리를 한다.
# 5. 해당 코드를 일반 함수를 만들어 코딩한다.
# 6. 위 5번의 함수를 클래스로 변경한다.
# 7. 처리한 파일 이름을 외부에서 임의로 지정하여 처리한다.+
#    - 교제 페이지(183) 참조
#    - 파일(score.txt)을 읽어서 성적처리 결과 파일(score-result.txt) 생성
#    - python score.txt score-result.txt
# 
# sys 라이브러리는 파이썬 인터프리터(코드를 작성하고 실행하는데 필수적인 도구)를 제어하는데 사용


# 데이터 정제
# 리스트의 각 요소에서 '\n' 제거해서 새로운 리스트 리턴
#%%
# 절차형/ 구조형/ 객체지향/ 함수형 프로그래밍
#%%
#객체와 클래스
#객체 지향 프로그래밍에서의 객체는 다음과 같이 정의된다.
#객체(Object) = 속성(Attribute) + 기능(Method)
#속성은 사물의 특징을 말한다.자동차로 예를 들면, 몸체의 색, 바퀴의 크기, 
#엔진의 배기량 등이 자동차의 속성이라 할 수 있다. 기능은 어떤 것의 특징적인 동작을 말한다.
#다시 자동차로 예를 들면, 전진, 후진, 좌회전, 우회전등이 자동차의 기능이라고 할 수 있다!
#속성을 ‘변수’, 기능을 ‘함수’로 바꿔 ‘객체 = 변수 + 함수’라고 할 수 있다.
#%%
#%%

import sys

def stripNewLine(lst):
    splist = lst.split(',') # 콤마 분리
    result = []
    for sl in splist:
        col = sl.rstrip('\n')
        result.append(col)

    return result


#%%
# 예외처리
# Exception 변수를 상속시켜 예외처리
class StudentScoreError(Exception):
    pass

#%%

# 클래스    
class StudentScore:

    def __init__(self, rf, wf):
        self.students = []
        self.rfile = None # 속성값 생성
        self.wfile = None
        
        try: # None 이 아닌 값들만 오픈
            self.rfile = open(rf, 'r', encoding='utf8') 
        except FileNotFoundError as e:
            raise StudentScoreError(f"성적처리 파일 오픈 실패({rf})")

        try:
            self.wfile = open(wf, 'w', encoding="utf8")
        except FileNotFoundError as e:
            raise StudentScoreError("성적처리 파일 오픈 실패({wf})")

    def compute(self): 
        self.readColumns() # 내부에서 사용하는 메서드
        self.readScores()
        self.calcScore()
        self.writeScore()

    def readColumns(self): # 외부에서 사용하는 함수
        # 컬럼이름 읽기
        cols = self.rfile.readline()
        if cols:
            self.students.append(stripNewLine(cols))
            self.students[0] += ['총점', '평균']
            print(self.students[0])

    def readScores(self):
        # 성적파일 읽기
        while True:
            txtline = self.rfile.readline()
            if not txtline:
                print("\n[end of file]")
                break
        
            student = stripNewLine(txtline)
            self.students.append(student)
            print(student)

    def calcScore(self):
        # 성적처리
        for cnt in range(1, len(self.students)):
            student = self.students[cnt]
            n = student[0]
            k = int(student[1])
            e = int(student[2])
            m = int(student[3])
            s = int(student[4])
            t = k + e + m + s
            a = t // 4
            student.append(str(t))
            student.append(str(a))
            print(student)
    
    def writeScore(self):
        # 성적처리 결과 저장
        for student in self.students:
            data = ','.join(student)
            print(data, file=self.wfile)
            
    def closeAll(self):
        if self.rfile != None:
            self.rfile.close()      
            self.rfile = None
            
        if self.wfile != None:
            self.wfile.close()      
            self.wfile = None

#%%
# 결과 리스트
students = [] 

#%%
try:
    stf = open("./student.txt", 'r', encoding='utf8') 
    
    # 컬럼이름 읽기
    cols = stf.readline()
    if cols:
        students.append(stripNewLine(cols))
        students[0] += ['총점', '평균']
        print(students[0])
except FileNotFoundError as e:
    print("[예외발생]", e)
    sys.exit(0)

#%%

# 성적파일 읽기
while True:
    txtline = stf.readline()
    if not txtline:
        print("\n[end of file]")
        break

    student = stripNewLine(txtline)
    students.append(student)
    print(student)
    
stf.close()
 
#%%

# 성적처리
for cnt in range(1, len(students)):
    student = students[cnt]
    n = str(student[0])
    k = int(student[1]) 
    e = int(student[2])
    m = int(student[3])
    s = int(student[4])
    t = k + e + m + s
    a = t // 4
    student.append(str(t))
    student.append(str(a))
    print(student)
    
#%%

# 성적처리 결과 저장
wf = open("./student-result.txt", 'w', encoding="utf8")
for student in students:
    data = ','.join(student) # 콤마삽입
    print(data, file=wf)
wf.close()      
#%%
# 처리한 파일 이름을 외부에서 임의로 지정하여 처리한다
#try (해당 구문 안에서 에러 발생 시 처리 가능 - 필수)
#except (에러 발생시 수행 - 선택이지만 에러를 처리하려면 필수)
#else (에러 없을 때 수행 - 선택이지만 except 없이는 올 수 없음)
#finally (에러가 있거나 없거나 상관없이 항상 수행 - 선택)

import studentscore as sc
# 내부에서 파일 임의로 지정
rfile = "./student.txt"
wfile = "./student-result.txt"

try:
    #객체(Object) = 속성(Attribute) + 기능(Method)
    students = sc.StudentScore(rfile, wfile)
    students.compute()
except sc.StudentScoreError as e:
    print("[예외발생]", e)
finally:
    if students != None: # rf이 닫히지 않은 상태로 wf가 열리게 할 떄를 대비
         students.closeAll()