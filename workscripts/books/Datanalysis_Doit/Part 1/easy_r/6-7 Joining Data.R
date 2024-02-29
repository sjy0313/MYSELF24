# 6-7 데이터 합차기 (POWER BI 관계설정과 유사함)
# join을 이용하여 데이터 병합하기
# bind_rows() 세로로 합치기 

library(dplyr)
# teacher kim(join 이 되는 기준columnem들)은 foreign키(외래키)와 값음 

exam <- read.csv("csv_exam.csv")
exam

# 담임교사 
teachers <- data.frame(class= c(1,2,3,4,5),
                       teacher=c("kim", "lee", "park", "choi", "jung"))
teachers 

# exam 에 담임교사 추가 left_join을 응용하면 특정 변수의 값을 기준으로 다른 데이터의 값을 추가가능
# class 변수를 기준으로 삼고 teachers 변수 추가 
exam_teacher <- left_join(exam, teachers, by='class')
exam_teacher

#담임 기준으로 조인 담임 데이터만 선택
# class(5)는 누락
exam_teacher <- right_join(exam, teachers, by='class')
exam_teacher


# 세로로 합치기 bind_rows
group_a <- data.frame(id= c(1,2,3,4,5),
                      test=c(60,70,80,90,85))
group_b <- data.frame(id= c(6,7,8,9,10),
                      test=c(70,83,65,95,80))
group_all <- bind_rows(group_a, group_b)
group_all
#    id test
# 1   1   60
# 2   2   70
# 3   3   80
# 4   4   90
# 5   5   85
# 6   6   70
# 7   7   83
# 8   8   65
# 9   9   95
# 10 10   80
