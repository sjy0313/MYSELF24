gender <- c("man", "woman", "man", "man") 
#요인형: factor ordinal
#백터를 요인형을 변환
# factor(x, levels, ordered)

ordinal_gender <- factor(gender, levels=c("woman", "man"), ordered=TRUE)
ordinal_gender #Levels: man < woman 

#빈도수: 수치형
table(ordinal_gender) # man 3, woman 1

#빈도수: 그래프
plot(ordinal_gender)

#mode(): 자료형
mode(ordinal_gender) # gender  

#class() 자료형
class(ordinal_gender) # "ordered" "factor" 2개의 class를 확인가능 서열변수와 명목변수 속서을 다가지고 있음을 의미

# 차트 그리기 
nominal_gender <- as.factor(gender)
par(mfrow=c(1,2))
plot(nominal_gender)
plot(ordinal_gender)
