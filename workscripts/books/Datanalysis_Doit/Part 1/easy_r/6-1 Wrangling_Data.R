# 데이터 전처리와 비슷한 의미
# - 데이테 가공(Data Manipulation)
# - 데이터 핸들링(Data Handling)
# - 데이터 랭글링(Data Wrangling)(감싸다) # 데이터를 수집한 후에, 해당 데이터를 분석 및 시각화에 활용하기 좋은 형태로 가공하고 정리하는 과정을 의미
# - 데이터 먼징(Data Munging)


dplyr 패키지는 %>% 기호를 이용해 함수들을 나열하는 방식으로 코드 작성
# %>% =pipe operator %>% = ctrl + shift + m

library(dplyr)
exam <- read.csv("csv_exam.csv")
exam

# filter 활용하여 특정 데이터 추출하기 class가 1인 행만 추출
exam %>% filter(class == 1)
# != 같지않다 1반이 아닌 경우
exam %>% filter(class != 1) 
#filter and활용 (여러조건 동시 추출) : &/ or활용 (여러 조건 중 하나라도 충족되는 데이터 추출) :  |
exam %>% filter(class != 1 (&/|) english >= 90) 
# |를 활용하여 여러조건의 데이터 나열 가능하지만 아래 
# %in% 기호를 이용하여 |를 이용할 떄 보다 간편하게 작성 가능 
exam %>% filter(class %in% c(1,3,5)) # 1,3,5반에 해당하면 추출

# 변수 추출하기
# select()로 해당 변수 추출 가능 ,를 넣어 여러 변수 동시 추출 -를 이용하여 변수 제외가능
exam %>% select(-math) # class = data.frame
exam$math class= "integer", vector 형으로 추출되기 떄문에 위 dataframe와 같은 표형식은 만들어지지 않음
#filter와 select의 조합
exam %>% filter(class == 1) %>% select(english) / exam %>% select(id, math) %>% head(앞부분 6행까지)

# data.frame(class=exam$class, Math=exam$math, English=exam$english) filter와 select함수를 활용하면 식이 훨씬 짧아짐

# dplyr 함수의 장점은 %>% 을 활용하여 여러 함수를 조합하여 코드의 길이를 줄일 수 있음

#오름차순 정렬(sort) 낮은 데이터에서 높은 데이터 순
exam %>% arrange(math) # math 오름차순 정렬 / arrange(desc(math)) 내림차순 정리

# 백터 정렬 : 오름차순
# 데이터를 정렬  sort() : 정렬된 데이터 바로 리턴(순서에 맞게 재배치 후 값 출력)
math_sort_asc <- sort(exam$math) # 수학 점수= 추출된 데이터 기준으로 오름차순 정렬
math_sort_asc # 20 25 30 45 45 46 48 50 50 50 58 60 65 65 75 78 80 80 89 90


# order(데이터, na.last, decreasing) order함수
math_order_asc <- order(exam$math) #  정렬된 쉘의 위치 값 리턴( order() 함수는 default로 NA값을 정렬 결과에서 제외합니다. # 그리고 오름차순을 기본 정렬 순서로 합니다.)
# ex. v2[order(v2, na.last = F)]   # NA를 처음으로 배치
# [1] NA  1  2  3  5 10

math_order_asc # 9  5  4  3 12 13 14  1  6 10 16  2 11 17 15 20  7 18 19  8 # 인덱스 추출(특정데이터 = 여기선 id 추출)
math_order_desc <- order(-exam$math)
math_order_desc

# 내림차순  (데이터베이스의 인덱스가 책의 목차와 색인과 같은 역할을 한다.)
#  8 19  7 18 20 15 11 17  2 16  1  6 10 14 13  3 12  4  5  9

m1 <- exam %>% arrange(desc(math))
m1
class(m1) # "data.frame"
m2 <-exam %>% select(math)
m2
class(m2) # "data.frame"
m3 <- exam$math
m3
class(m3) # integer
# 이로써 정수형 데이터셋에서만 order 함수이용가능
m3[order(m3, decreasing = T)]  # 수학점수 오름차순으로 나열
# 90 89 80 80 78 75 65 65 60 58 50 50 50 48 46 45 45 30 25 20


# 아래 데이터는 math데이터에서 높은 점수 순으로 상위 10위의 리스트를 추출한 것임 order함수는 순서를 추출하는 것임 
#    id class math english science
# 1   8     2   90      78      25
# 2  19     5   89      68      87
# 3   7     2   80      90      45
# 4  18     5   80      78      90
# 5  20     5   78      83      58
# 6  15     4   75      56      78
# 7  11     3   65      65      65
# 8  17     5   65      68      98
# 9   2     1   60      97      60
# 10 16     4   58      98      65
# order( ) 함수: 순서를 정렬해서 인덱스 반환

# exam[math_order_asc,] indexing 하게 되면 효율적으로 데이터 추출가능(data optimizing)
#    id class math english science
# 9   9     3   20      98      15
# 5   5     2   25      80      65
# 4   4     1   30      98      58
# 3   3     1   45      86      78
# 12 12     3   45      85      32
# 13 13     4   46      98      65
# 14 14     4   48      87      12
# 1   1     1   50      98      50
# 6   6     2   50      89      98
# 10 10     3   50      98      45
# 16 16     4   58      98      65
# 2   2     1   60      97      60
# 11 11     3   65      65      65
# 17 17     5   65      68      98
# 15 15     4   75      56      78
# 20 20     5   78      83      58
# 7   7     2   80      90      45
# 18 18     5   80      78      90
# 19 19     5   89      68      87
# 8   8     2   90      78      25

help(arrange) 


# 수학점수 상위 10명을 점수가 높은 순으로 추출
math_higher10 <- exam %>% arrange(desc(math)) %>% head(10)
math_higher10
# 성능
exam %>% 
  select(id, class, math) %>% 
  arrange(desc(math)) %>% 
  head(10) %>% 
  arrange(id)

#     id class math
# 1   2     1   60
# 2   7     2   80
# 3   8     2   90
# 4  11     3   65
# 5  15     4   75
# 6  16     4   58
# 7  17     5   65
# 8  18     5   80
# 9  19     5   89
# 10 20     5   78
help(order)
