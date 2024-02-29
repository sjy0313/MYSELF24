#연습문제

#[문제]
#백터(vector) n의 만들고 연속된 숫자의 
#홀수의 합과 짝수의 합을 각각 구하라.
v <- c(2,1,4,5,3,6,9,8)

c(1:8) # 1 2 3 4 5 6 7 8

#홀수의 합을 구하는 함수
# x: 합을 구할 백터 
# opt: 짝수(0) , 홀수(1) #나머지
oddsum <- function(x)  
sumx <- function(x, opt) 
  
s <- 0　#총합
l <-length(v) #백터의 길이
 
  #
  for (n in c(1:l))  #for= 반복문 l의 길이 만큼 반복
   y <- v[n]
   if(y %% 2== opt) # 나머지 연산
     s <- s + y

return(s)
#홀수의 합
oddsum(v) # 1 5 3 9 <- 18
#짝수의 합
even <- sumx(v,0)

v <- c(1:10)
#
# v
# [1]  1  2  3  4  5  6  7  8  9 10

# sum_odd <- ((sum)seq[1,length(n),2])
# sum_odd <- sum(n[seq(1, length(n), 2)])
# sum_odd 25
# sum_even <- sum(n[seq(2, length(n), 2)])
# sum_even 30

#답안
n <- 10 # 백터 n
s <- 1 # 시작값
v <- c(s:n) # 백터
l <- length(v) # 백터의 길이

#홀수의 합
odd <- seq(s,l,1) 
sum(v[seq(s,l,2)]) # 25
sum(seq(s,l,2)) #25
sum(odd) #25
#짝수의 합
even <- seq(s+1,l,2) 
sum(v[seq(s+1,l,2)]) # 30
sum(even) #30


#[문제2]
#1부터 16까지 백터 값을 Matrix 4행 4열 생성하라.
#행 단위로 각 행의 최대값 구하기
#열 단위로 각 열의 최대값 구하기
#행 단위 합계
#열 단위 합계
#행 단위 평균
#열 단위 평균

# 답안
# 요소의 수
length(mx) # 16
nrow(mx) # 4행 nrow(mx) # 4열

mx44 <- matrix(c(1:16), nrow=4) 
mx44 <- matrix(1:16, nrow=4, ncol=4)


mx44
#      [,1] [,2] [,3] [,4]
# [1,]    1    5    9   13
# [2,]    2    6   10   14
# [3,]    3    7   11   15
# [4,]    4    8   12   16

#행 단위로 각 행의 최대값 구하기
max_row <- apply(mx44, MARGIN=1, max)
max_row # 13 14 15 16
#열 단위로 각 열의 최대값 구하기
max_col <- apply(mx44, MARGIN=2, max)
max_col # 4  8 12 16

#ex.
sum_row <- sum(mx44[1,c(1:4)]) = sum(mx44[1,])
sum_row # 28
sum_row2 <- sum(mx44[2,])
sum_row2 # 32
#행 단위 합계
apply(mx44, 1, sum)
# 28 32 36 40
#열 단위 합계
apply(mx44, 2, sum)
# 10 26 42 58
#행 단위 평균
apply(mx44, 1, mean)
# 7  8  9 10
#열 단위 평균
apply(mx44, 2, mean)
# 2.5  6.5 10.5 14.5

# 전체합계
sum_row2 <- sum(mx44[c(1:4),c(1:4)])
sum_row2 136


#[문제3]
#백터 1부터 12까지 12개의 요소로 구성된 
#3행 * 2열 * 2면의 array 만들고 아래의 계산을 하라 
#각면의 행의 합계
#각면의 열의 합계

c12 <- c(1:12) #백터 
adm <- c(3, 2, 2) #차원 3행 * 2열 * 2면
ax <- array(c12, adm) #배열
ax
#or 
arfx <- array(1:12, dim = c(3,2,2))
arfx
# , , 1
# 
#       [,1] [,2]
# [1,]    1    4
# [2,]    2    5
# [3,]    3    6
# 
# , , 2
# 
#       [,1] [,2]
# [1,]    7   10
# [2,]    8   11
# [3,]    9   12
# 면 참조
a1 <- ax[,,1] # 1면
a2 <- ax[,,2] # 2면

# 각면의 행의 합계
apply(a1, MARGIN=1, sum)
apply(a2, MARGIN=1, sum)

arfx <- array(1:12, dim = c(3,2,2))
sum1 <- apply(arfx, c(3,1), sum)

# c(3, 1)으로 apply() 함수에 적용하면, 먼저 세 번째 차원을 따라 합계를 계산하고, 
# 그 후에 첫 번째 차원을 따라 추가적인 합계를 계산합니다. 

sum1
#       [,1] [,2] [,3]
# [1,]    5    7    9 
# [2,]   17   19   21
#각 면의 열의 합계
sum2 <- apply(arfx, c(3,2), sum)
sum2
#       [,1] [,2]
# [1,]    6   15
# [2,]   24   33

#각 면의 총합
sum(apply(a1, MARGIN=1, sum)) #1면의 총합
