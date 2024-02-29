# 엑셀 파일 읽기

# 패키지 설치 및 로딩
install.packages("readxl")
library(readxl)
# 도움말
help(read_excel)

#처음 시트를 읽음
student <- read_excel("./student.xlsx")
student

#시트 이름 지정 (sheet= 엑셀시트이름)
general <- read_excel("./student.xlsx", sheet="장군")
general

# 엑셀로 쓰기
install.packages("openxlsx")

install.packages("writexl")
library(writexl)
#엑셀로 쓰기
write_xlsx(student, path="./student-wt.xlsx")

#엑셀로 쓰기 : 컬럼을 생략하고 데이터만 저장
write_xlsx(student, path="./student-wt-nocolnames.xlsx", col_names=F)

#파일 읽기

# read.csv() 함수
help("read.csv")
#파일 선택 다이얼로그 박스
sf <- file.choose()
# student <- read.csv(file="./student.csv", head=F)
student <- read.csv(file=sf, header=F)
student
