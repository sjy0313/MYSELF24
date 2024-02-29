#DataFrame
# -데이터베이스의 테이블 구조 
# -column 단위
# -mix of list and vector
# -column은 list
# -column내의 데이터는 백터 자료구조
# 기타:
# - 각 칼럼의 행의 갯수가 일치 하지 않으면 애러를 출력하고 
# - 일치되는 갯수만 지정되며 나머지는 무시된다.
# - 가장 작은 행으로 지정된다.
#컬럼
no <- c(1,2,3)
name <- c('Kim', "Lee", "Chol")
pay <- c(200,300,400)
# ex no에 4 name에 cho추가 시 무시됨
#dataframe 
emp <- data.frame(No=no, Name=name, Pay=pay)
emp
#   No  Name  Pay
# 1  1  Kim   200
# 2  2  Lee   300
# 3  3 Chol   400
# 
# mode(emp) #list" 자료
# class(emp) #data.frame" 구조
# str(emp) #객체의 자료형을 문자열로 변환 출력
# 'data.frame':	3 obs. of  3 variables:
#  $ No  : num(ber)  1 2 3
#  $ Name: chr(acter)  "Kim" "Lee" "Chol"
#  $ Pay : num(eric)  200 300 400

#컬럼의 갯수
ncol(emp) # 3
#행의 갯수
nrow(emp) # 4
#컬럼명
names(emp) # "No" "Name" "Pay"
#요약: 데이터
summary(emp)
#      No          Name                Pay     
# Min.   :1.0   Length:3           Min.   :200  
# 1st Qu.:1.5   Class :character   1st Qu.:250  
# Median :2.0   Mode  :character   Median :300  
# Mean   :2.0                      Mean   :300  
# 3rd Qu.:2.5                      3rd Qu.:350  
# Max.   :3.0                      Max.   :400 

#참조: 컬럼
emp$No # 1 2 3 4 
emp$Name # "Kim"  "Lee"  "Chol"
emp$Pay # 200 300 400
