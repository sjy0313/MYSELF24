# 결측치(Missing value)즉 누락된 값 찾기 및 확인하기 

df <- data.frame(sex = c("M", "F", NA, "M", "F"),
               score = c(5, 4, 3, 4, NA))
df
#    sex score
# 1    M     5
# 2    F     4
# 3 <NA>     3
# 4    M     4
# 5    F    NA

# is.na(df) 결측치 확인하기  / !is.na를 입력하면 결측치가 아닌 값을 의미
#        sex score
# [1,] FALSE FALSE
# [2,] FALSE FALSE
# [3,] FALSE FALSE
# [4,] FALSE FALSE
# [5,] FALSE  TRUE

# table(is.na(df)) 결측치 빈도 출력 
# FALSE  TRUE 
#   9     1
# 항목별 결측치 빈도 출력
table(is.na(df$sex))
# FALSE 
# 5 
table(is.na(df$score))
# FALSE  TRUE 
# 4     1 
library(dplyr)
df %>% filter(is.na(score)) # score가 NA인 데이터만 출력 # 결측치가 포함된 데이터의 함수는 연산X, NA가 출력
#   sex score
#    F    NA 

# 결측치가 있는 행 추출 
df %>% filter(is.na(score)) # score가 na인 데이터만 출력
# sex score
# 1   F    NA

df %>% filter(!is.na(score)) # 5번의 결측치를 포함한 데이터를 제외한 나머지 데이터 출력( &를 활용하여 3번의 결측값도 제거가능)
# 아래와 같이 score에 대한 결측치를 제외한 나머지 데이터를 산출하게 되면 mean/sum 값들을 도출 가능
#    sex score 
# 1   M     5
# 2   F     4
# 3  NA     3
# 4   M     4

# 모든 변수에 결측치 없는 데이터 추출 filter()에 일일이 변수를 지정하지 않아도 결측치가 있는 행을 제거하도록 코드구성됨
# 성별의 결측값에 "NA" ""를 씌워주게 되면 결측치가 아닌 영문자 "NA"로 인식하기 때문에 na.omit()함수를 적용해도 결측치가 
#완전히 제거가 안됨. 
#   sex score
# 1   M     5
# 2   F     4
# 3  NA     3
# 4   M     4
df_nomiss2 <- na.omit(df)
df_nomiss2
# sex score
# 1   M     5
# 2   F     4
# 4   M     4

?na.omit (Object = dataframe)
# na.fail(object, ...)
# na.omit(object, ...)
# na.exclude(object, ...)
# na.pass(object, ...)

# 함수의 결측치 제외 기능 이용하기
mean(df$score, na.rm = T) # 결측치를 제외하고 평균 산출


library(dplyr)
exam <- read.csv("csv_exam.csv")
exam

#요약 통계량을 산출할 떄도 na.rm을 적용가능 
exam[c(3,8,15), "math"] <- NA # 3,8,15행의 math에 NA 할당
exam

# exam math가 결측치를 포합하기 떄문에 summarise()로 평균을 산출하면 NA가 출력이 됨. 
exam %>% summarise(mean_math = mean(math)) # math의 평균 산출
# mean_math
# 1        NA
# 따라서 mean()함수에서 na.rm을 적용하면 결측치를 제외하고 평균을 구할 수 있음.

# 평균값으로 결측치 대체하기 결측치 대체법(Imputation)
# 결측치를 제거하면 너무 많은 데이터들이 손실돼 분석 결과를 왜곡하는 문제가 발생 이를 해결하기 위해 제거하는 대신해 다른 값을 
# 채워 넣으므로서 데이터 손실을 막을 수 있다. 
mean(exam$math, na.rm = T) #결측치를 제외하고 math 평균 산출 #  55.23529
exam$math <- ifelse(is.na(exam$math), 55, exam$math) #math가 NA면 55로 대체 아니면 exam$math
table(is.na(exam$math)) 
# FALSE 
# 20 
exam
#     id  class math english science
# 1   1     1   50      98      50
# 2   2     1   60      97      60
# 3   3     1   55      86      78
# 4   4     1   30      98      58
# 5   5     2   25      80      65
# 6   6     2   50      89      98
# 7   7     2   80      90      45
# 8   8     2   55      78      25
# 9   9     3   20      98      15   
# 10 10     3   50      98      45
# 11 11     3   65      65      65
# 12 12     3   45      85      32
# 13 13     4   46      98      65
# 14 14     4   48      87      12
# 15 15     4   55      56      78
# 16 16     4   58      98      65
# 17 17     5   65      68      98
# 18 18     5   80      78      90
# 19 19     5   89      68      87
# 20 20     5   78      83      58 
# 위의 표를 확인해보면 3,8,15행에 할당하였던 결측값이 55로 대체된 것을 확인할 수 있다.




