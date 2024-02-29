st1 <- c("hello", "World")
st1
x <- c(1,2,3)
mean(x) # 2
max(x) # 3 
min(x) # 
# Paste 함수( ,를 구분자로 단어를 하나로 합치기, collapse는 단어를 구분할 문자를 지정하는 기능)
# collapse처럼 함수의 옵션을 설정하는 명령어를 parameter or 매개변수
paste(st1, collapse = ",") # "hello,World"
paste(st1, collapse = " ") # "hello World" 띄어쓰기 

