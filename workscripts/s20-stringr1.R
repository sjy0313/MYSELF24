#문자열 처리

#패키지 설치
install.packages("stringr") <- 문자열 처리 위해 stringr

#패키지 제거 
remove packages("stringr")

#사용 : 메모리로 로딩
library(stringr)

# 문자열의 길이 
s1 <- "Hello, World." # 스칼라형이기 때문에 하나의 문자열로 봄("")
s1_len <- length(s1) 
s1_len # 1L

n <- 10
s <- "10" # ASCII 코드법으로 출력 => 숫자 1byte(8bit) 영문 2byte(16bit) 한글 3byte로 처리

#문자열에서 논리적인 문자로 구성된 길이 
s1 <- str_length(s1)
s1  # [1] 13 #가운데 공백도 문자열로 카운팅

# 한글, 숫자, 공백, 특수문자
shn <- "한글12345\n"
shl <- str_length(shn)
shl #8 : 한글(2) + 공백(1) + 숫자(5) + 특수문자(1)[\n]

# 문자열 내에서 특정 문자열의 위치

# str_locate 함수는 문자열에서 특정 패턴의 위치를 찾아주는 함수입니다. 이 함수를 사용할 때 특정 패턴이
#문자열에서 여러 번 등장하는 경우,반환값은 위치를 나타내는 행렬(matrix)로 처리됩니다.
#따라서 백터 형태로 처리되지 않습니다.


sp1 <- "일이삼사오육칠팔구십"
l10 <- str_locate(sp1, "육")
l10  #  6 6

l38 <- str_locate(sp1, "삼사오육칠팔")
l38 
#       start end
# [1,]     3    8 

l38[1,1] # 시작위치: 3
l38[1,2] # 종료위치: 8

#
l3 <- str_locate(sp1, "삼")
l3
#       start end
# [1,]     3   3
l8 <- str_locate(sp1,"팔")
l8
#       start end
# [1,]     8   8


l8 <- str_locate(sp1,"팔구")
l8
#      start end
# [1,]     8   9

#부문 문자열 만들기
# help(Str_sub)
# str_sub(string, start= 1L, end= -1L) 
# end 파라미터에 -1L을 사용하는 이유는 문자열의 끝(end)을 나타내기 위함입니다.
# 여기서 -1L은 문자열의 마지막 위치를 나타냅니다.
# -1L을 사용함으로써 문자열의 끝에서부터 하나를 제외한 위치까지 추출할 수 있습니다.

s38 <- str_sub(sp1, l3[1,1],l8[1,2])
s38 #  "삼사오육칠팔구"

# [문제]

#이메일: abc@ysit.ac.kr, admin@ysit.ac.kr
#위 이메일 주소에서 아이디와 주소를 분리 추출하라 
#조건: 다양한 이메일 주소를 처리 가능하도록 하라 
#아이디: abc
#주소 : ysit.ac.kr

#ID <- str_locate(EMAIL_ID, "abc")
EMAIL_ID <- "abc@ysit.ac.kr"
ID <- str_locate(EMAIL_ID, "abc")
ID
#       start end
# [1,]     1   3

EMAIL_ID <- "admin@ysit.ac.kr"
ID2 <- str_locate(EMAIL_ID, "admin")
ID2
#       start end
# [1,]     1   5
ID2 <- str_sub(EMAIL_ID, end= -12L ) 
ID2 # "admin"

# OR
ID2 <- str_sub(EMAIL_ID, ID2[1,1], ID2[1,2])
ID2 # "admin"

EMAIL_ID2 <- "abc@ysis.ac.kr"
ID2 <- str_locate(EMAIL_ID2, "ysis.ac.kr")
ID2      
#       start end
# [1,]     5  14'

ID3 <- str_locate(EMAIL_ID2, "abc")
ID3
#       start end
# [1,]     1   3

ID <- str_sub(EMAIL_ID2,ID3[1,1], ID3[1,2])
ID # "abc"
ADS <- str_sub(EMAIL_ID2, ID2[1,1], ID2[1,2])
ADS # "ysis.ac.kr"

# [모범정답]
#이메일: abc@ysit.ac.kr, admin@ysit.ac.kr
email <- "abc@ysit.ac.kr"
eloc <- str_locate(email, '@') #구분문자('@')의 위치 (시작과 종료위치가 같음 문자1개여서)
el <- str_length(email) # 이메일의 전체 길이 
es <- eloc[1,1] # 구분자의 시작위치(@앞)
ee <- eloc[1,2] # 구분자의 종료위치(@뒤)
eid <- str_sub(email, 1, es - 1) # 아이디 추출
eha <- str_sub(email, ee + 1, el) # 주소 추출
eid #  "abc"
eha # "ysit.ac.kr"

# 대소문자 변환
EMAIL <- str_to_upper(email) # 문자열을 대문자로 변환하여 리턴, 원본은 변경X
EMAIL #  "ABC@YSIT.AC.KR"

# 소문자 변환
small <- str_to_lower(EMAIL)
small # "abc@ysit.ac.kr"












