#자료형
#숫자형(Numeric): 0, 123 , -1234
#문자형(String): : "a" , "abc", 'ABC'
#논리형(Logical) : TRUE, FALSE , T, F
#결측: NA(Not a Available), NaN(Not a Number) NA=값이 존재X 
#무한값: Inf, -Inf
#정의되지 않은 값: NULL
#숫자형(Numbeic)
n <- 22
is.numeric(n) #TRUE
#문자형(string)
s1 <- "신정윤"
s2 <- '홍길동'
s3 <- "홍길동은 '신정윤'의 조상이다"
s4 <- '신정윤은 "홍길동"의 후손이다'
is.character(s1) #TRUE
is.character(s2) #TRUE
is.character(s3) #TRUE
is.character(s4) #TRUE
#논리형(Logical)
t1 <- TRUE
t2 <- T
f1 <- FALSE
f2 <- F
is.logical(t1) #TRUE
is.logical(t2) #TRUE
is.logical(t3) #TRUE
is.logical(t4) #TRUE
# 자료형이 일치하지 않으면 FALSE
is.numeric("홍길동")

#NA(Not a Available), NaN(Not a Number)
x <-  NA
is.na(n) #FALSE
is.na(s1) #FALSE
is.na(NA) #TRUE
IS.na(x) #TRUE
#NAN(Not a Number)
is.nan(n) #FALSE
is.nan(t1) #FALSE
is.nan(s1) #FALSE
is.nan(x) #FALSE
is.nan(NAN) #TRUE
is.nan(Inf) #FALSE
s= "홍길동"
is.nan(s) #FALSE
is.nan(10) #FALSE

is.nan("홍길동") #FALSE
#문자는 판단할 수 없음 그러므로 숫자형으로 변환 후 판단 
hn <- as.numeric("홍길동") #NA
is.nan(as.numeric("홍길동")) #강제형변환에 의해 생성된 NA 입니다 
l <- 99 
is.numeric(l) #TRUE
is.integer(l) #FALSE, 정수는 아니다
is.double(l) #TRUE, 실수형

nl <- 99L #정수형
is.intiger(nl) #TRUE

xl <- as.integer(l) #형변환 : as.자료형(변수)
is.integer(xl) #TRUE

