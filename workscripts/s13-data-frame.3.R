#데이터프레임

#[실습]
#임의의 데이터프레임을 만들어 apply() 함수를 이용하여 처리
color <- c('green', 'blue', 'white')
landscape <- c('trees', 'sky','water')
occupied <- c(2/10, 5/10, 3/10)
emp <- data.frame(color=color, Landscape=landscape, Occupied=occupied)
emp
#   color Landscape Occupied
# 1 green     trees      0.2
# 2  blue       sky      0.5
# 3 white     water      0.3
# 
# str(emp)
# 'data.frame':	3 obs. of  3 variables:
#   $ color    : chr  "green" "blue" "white"
# $ Landscape: chr  "trees" "sky" "water"
# $ Occupied : num  0.2 0.5 0.3]


sum_of_occupied <- apply(emp[, 'Occupied', drop=FALSE],2,sum)
#drop argument is used to control whether the result should be simplified to the lo2west possible dimension.
#drop= TRUE가 default임 => 결과값이 열1개여도 dataframe형태로 남아있음.

sum_of_occupied # 1
#apply함수 쓰지않고 해당 열의 합 구하기
sum_of_occupied <- sum(emp$Occupied)
sum_of_occupied # 1
df <- data.frame(x=c(1:5), y=seq(2,10,2), z=letters[1:5])
df
summary(df)

#모든 행의 컬럼(1,2) 즉 x, y의 요소를 선택
df[,c(1,2)] 
#x,y의 행 단위
#합계
apply(df[,c(1,2)], MARGIN = 1, sum) # 3 6 9 12 15

#평균 
apply(df[,c(1,2)], MARGIN = 1, mean) # 1.5 3.0 4.5 6.0 7.5

#x,y의 열 단위
apply(df[,c(1,2)],MARGIN=2, sum) 
# x  y 
# 15 30 
apply(df[,c(1,2)],MARGIN=2, mean) 
# x y 
# 3 6



