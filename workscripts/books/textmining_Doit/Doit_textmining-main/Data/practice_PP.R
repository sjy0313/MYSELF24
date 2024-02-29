library(stringr)
library(KoNLP)
useNIADic()
library(stringr)
library(dplyr)
library(tidytext)
library(ggplot2)
library(ggwordcloud)
library(showtext)
# Q1. speech_park.txt를 불러와 분석에 적합하게 전처리한 다음 띄어쓰기 기준으로 토큰화하세요.
# 
# Q2. 가장 자주 사용된 단어 20개를 추출하세요.
# 
# Q3. 가장 자주 사용된 단어 20개의 빈도를 나타낸 막대 그래프를 만드세요.
# •그래프의 폰트는 나눔고딕으로 설정하세요.

raw_park <- readLines("speech_park.txt", encoding = "UTF-8")
park <- raw_park %>% 
  str_replace_all("[^가-힣]", " ") %>% # 한글 제외 모두 제거
  str_squish() %>%  # 연속된 공백 제거 
  as_tibble() # 간단하게 처리 
park
# 토큰화
library(tidytext)
word_space <- park %>% 
  unnest_tokens(input = value,
                output = word,
                token = "words") # 띄어쓰기 기준 
word_space
# 가장 자주 사용된 단어 20개 추출
top20 <- word_space %>% 
  count(word, sort= T) %>% 
  filter(str_count(word)>1) %>% 
  head(20)
top20
# T이면 빈도가 높은 순으로 단어입력, str_count (단어개수)

# 빈도를 나타내는 그래프 + 폰트는 나눔고딕
library(showtext)
font_add_google(name= "Nanum Gothic", family = "nanumgothic")
showtext_auto()

library(ggplot2)
ggplot(top20, aes(x= reorder(word, n), y=n)) +
  geom_col() +
  coord_flip() +
  geom_text(aes(label = n), hjust = -0.3) +
  labs(x=NULL) +
  theme(text = element_text(family = "nanumgothic"))










