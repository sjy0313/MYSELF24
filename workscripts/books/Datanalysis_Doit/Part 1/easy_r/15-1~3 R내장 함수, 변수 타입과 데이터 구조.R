# R내장 함수, 변수 타입과 데이터 구조

exam <- read.csv("csv_exam.csv")
# 행 번호로 행 추출하기 
exam
exam[] #  조건없이 전체 데이터 출력
exam[1,] # 1행 추출
exam[2,] # 2행 추출

# 조건을 충족하는 행 추출하기
exam[exam$class == 1,] # class 1인 행
exam[exam$math >= 80,] # 80점 이상인 행

# dplyr과 달리 내장함수에서는 조건을 입력할 떄 변수명 앞에 데이터프레임 이름을 반복해 써야 한다
exam[exam$class == 1 & exam$math >= 50,]
# id class math english science
# 1  1     1   50      98      50
# 2  2     1   60      97      60

#열번호 별 변수 추출하기
exam[,1]
#변수명으로 변수 추출하기
exam[, "class"]  # c()통해 여러 변수 한번에 추출가능

# 행 변수 동시 추출
exam[1,3] # 50

# 파생변수 생성
exam$tot <- (exam$math + exam$english + exam$science)/3
exam
# id class math english science      tot
# 1   1     1   50      98      50 66.00000
# 2   2     1   60      97      60 72.33333
# 3   3     1   45      86      78 69.66667
# 4   4     1   30      98      58 62.00000
# 5   5     2   25      80      65 56.66667
# 6   6     2   50      89      98 79.00000
# 7   7     2   80      90      45 71.66667
# 8   8     2   90      78      25 64.33333
# 9   9     3   20      98      15 44.33333
# 10 10     3   50      98      45 64.33333
# 11 11     3   65      65      65 65.00000
# 12 12     3   45      85      32 54.00000
# 13 13     4   46      98      65 69.66667
# 14 14     4   48      87      12 49.00000
# 15 15     4   75      56      78 69.66667
# 16 16     4   58      98      65 73.66667
# 17 17     5   65      68      98 77.00000
# 18 18     5   80      78      90 82.66667
# 19 19     5   89      68      87 81.33333
# 20 20     5   78      83      58 73.00000
# 범주별 통계량
# tot~class
# ~class : 그룹화
# tot를 대상으로 class를 그룹화를 해라, tot대상으로 평균을 구해라 
aggregate(data=exam[exam$math >= 50 & exam$english >= 80,], tot~class, mean)
# class      tot
# 1     1 69.16667
# 2     2 75.33333
# 3     3 64.33333
# 4     4 73.66667
# 5     5 73.00000

#subset() 함수 subset(데이터명, select = c("변수1," "변수2", ... , "변수n") 
exam_subset <- subset(exam, exam$math >= 50, select = c("english", "science"))
exam_subset

