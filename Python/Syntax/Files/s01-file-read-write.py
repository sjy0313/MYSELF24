# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:03:34 2024

@author: Shin
"""

# 파일 입출력
#
#[문제]
#1. 국어/영어/수학/과학 점수를 텍스트 파일로 생성
#   -아래와 같이 텍스트 편집기로 작성
#   예시) 
    #이름  국어,영어,수학,과학
    #홍길동 100,90,80,70
    #이순신 100,90,80,70
    #강감찬 100,90,80,70

#2. 생성된 파일을 읽어서 총점, 평균을 구한다.
#   예시) 
    #이름  국어,영어,수학,과학,총점,평균
    #홍길동 100,90,80,70,340,85
    #이순신 100,90,80,70
    #강감찬 100,90,80,70
#3. 위에서 처리한 성적을 새로운 파일에 저장한다.
#4. 파일이 없는 경우 예외처리를 한다.
#5. 해당 코드를 일반 함수를 만들어 코딩한다.
#6. 위 5번의 함수를 클래스로 변경한다.
#7. 처리한 파일 이름을 외부에서 임의로 지정하여 처리한다.
# - p183 참조 
#   - 파일(score.txt) 읽어서 성적처리 결과 파일(score-result.txt) 생성
#   - python score.txt score-result.txt


# 1.
# 파일 읽기 함수: 파일을 라인 단위로 전체를 한 번에 읽어서 리턴
# 리스트 = 파일객체.readlines()
scores_file = open("./scores.txt", 'w', encoding="utf8")
scores_file.write("이름 국어 영어 수학 과학")
scores_file.close()

scores_file = open("./scores.txt", 'a', encoding="utf8")
scores_file.write("\n홍길동 100 90 80 70")
scores_file.write("\n강감찬 70 60 50 90")
scores_file.write("\n홍길동 45 60 80 70")
scores_file.write("\n을지문덕 50 70 95 75")
scores_file.write("\n")
scores_file.close()
#with문이 실제 동작은 이렇습니다. with문에 진입할 때
#객체의 __enter__ 함수를 호출합니다. 그리고 with문이 종료될 때
#__exit__함수를 호출합니다. 그래서 이 두 함수를 정의하면 with문에서
#사용할 수 있는 객체를 만들 수도 있습니다.

with open("./scores.txt", 'a', encoding="utf8") as scores_file:
    scores_file.write("\n[다음은 점수에 대한 총점과 평균값에 대한 데이터입니다]\n")
    
scores_file = open("./scores-result.txt", 'a', encoding="utf8")
scores_file.write("이름 총점 평균")
scores_file.write("\n홍길동 ")
scores_file.write("\n강감찬 )
scores_file.write("\n홍길동 )
scores_file.write("\n을지문덕 ")
scores_file.write("\n")
scores_file.close()  
try:

    with open("./scores.txt", 'r', encoding="utf8") as editable:
        results = editable.read()
    with open("./scores-result.txt",'a', encoding='utf-8') as editable:
        editable.write(results)
    
        print("scores-result.txt 파일의 내용이 scores.txt 파일에 추가되었습니다.")
except FileNotFoundError:
    print("찾으시는 파일이 없습니다.")



# scores-result.txt 파일의 내용을 scores.txt 파일에 추가
input_file = "scores-result.txt"
output_file = "scores.txt"
append_file(input_file, output_file)






        



"""
def totalavg(scores):
    histories = [] # 히스토리: 표현식 전체를 이력처리
    total = 0      # 총합누적
    count = 0      # 연산횟수
    def plus(self, a, b):
        return a + b
    
    
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
     
     return c  self.tot += result
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
   
#%%



class Student:
    def __init__(self, sid= '애러없음', kor=0, eng=0, math=0): 
        self.sid = sid
        self.kor = kor
        self.eng = eng
        self.math = math
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

s1 = Student() # 객체 생성 (s1 = 객체 식별자)
s1.name('길동') # 객체 맴버 매서드에 접근(세터)
#%% 
s1 = Student('홍길동', 90) # 이름 국어
print(s1.score()) # ('홍길동', 90, 0, 0)

#%%
s2 = Student('감찬', 100, 80) # 이름 국어 영어
print(s2.score(), s2.total(), s2.avg())
#%%
s3 = Student('순신', 100, 80, 90) # 이름 국어 영어 수학
print(s3.score(), s2.total(), s2.avg())






