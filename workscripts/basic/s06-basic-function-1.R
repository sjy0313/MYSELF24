#기본함수
#함수 도움말
#help(함수명)
#?함수명
help(sum)
?sum 
#args(함수명) sum의 arguments가 뭐냐 args(sum)
args(sum) function (..., na.rm = FALSE) ...=가변적임, na는 지우지않는다(rm)
sum(1,3,5,7,9)
#sum() 인자 값을 모두 더한 결과를 리턴
sum(2,4,6,NA) #NA 가 있으면 연산결과는 NA다.
sum(2,4,6,8,NA, na.rm=T) #20 (NA제외) na.rm = FALSE (기본값으로 가지고있음) false가 기본값이므로 na가 인자가 되려면 TRUE로 
정의 필요
sum(2,4,6,8,NA, na.rm=F) #NA

#함수 예제
#example(함수명)
example(sum)
sum(1:10) # 55 1~10합
sum(1:5, 6:10) #55

