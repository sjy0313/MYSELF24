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
#사용자가 파일을 선택해야함
sf <- file.choose()
sf # 선택한 파일 패스 및 파일이름
# student <- read.csv(file="./student.csv", head=F)
student <- read.csv(file=sf, header=F)
student

# 인터넷 주소: URL
read.csv(url) 
url <- "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanic <- read.csv(file=url, header=T)
titanic

#성별에 따른 생존 여부
sursex <- table(titanic$Survived, titanic$Sex)
sursex
#막대 그래프 세로 막대 
help(barplot)
barplot(sursex, col=rainbow(2), main="성별에 따른 생존 여부")
#막대 그래프 가로 막대
barplot(sursex, col=rainbow(2), horiz=T,
        ylab= "생존 및 사망 숫자",
        xlab= "성별",
        main= "성별에 따른 생존 여부")
# horiz 옵션 사용

# 범례
help(legend)
x= 10
y= 10
legend(x, y, c("male", "female"), cex=0.8, fill=rainbow(2))


