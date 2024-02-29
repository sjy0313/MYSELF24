#DataFrame

#매트릭스(matrix)를 이용하여 dataframe 생성

mx <- matrix(c(1, '홍길동', 100,
               2, '이순신', 200, 
               3, '강감찬', 400), nrow=3, byrow=T)
mx

#dataframe
#컬럼명은 자동 부여
emp <- data.frame(mx)
emp
# > emp
#   X1     X2  X3
# 1  1 홍길동 100
# 2  2 이순신 200
# 3  3 강감찬 400

#컬럼이름 변경
colnames(emp) <- c("번호", "이름", "급여")
names(emp)
emp
#   번호   이름 급여
# 1    1 홍길동  100
# 2    2 이순신  200
# 3    3 강감찬  400

#행번호를 통한 데이터 참조
emp[1,]
#   번호   이름 급여
# 1    1 홍길동  100
#열번호를 통한 데이터 참조
emp[,1] # "1" "2" "3"

#범위지정
emp[2:3, 2:3] #2,3행, 2,3열
#     이름 급여
# 2 이순신  200
# 3 강감찬  400

#특정 컬럼의 자료형을 변경
mode(emp$급여) # "character"
emp$급여 <- as.numeric(emp$급여)
mode(emp$급여) # "numeric"
