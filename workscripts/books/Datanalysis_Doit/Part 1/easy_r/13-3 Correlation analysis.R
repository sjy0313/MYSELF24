# 상관 분석 - 두 변수의 관계성 분석
# 상관 분석(corelation analysis)
# - 상관 계수(correlation coefficient)
# - 0 ~ 1 사이의 값 
# - 1에 가까울 수록 관련성이 크다 
# - 양수 : 정비례 / 음수: 반비례
# 함수: cor.test() 이용하면 상관분석 가능

#=============================================#

# 실업자 수와 개인 소비 지출의 상관관계
# unemploy : 실업자 수
# pce : 개인 소비 지출

economics <- as.data.frame(ggplot2::economics)
# 상관계수
cor.test(economics$unemploy, economics$pce)

# 결과

# Pearson's product-moment correlation

data:  economics$unemploy and economics$pce
t = 18.63, df = 572, p-value < 2.2e-16
alternative hypothesis: true correlation is not equal to 0
95 percent confidence interval:
 0.5608868 0.6630124
sample estimates:
      cor 
0.6145176 

p-value < 2.2e-16 # 0.05미만이므로 실업자 숭와 개인 소비 지출의 상관이 통계적으로 유의적임
cor : 0.6145176 # 실업자 수와 개인 소비 지출은 한 변수가 증가하면 다른 변수가 증가하는 정비례 관계

#====================================================================================================#

# 상관행렬(correlation matrix) 히트맵 만들기
# mtcats 데이터셋
- mpg: 연비
- cyl: 실린더 수
# wt: 무게

cor()을 이용하면 상관행렬을 만들 수 있음
head(mtcars)
# mtcars는 자동차 32종의 11개 속성에 대한 정보를 담고 있는 데이터
#                    mpg cyl disp  hp drat    wt  qsec vs am gear carb
# Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
# Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
# Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
# Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
# Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
# Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1

car_cor <- cor(mtcars)
round(car_cor, 2) # 소수점 셋째 자리에서 반올림 해서 출력

install.packages("corrplot")
library(corrplot)

corrplot(car_cor)
# corrplot의 parameter을 이용해 다양한 그래프의 형태를 바꿀 수 있다 method 에 number지정하여 원대신에 상관계수 입력가능
corrplot(car_cor, method = "number")

col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD","#4477AA"))

corrplot(car_cor,
         method = "color", # 색깔 표현
         col = col(200), # 색상 200개 선정
         type = "lower",# 왼쪽 아래 행렬만 표시
         order = "hclust", # 유사한 상관계수끼리 군집화
         addCoef.col = "black", # 상관계수 색
         tl.col = "black", # 변수명 색 
         tl.srt = 45, # 변수명 45도 기울임 
         diag = F) # 대각행렬 제외










