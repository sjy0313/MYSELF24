#요인형(Factor)
#같은 성격의 값의 목록을 범주로 갖는 백터의 자료 
#nominal(명목변수): 순서가 없음(계층관계x)/ 알파벳은 순서로 정렬
#ordinal(서열변수): 순서가 있음(계층관계o)/ 사용자가 지정한 순서 

#백터
gender <- c("man", "woman", "man") 

#요인형 : 백터를 요인형으로 변환(factor nominal)
#default : 알파벳 순서로 정렬되는 요인형
nominal_gender <- as.factor(gender) #명목변수로 변환
nominal_gender #Levels: man woman man -> 1 2 1
#빈도수: 수치형
table(nominal_gender) #man 2, woman 1 
#빈도수: 그래프
plot(nominal_gender)
#mode(): 자료형
mode(nominal_gender) #gender  
#class() 자료형
class(nominal_gender) #factor



