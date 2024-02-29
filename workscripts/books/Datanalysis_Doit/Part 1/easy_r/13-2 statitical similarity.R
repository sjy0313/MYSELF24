# 13-2
# T검정 - 두 집단의 평균 비교
# t-test  통계적으로 유의한 차이가 있는지 알아볼 떄 사용하는 통계기법
# (변수-평균) /  표본의 표준편차
# class : 자동차 종류
# city : 도시연비
# 유의 확률(p-value): 0.05(5%) 판단기준 (p-value)가 0.05미만이면 집단 간 차이가 통계적으로 유의하다 
#아래 compact와 suv간 평균도시 연비차이가 통계적으로 유의함을  p-value < 2.2e-16 를 보고 판단 할 수 있다.


#------------------------------------------------------------------------#
# 평균 연비
# compact : 20.12766
# suv : 13.50000

mpg <- as.data.frame(ggplot2::mpg)
# compact 자동차와 suv자동차의 도시연비 t검정
library(dplyr)
mpg_diff <- mpg %>% 
  select(class,cty) %>% 
  filter(class %in% c("compact", "suv"))

head(mpg_diff)
mpg_diff
table(mpg_diff$class) # class 변수가 compact인 자동차와 suv인 자동차를 추룰
# compact     suv 
#     47      62 

# T 검정 함수 : t.test 앞에서 추출한 mpg_diff데이터를 지정하고 ~를 이용해 비교할 값인 cty변수와 비교할 집단인 class변수를 지정 
# t검정은 비교하는 집단의 분산이 같은지 여부에 따라 적용공식이 다름 여기서는 분산이 같다고 가정하고 var.equal에 T지정

t.test(data = mpg_diff, cty ~ class, var.equal = T)

Two Sample t-test

data:  cty by class
t = 11.917, df = 107, p-value < 2.2e-16
alternative hypothesis: true difference in means between group compact and group suv is not equal to 0
95 percent confidence interval:
  5.525180 7.730139
sample estimates:
  mean in group compact     mean in group suv 
20.12766              13.50000 

#-------------------------------------------------------------------------------------------------------#

#일반 휘발유와 고급 휘발유의 도시 연비 t 검정
#도시 연비 차이가 통계적으로 유의한가 

mpg <- as.data.frame(ggplot2::mpg)
mpg
mpg_diff2 <- mpg %>% 
  select(fl, cty) %>% 
  filter(fl %in% c("r", "p")) # r: regular , p: premium
mpg_diff2 
table(mpg_diff2$fl)
# p   r 
# 52 168 

t.test(data = mpg_diff2, cty ~ fl, var.equal = T)
Two Sample t-test

data:  cty by fl
t = 1.0662, df = 218, p-value = 0.2875
alternative hypothesis: true difference in means between group p and group r is not equal to 0
95 percent confidence interval:
  -0.5322946  1.7868733
sample estimates:
  mean in group p mean in group r 
17.36538        16.73810 

# p-value 0.2875 > 0.05 #sample estimates



















