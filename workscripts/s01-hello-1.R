#주석
# 현재 라인 실행 : ctrl + Enter

#설치된 패키지
available.packages()
dim(available.packages())

#R session 보기
sessionInfo()

#패키지 설치
install.packages("translations")

#패키지 로딩 : 사용
library("translations")

#현재 로드된 패키지 확인
search()

#패키지 제거 
remove.packages("translations")

