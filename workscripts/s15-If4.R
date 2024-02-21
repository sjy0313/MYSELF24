#

score <- seq(50, 100, 10)

exam <- ifelse(score >= 80, '합격', '불합격')
exam # "불합격" "불합격" "불합격" "합격"   "합격"   "합격" 