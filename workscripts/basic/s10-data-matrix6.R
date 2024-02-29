# <- <- <- <- <- <- <- <- <- <- <- <- 

help(matrix)

#3행 4열, 행우선
#data: 매트릭스에 지정할 값
#nrow: 행의 개수
#ncol: 열의 개수
#byrow: 행우선 유무 ,기본(FALSE) 열우선
mx <- matrix(data=1:12, nrow=3, ncol=4, byrow=T)
mx
#       [,1] [,2] [,3] [,4]  
# [1,]    1    2    3    4
# [2,]    5    6    7    8
# [3,]    9   10   11   12


length함수
my_list <- list("apple", "banana", "cherry")
length(my_list)  # 리스트의 길이 출력

mat <- matrix(1:6, nrow = 2, ncol = 3)
mat

length(mat)  # 행렬의 길이 (전체 요소 수) 출력

df <- data.frame(x = c(1, 2, 3), y = c("a", "b", "c"))
length(df)  # 데이터프레임의 길이 (열의 개수) 출력
