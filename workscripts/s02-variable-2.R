#그룹형 변수
#변수.맴버 형식의 변수 선언
학생정보 
student.code <- "24031-013"
student.name <- "신정윤"
student.age <- "23"
#학생정보 : 변수참조 
student.code 
student.name
student.age
# alt－　＝　＜－단축키
＃변수　선언？　참조？　
변수가　없는　상태에서는　＇참조＇
　ｘ＝　에러: 객체 'ｘ'를 찾을 수 없습니다
변수를　선언할　떄는　반드시　초깃값을　지정해야함
＃변수　<- 초깃값　변수의　자료형이　결정　기존　변수에　다른　자료형의　값을　넣으면　자료형이　변경된다
ｘ <-９９　＃숫자형
ｘ <- ＂신정윤＂　＃문자형
as.numeric(variable)
# 숫자 99를 붙여서 변수에 할당
variable <- paste("99", collapse = "")

# 결과 확인
print(variable)

# 문자열을 숫자로 변환
variable_numeric <- as.numeric(variable)

# 결과 확인
print(variable_numeric)
ｘ <- ９９
