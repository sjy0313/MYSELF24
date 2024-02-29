english <- c(90, 80, 60, 70)
english

math <- c(50, 60, 70, 80)
math
# 데이터 프레임 만들기
df_midterm <- data.frame(english, math)
df_midterm
# #  english math
# 1      90   50
# 2      80   60
# 3      60   70
# 4      70   80

class <- c(1,1,2,2)
class
df_midterm <- data.frame(english,math,class)
df_midterm 

# 평균 산출( 영어/수학 각각)
mean(df_midterm$english) # 75
mean(df_midterm$math) # 65

# 데이터 프레임 한번에 만들기 

df_midterm <- data.frame(english = c(9classdf_midterm <- data.frame(english = c(90,80,60,70), 
                         math = (50,60,100,20),
                         class = c(1,1,2,2))
df_midterm

