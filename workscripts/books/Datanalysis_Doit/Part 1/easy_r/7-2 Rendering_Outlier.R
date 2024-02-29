# 이상치(Outlier) 정제하기
# sex(1,2) score(1~5) 범위 
outlier <- data.frame(sex = c(1,2,1,3,2,1),
                      score = c(5,4,3,4,2,6))
outlier
#   sex score 
# 1   1     5
# 2   2     4
# 3   1     3
# 4   3     4
# 5   2     2
# 6   1     6
# outlier of "sex"column 3 /  outlier of "score"column 6

# 결측 처리하기(이상치->결측치로 변환)
# sex가 3/ score>5 이면 NA할당 
outlier$sex <- ifelse(outlier$sex == 3, NA, outlier$sex)
outlier
outlier$score <- ifelse(outlier$score == 3, NA, outlier$score)
outlier

#   sex score
# 1   1     5
# 2   2     4
# 3   1    NA
# 4  NA     4
# 5   2     2
# 6   1     6

#결측치를 제외하고 평균구하기
outlier %>% 
  filter(!is.na(sex) & !is.na(score)) %>% #결측치 제외하기
  group_by(sex) %>%  # 집단별로 요약하기
  summarise(mean_score = mean(score)) # 평균값 구하기
# A tibble: 2 × 2
#    sex mean_score(성별별 점수 평균)
#   <dbl>   <dbl>
# 1   1      5.5
# 2   2        3  

# 이상치 제거하기- 극단적인 값 p176 참고 
boxplot(mpg$hwy)
boxplot(mpg$hwy)$stats
#       [,1]
# [1,]   12
# [2,]   18
# [3,]   24
# [4,]   27
# [5,]   37
# 결측처리(정상범위를 벗어난 놈들은 결측값으로 처리)
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy >37, NA, mpg$hwy)
table(is.na(mpg$hwy))
# FALSE  TRUE 
# 231     3

                  


