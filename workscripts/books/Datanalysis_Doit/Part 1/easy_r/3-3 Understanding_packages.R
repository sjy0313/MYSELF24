# 패키지 설치
install.packages("ggplot2")
# 패키지 로드
library(ggplot2)
x <- c("a", "a", "b", "c")
x

qplot(x)
# collapse 같은 parameter들을 활용하여 함수에 적용하기
# 그래프생성
qplot(data = mpg, x = drv, y=hwy, geom= "boxplot", colour = drv)
# + geom = line/ boxplot(상자그림 형태ㅡ , colour= drv별 색 표현 )

# 함수의 기능이 궁금할 떄 
?qplot

mpg <- as.data.frame(ggplot2::mpg) # 패키지의 mpg데이터 불러와 데이터 프레임 만들기
mpg

?mpg # mpg 설명글 출력

