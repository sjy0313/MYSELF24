#if문
# 결과 <- ifelse(조건문, 참, 거짓)
help(ifelse)
ifelse(test, yes, no)
Arguments
test	
an object which can be coerced to logical mode.

yes	
return values for true elements of test.

no	
return values for false elements of test.


score <- 100
grade <- 'D'

if(score >=90) {
  grade= 'A'
} else if(score >=80) {
  grade= 'B'
} else if(score >=70) {
  grade= 'C'
} else {
  grade = 'D'
}

score <- 82
guide <- ifelse(score >= 80, '우수합격', '불합격')

cat('당신의 점수는:', score) # 100
cat('당신의 등급은?',grade) # A
cat('당신은 시험에', guide, "하였습니다.",sep='') 
