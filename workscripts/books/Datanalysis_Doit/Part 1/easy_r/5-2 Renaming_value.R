install.packages("dplyr")
library(dplyr)
help(dplyr)

df_raw <- data.frame(var1=c(1,2,1), var2=c(2,3,2))
df_raw # 원본은 변경되지 않음
# 복사본 새로운 데이터 프레임
df_new <- df_raw
df_new

# rename() 함수 :dplr 패키지
?rename
df_new <- rename(df_new, v2=var2) # var2 를 v2로 수정 (컬럼명 수정)
df_new

df_raw
# var1 var2
# 1    1    2
# 2    2    3
# 3    1    2
df_new
# var1 v2
# 1    1  2
# 2    2  3
# 3    1  2