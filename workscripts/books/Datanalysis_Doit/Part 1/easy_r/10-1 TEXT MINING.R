10-1
install.packages("multilinguer")
library(multilinguer)

install.packages(c("stringr", "hash", "tau", "Sejong", "RSQLite", "devtools"), type = "binary")

install.packages("remotes")
remotes :: install_github(" haven-jeon/KoNLP",
                          upgrade = "never",
                          INSTALL_opts = c("--no-multiarch"))

install.package("KoNLP") 




# 안될시, 
library(KoNLP)
devtools::install_github("haven-jeon/KoNLP", upgrade = "never", INSTALL_opts = c("--no-multiarch"))
library(KoNLP)


# hiphop.txt 에는 멜론 차트 랩 힙합 상위 50곡의 가사가 포함됨.
txt <- readLines("hiphop.txt")
head(txt)

install.packages("stringr")
library(stringr)
# 문장에 있는 특수문자 제거( \\W는 특수문자를 나타내는 정규 표현식(regular expression) 정규 표현식을 이용하면 문장의 내용 중 #이메일 주소, 전화번호 처럼 특정한 규칙으로 되어 있는 부분을 추출가능
txt <- str_replace_all(txt, "\\W", " ")
txt

#명사 추출하기 
extractNoun("대한민국의 영토는 한반도와 그 부속도서로 한다")
# "대한"     "민국"     "영토"     "한반도와" "부속도서" "한"  



# 워드 클라우드(단어의 빈도를 구름 모양으로 표현한 그래프)
install.packages("wordcloud")
library(wordcloud)
library(RColorBrewer)

# 단어 색상 목록 만들기
pal <- brewer.pal(8, "Dark2")
# 난수(무작위로 생성한 수) 고정하기[함수를 실행할 때 마다 매번 다른 모양의 워드 클라우드를 만들어내므로]
set.seed(1234)

df_word