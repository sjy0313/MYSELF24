# 액셀 파일 불러오기 (e)
install.packages("readxl")
library(readxl)

df_exam <- read_excel("excel_exam.xlsx") # 양쪽에 "가 들어가야하며 확장자인 (.xlsx)까지 기입되어야함)
df_exam
#R에서 파일명을 지정할 떄 항상 앞뒤에 따옴표를 넣습니다, 다른 폴더에 있는 파일을 불러오려면 경로 지정이 필요
 #(예시)df_exam <- read_excel("d:/easy_r/excel-exam.xlsx")
# col_names = F 첫번 쨰 행을 변수 명이 아닌 데이터로 인식해 불러오고 변수명은 숫자로 자동 지정
df_exam <- read_excel("d:/easy_r/excel-exam.xlsx", col_names = F)

# 여러개의 시트로 구성된 파일 불러올 떄
df_exam_sheet <- read_excel("excel_exam_sheet.xlsx", sheet = 3)# sheet parameter를 이용해 몇번 쨰 시트의 데이터 불러올건지 지정가능

# csv 파일 불러오기( 데이터를 불러올 떄 용량이 작기 때문에 자주 이용)
df_csv_exam <- read.csv("csv_exam.csv")
df_csv_exam

# r 내장 함수인 write.csv()로 파일 저장 
write.csv(df_midterm, file = "df_midterm.csv") # file parameter로 파일명 지정/ header=F 변수명 없는 CSV파일 불러올떄

# rm() 데이터 삭제 할 때 () 

df_csv_exam <- read.csv("csv_exam.csv")
df_csv_exam


head(df_csv_exam) # 처음 부터 6행까지 출력
head(df_csv_exam,10) 

tail(df_csv_exam) # 마지막 부분 6행 출력
view(df_csv_exam) # 데이터 확인 창
edit(df_csv_exam) # 수정 창
dim(df_csv_exam) # 차원 출력 -> 20행 5열
summary(df_csv_exam) # 요약 통계량 산출하기
str(df_csv_exam) #데이터 속성파악







