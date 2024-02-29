# matrix
# 행렬 처리 함수 : apply()

help(apply)
#apply(X, MARGIN, FUN, ..., simplify = TRUE)
# X : 행렬개체
# MARGIN : 1: 행단위 /  2: 열단위
# FUN: 행렬 자료에 적용할 함수

mx <- matrix(data=1:12, nrow=3, ncol=4, byrow=F) # 열우선
mx
#       [,1] [,2] [,3] [,4]
# [1,]    1    4    7   10
# [2,]    2    5    8   11
# [3,]    3    6    9   12

# 행 단워 최대값
apply(mx,1,max) # 10 11 12
# 열 단워 최대값
apply(mx,2,max) # 3 6 9 12

#합계 : sum
apply(mx, 1, sum) # 행 단위 합계: 22 26 30
apply(mx, 2, sum) # 열 단위 합계: 6 16 24 33

#평균: mean
apply(mx,1, mean) #행단위 5.5 6.5 7.5
apply(mx,2, mean) #열단위 2 5 8 11