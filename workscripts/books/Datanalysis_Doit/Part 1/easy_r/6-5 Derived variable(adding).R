# 파생변수 추가(변수명은 원하는데로 추출가능)
exam %>% mutate(total = math + english + science) %>% head # 총합 변수 추가/ 일부 추출
# id class math english science total
# 1  1     1   50      98      50   198
# 2  2     1   60      97      60   217
# 3  3     1   45      86      78   209
# 4  4     1   30      98      58   186
# 5  5     2   25      80      65   170
# 6  6     2   50      89      98   237
# 여러 파생변수 한 번에 추가 가능
exam %>% mutate(total = math + english + science,
                mean = math + english + science)/3) %>% head # 총평균 변수 추가 
# mutate() 함수에 ifelse() 적용하기
exam %>% mutate(test = ifelse(science>=60, "pass", "fail")) %>% 
  
  
# 집단별 요약 
-summarise() mutate() # 함수를 사용할 떄와 마찬가지로 변수명은 자유롭게 정열가능
-mean() 평균
-sum() 합계
-median() 중앙값
-min()최솟값
-max() 최대값
-n() 빈도
#데이터프레임의 전체 요약 summary(exam)

exam %>% summarise(mean_math=mean(math)) # math 평균산출
# exam별로 분리 + math 평균산출(exam별 수학점수평균)
exam %>%
  group_by(class) %>% 
  summarise(mean_math=mean(math))
#  class mean_math
#    <int>     <dbl>
# 1     1      46.2
# 2     2      61.2
# 3     3      45  
# 4     4      56.8
# 5     5      78  

# 여러요약 통계량 
exam %>%
  group_by(class) %>% # class별 분리
  summarise(mean_math=mean(math), #math 평균
            sum_math = sum(math), #math 합계
            median_math = median(math), #math 중앙값
            n = n()) #학생 수

# dplyr 함수들을 하나의 구문으로 조합 example
회사별로 "suv" 자동차의 도시 및 고속도로 통합 평균 연비 평균을 구해 내림차순으로 정렬하고 1~5위 출력
# 참고(# mutate()함수를 통해 새로운 파생 column 을 만드는 함수(mutate(dataframe, 새로운 column명 = 기존 columns을 조합한 수식)
#  filter() 활용하여 특정 데이터 추출 / summarise()활용하여 
mpg %>%
  group_by(manufacturer) %>%
  filter(class == "suv") %>% 
  mutate(tot = (cty+hwy)/2) %>% 
  summarise(mean_tot = mean) %>% 
  arrange(desc(mean_tot)) %>% 
  head(5)


mpg %>%
  group_by(manufacturer) %>% 
  summarise(mean_cty = mean(cty)) %>% 
  head(10)

# manufacturer mean_cty
# <chr>           <dbl>
#   1 audi           17.6
# 2 chevrolet        15  
# 3 dodge            13.1
# 4 ford             14  
# 5 honda            24.4
# 6 hyundai          18.6
# 7 jeep             13.5
# 8 land rover       11.5
# 9 lincoln          11.3
# 10 mercury         13.2






 

  