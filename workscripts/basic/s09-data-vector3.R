#백터(vector)
#문자 백터: letters 

# 알파벳 소문자 백터: 
letters # "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"

ap <- letters
ap[1]
ap[26]

ace <- ap[c(1,3,5)]
ace # "a" "c" "e"
ace[1] # "a"
ace[2] # "c"
ace[3] # "e"

#없는 요소의 인덱스에 값을 지정하여 추가가 된다. 
#백터에 원소를 추가 
#빈공간은 NA로 채워진다
ace[10] <- 'z' # "a" "c" "e" NA NA NA NA NA "z"

#NA로 채원진 빈 공간을 삭제
#음수(minus) 요소를 지정하여 요소를 제외하면 삭제 효과를 냄
ace[-c(4:9)] # "a" "c" "e" "z"

#값이 존재하는 기존 요소에 값을 지정하면 수정된다.
#요소를 수정
ace[1] <- 'A'
ace

