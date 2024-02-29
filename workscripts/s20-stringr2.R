#문자열 처리 라이브러리

#패키지 설치
install.packages("stringr")

#패키지 제거 
remove packages("stringr")

#사용 : 메모리로 로딩
library(stringr)

# 문자열 교체
# help(str_replace)
# str_replace(string, pattern, replacement) / str_replace_all(string, pattern, replacement)
str_replace(문자열, 교체대상문자열, 새로운문자열)
sid <- "020313-1234567"
sid #   "020313-1234567"
# 처음 만나는 문자열('-')를 새로운 문자열('.')로 교체
xid <- str_replace(sid, '-','.')
xid #   "020313.1234567"

# 전화번호
tel <- "010-1234-4567"
# 처음 만나는 문자열만 변경 됨
str_replace(tel,'-','.') # "010.1234-4567"
str_replace_all(tel,'-','.') "010.1234.4567"

# 문자열 결합(joining multiple strings into onestring) 
# str_c(...)
# str_c(..., sep = "", collapse=NULL) # ...= charcter vec, sep= string to insert between input vector 
help(str_c)
t1 <- '010'
t2 <- '1234'
t3 <- '5678'
tel <- str_c(t1, '-', t2, '-', t3)
tel "010-1234-5678"

# 문자열 분활(seperating multiple strings into string/s)
telx <- str_split(tel, '-')
telx # "010"  "1234" "5678"
class(telx) # "list"
telx[[1]]  # 전체 참조 "010"  "1234" "5678"
telx[[1]][1] # 개별 참조 "010"
telx[[1]][2] # "1234"

# 분활 함수 str_split()의 결과 list형을 백터 변환
telv <- unlist(telx)
telv  # "010"  "1234" "5678"
class(telv) # "character"
telv[1] # "010"
telv[2] # "1234"
telv[3] # "5678"

# 백터를 문자열로 결합
telp <- paste(telv, collapse ='.') # collapse: 결합원하는 문자열 지정가능
telp "010.1234.5678"

# [문제]
# 문자열: "010-1234-5678", "123456-7654321"
#위 문자열 예시처럼 데이터가 문자('-')로 n개로 연결되어 있다.
# str_c() 함수를 사용하여 새로운 연결문자('.')로 결합해라
# str_c(문자열, 연결문자)와 같이 해결하라.
# paste() 함수사용x

library(stringr)

e[1] <- "010-1234-5678"
e[2] <- "123456-7654321"
e1 <- "010"
e2 <- "1234"
e3 <- "5678"

str_c(..., sep = "", collapse=NULL)
str_replace(sid, '-','.')
paste(e1, e2, e3, collapse = ".")
e1 <- "010"
e2 <- "1234"
e3 <- "5678"
str_c(e1, ".", e2, ".",e3, collapse = ".")
# "010.1234.5678"

# or 
str_replace_all(e1,'-', '.')  # "010.1234.5678"

e4 <- "123456"
e5 <- "7654321"
str_c(e4,".",e5) "123456.7654321"

# 정답 
data <- "010-1234-5678"
vdata <- unlist(str_split(data,'-'))
vdata #  "010"  "1234" "5678"

ldata <- length(vdata)
ldata # 3
vdata[1] # "010"
vdata[2] # "1234"
vdata[3] # "5678"

seq(2,ldata) 

xdata <- vdata[1] # 초기값인 010 먼저 설정
for(n in seq(2,ldata)) {  # = n in 2:ldata
   cat(xdata, '\n')
   xdata <- str_c(xdata, '.') # string combine
   xdata <- str_c(xdata, vdata[n])
}
xdata #  "010.1234.5678"


# 개별 문자로 쪼개버리기 
help(strsplit)
data <- "010-1234-5678"
vdata <- unlist(strsplit(data, '')) # <- 문자열-> 문자백터
vdata # "0" "1" "0" "-" "1" "2" "3" "4" "-" "5" "6" "7" "8"

ldata <- length(vdata)
ldata # 13 

for(n in seq(1, ldata)) {
  if(vdata[n] == '-') {
    vdata[n] = '.'
  }
}

vdata #  "0" "1" "0" "." "1" "2" "3" "4" "." "5" "6" "7" "8"
vdata <- paste(vdata, collapse = '') # 백터를 문자열로 변환
vdata # "010.1234.5678"
class(vdata) character 