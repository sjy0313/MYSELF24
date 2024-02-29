# 그래프 패키지(함수를 이용할려면 해당 함수가 담긴 해당 패키지를 다운받아야한다.)
#산점도(scatter plot) 나이/소득 처럼 연속된 값으로 된 두 변수의 관계표현할 떄 씀
#ggplot2 문법은 layer 구조로 되어 있다. 
# 1단계: 배경설정 2단계: 그래프 추가(점/막대/선) 3단계: 설정 추가(축 범위, 색, 표식)

library(ggplot2)
#1단계
ggplot(data = mpg, aes(x=displ, y=hwy))
#2단계
ggplot(data = mpg, aes(x=displ, y=hwy)) + geom_point()
#3단계
ggplot(data = mpg, aes(x=displ, y=hwy)) + geom_point()+xlim(3, 6) # 축 범위 3~6지정

#막대그래프(BAR CHART) p190
library(dplyr)
# 집단별 평균표
df_mpg <- mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy))

# drv   mean_hwy
# <chr>    <dbl>
#   1 4         19.2
# 2 f         28.2
# 3 r         21  
df_mpg
# 막대그래프 생성
ggplot(data = df_mpg, aes(x = drv, y = mean_hwy)) + geom_col()
# 크기순으로 작성  reorder()를 사용해 막대를 크기순으로 정렬 가능 정렬 기준변수 앞에 -을 붙여 내림차순으로 정렬
ggplot(data = df_mpg, aes(x = reorder(drv, -mean_hwy), y = mean_hwy)) + geom_col()

# 빈도 막대 그래프 
ggplot(data = df_mpg, aes(x = drv))  + geom_var()

# 선 그래프
ggplot(data = df_mpg, aes(x = date, y = unemploy)) + geom_line()

# 상자 그림 
ggplot(data = df_mpg, aes(x = drv, y = mean_hwy)) + geom_boxplot()


