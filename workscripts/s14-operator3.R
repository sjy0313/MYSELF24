# 산술 연산자
# 연산을 수행하는 두 대상의 요소의 갯수가 일치하지 않으면 처음 요소부터 반복한다.
# x %in% v : v에 존재하는가? 결과는 존재(TRUE), 존재하지 않으면(FALSE)
a <- c(0,2,4)
b <- c(1,2,3)
#백터 연산은 같은 인덱스 요소끼리 연산을 수행하여 
#요소의 갯수 만큼 백터를 리턴한다
c <- a+b
c # 1 4 7

d <- a - b
d# -1 0 1

eq <- a & b
eq # FALSE TRUE TRUE 

land <- a & b
land # FALSE TRUE TRUE

# x %in% v
in3 <- 3 %in% a 
in3 # FALSE

# a : 0 2 4 5 
# b : 1 2 3
inx <- b %in% a
inx # FALSE TRUE FALSE


