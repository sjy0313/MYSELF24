#matrix: 2차원 배열구조 
#행렬 자료 구조의 특징
#동일한 자료형 데이터만을 저장
#함수 : matrix(), rbind(), cbind(), apply()

# 열우선으로 값을 채운다(열단위)
#6행 1열 매트릭스 객체
mx <- matrix(c(1:6))
mx

# 2행 3열
# nrow: 행의 개수
m23 <- matrix(c(1:6),nrow=2)
m23

# 3행 2열
m32 <- matrix(c(1:6),nrow=3)
m32

#배수가 맞지 않으면? 
#처음 시작값부터 반복
#4행 2열 
m42 <- matrix(c(1:6),nrow=4)
m42 # 1-6 다시 처음부터 counts 

#4행 3열 : 12개 
#생성된 값은 11개. 처음값 10이 반복
m43 <- matrix(c(10:20),nrow = 4)
m43

#4행 5열 : 20개
cv <- c(1:18, 30, 40)
m45 <- matrix(cv, nrow = 4)
m45


                           