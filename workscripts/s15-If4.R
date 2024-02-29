#ifelse (조건, 참, 거짓)
      # logical에 따라 참/거짓 나뉨
scores <- seq(50, 100, 10)
scores 

exam <- ifelse(scores >= 80, '합격', '불합격')
exam # "불합격" "불합격" "불합격" "합격"   "합격"   "합격" 

score <- scores[3]
score #70

pass <- ifelse(score >=70, '합격', '불합격')
pass # "합격"

fails <- ifelse(scores < 60, '불합격', '합격')
fails # "불합격" "합격"   "합격"   "합격"   "합격"   "합격"  

