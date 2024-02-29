# 데이터 합치기 dplyr에서 제공되는 mutate함수는 dataframe에 변수를 추가할 떄 씀.
library(dplyr)
# 문재인 대통령 연설문 불러오기
raw_moon <- readLines("speech_moon.txt", encoding = "UTF-8")
moon <- raw_moon %>%
  as_tibble() %>%
  mutate(president = "moon")
# 박근혜 대통령 연설문 불러오기
raw_park <- readLines("speech_park.txt", encoding = "UTF-8")
park <- raw_park %>%
  as_tibble() %>%
  mutate(president = "park")
# 데이터 합치기 
bind_speeches <- bind_rows(moon, park) %>%
  select(president, value)
bind_speeches
tail(bind_speeches)
head(bind_speeches)
# 위 코드에서는 행 기준으로 bind_rows함수를 이용하여 데이터를 통합했지만 (library(base)에서는 rbind()이용) 열 기준으로
# (base패키지 일때는 cbind()), bind_cols()를 통해 해결한다. 

# 기본적인 전처리와 토큰화
#  bind_speeches는 tibble 구조 이므로 mutate(활용)
library(stringr)
speeches <- bind_speeches %>%
  mutate(value = str_replace_all(value, "[^가-힣]", " "), #한글제외한 나머지 문자/특수문자를 공백처리
         value = str_squish(value)) # string(처리할 택스트), str_squish()은 연속된 공백을 제거할떄 사용 
speeches
# 토큰화 작업을 하여 value에 대해 word를 output으로 설정 해놔야 count()함수를 사용할 떄 문제없음.


# 형태소 분석기를 이용해 명사 기준 토큰화
library(tidytext)
library(KoNLP)
speeches <- speeches %>%
  unnest_tokens(input = value, # 분석대상
                output = word, # 출력 변수명
                token = extractNoun) # 토큰화 함수 
speeches

#연설문의 단어별 빈도
#METHOD 1
test1 <- table(speeches$word & speeches$president)
test1
#speeches$word & speeches$president에서 다음과 같은 에러가 발생했습니다:
#오로지 숫자, 논리, 또는 복소수 유형에 대한 연산들만 가능합니다 #table함수는 문자열에 대한 빈도측정 불가능
#METHOD 2
frequnecy1 <- speeches %>% 
  group_by(president, word) %>% 
  summarise(n = n()) %>% 
  filter(str_count(word) > 1) 
head(frequnecy1)
# A tibble: 6 × 3
# Groups:   president [1]
#  president word         n
#   <chr>     <chr>    <int>
# 1 moon      가동         1
# 2 moon      가사         1
# 3 moon      가슴         2
# 4 moon      가족         1
# 5 moon      가족구조     1
# 6 moon      가지         4
#  group_by함수를 이용해서 그룹별로 president, #word를 나누어 각각에 summarise함수를 적용해 동시에 #계산할 수 있음. 이때 n은 빈도수를 의미하며 각 변수마다 #정수형인 n열의 데이터갯수 만큼 빈도가 있음을 보여줌.
#METHOD 3
frequency <- speeches %>%
  count(president, word) %>%   # 연설문 및 단어별 빈도
  filter(str_count(word) > 1)  # 두 글자 이상 추출
head(frequency)
# count()함수는 입력한 변수의 알파벳/가나다순으로 행을 #정렬, count()에 집단을 구성하는 두 변수를 순서대로 입력
# A tibble: 6 × 3
#   president  word         n
#   <chr>     <chr>    <int>
# 1 moon      가동         1
# 2 moon      가사         1
# 3 moon      가슴         2
# 4 moon      가족         1
# 5 moon      가족구조     1
# 6 moon      가지         4

# 자주 사용된 단어 추출
# slice_max()는 값이 큰 상위 n개의 행을 추출해 내림차순으로 정렬하는 함수
# METHOD 1
df <- tibble(x= c(1:100))
df %>% slice_max(x, n=3) # 상위 행 3개 추출 
# METHOD 2
df %>% 
  arrange(desc(x)) %>% 
  head(3)
# METHOD 3
df %>% 
  top_n(x, n=3) %>% 
  arrange(desc(x))

# 가장 많이 추출된 단어 
top10 <- frequency %>%
  group_by(president) %>%  # president별로 분리
  slice_max(n, n = 10)     # 상위 10개 추출
top10
# A tibble: 22 × 3
# 10개를 추출했는데 20행이 아니라 22행이 추출된 이유는 빈도수가 동점이 아이들도 같이 추출되었기 때문
top10 %>% 
  filter(president == "park") # 동점인 행 확인 가능

# slice_max(with_ties = F): 원본 데이터의 정렬 순서에 따라 행 추출( 동점인 행 제거)
top10 <- frequency %>%
  group_by(president) %>%
  slice_max(n, n = 10, with_ties = F)
top10

# 막대 그래프 만들기  (변수의 항목별로 그래프 - facet_wrap(),  ~ 뒤에 그래프를 나누는 기준 변수 입력)
library(ggplot2)
ggplot(top10, aes(x = reorder(word, n),
                  y = n,
                  fill = president)) +
  geom_col() +
  coord_flip() +
  facet_wrap(~ president)

# 그래프 별 y축 설정하기
ggplot(top10, aes(x = reorder(word, n),
                  y = n,
                  fill = president)) +
  geom_col() +
  coord_flip() +
  facet_wrap(~ president,         # president별 그래프 생성
             scales = "free_y")  # y축 통일하지 않음

# PARK에서 value= 국민 제거하고 빈도수 비교
top10 <- frequency %>%
  filter(word != "국민") %>%
  group_by(president) %>%
  slice_max(n, n = 10, with_ties = F)
top10
ggplot(top10, aes(x = reorder(word, n),
                  y = n,
                  fill = president)) +
  geom_col() +
  coord_flip() +
  facet_wrap(~ president, scales = "free_y")
# 축 정렬
ggplot(top10, aes(x = reorder_within(word, n, president),
                  y = n,
                  fill = president)) +
  geom_col() +
  coord_flip() +
  facet_wrap(~ president, scales = "free_y")

# x= 축 by = 정렬기준 within = 그래프를 나누는 기준

# 변수 항목 제거
#tidytext::scale_x_reordered(): 각 단어 뒤의 범주 항목 제거
ggplot(top10, aes(x = reorder_within(word, n, president),
                  y = n,
                  fill = president)) +
  geom_col() +
  coord_flip() +
  facet_wrap(~ president, scales = "free_y") +
  scale_x_reordered() +
  labs(x = NULL) +                                    # x축 삭제
  theme(text = element_text(family = "nanumgothic"))  # 폰트









