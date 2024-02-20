#데이터셋 보기
data()
#히스토그램 : 빈도수 알려주는 그래프
#flow of the river nile
hist(Nile)
#히스토그램 : 밀도
hist(Nile, freq=F)
#분포곡선(line)
lines(density(Nile))

