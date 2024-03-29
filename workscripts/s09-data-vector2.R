# 백터(vector)  데이터 집합 

#참조: 첨자(index)는 1부터 시작

v <- c(1,3,5,7,9)
v # 1 3 5 7 9

v[0] 
# 0으로 참조를 하면 #numeric(0) 값이없음을 의미
vx <- v[0] + 10 #numeric(empty)
vt <- v[1] + v[2] + v[3] + v[4] + v[5] #25

v[1] # 1
v[2] # 3
v[3] # 5
v[4] # 7
v[5] # 9

vt2 <- sum(v)

#길이 : 백터의 길이 
vl <- length(v)
vl # 5 벡터의 길이는 데이터의 크기를 나타내며, 벡터 간의 거리나 유사성을 계산하는 데에 활용됩니다.

#평균
va <- sum(v) / length(v)
va # 5

#맨마지막 요소의 값
ve <- v[vl]

#슬라이스
v[1:vl] # 1 3 5 7 9
v[2:4] # 3 5 7 ( shift 아래화살표 해당 택스트 전체선택)

#상대참조( 지정한 위치에서의 해당하는 값 도출 가능)
rc <- c(2:4)
rc # 2 3 4
v[rc] # 3 5 7
v[c(1,3,5)] # 1 5 9

v10 <- c('a', 'b', 'c', 'd', 'e')
v10[c(1,3,5)] # "a" "c" "e"

v10[seq(1,length(v10),2)]#홀수번째
v10
v10[seq(2,length(v10),2)]  #짝수번쨰

#음수: 제외 
v10[-3] # 3번쨰 위치 제외
v10[c(-1,-3,-5)] # 1,3,5번쨰 위치 제외

#원본을 변경시키려면 다시 원본 변수에 할당 
#마지막 요소를 삭제
v10 <- v10[-length(v10)]
#마지막 요소 끝에서 부터 1개씩 삭제 원할 시, abcd -> abc -> ab
v10 <- v10[length(v10) * -1]

    


    

 