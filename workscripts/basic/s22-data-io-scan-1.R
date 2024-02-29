# 데이터 입출력
#scan() : 키보드 입력
#edit() : 데이터프레임 입력(GUI)

# 키보드 입력
# 아무것도 입력하지 않고 Enter을 치면 입력 종료 

#숫자 입력
#애러 : 숫자를 입력하지 않고 문자형을 입력하면 애러 발생
# 
num <- scan()
num
sum(num)

# 문자입력
name <- scan(what=character())

# 문자입력
help(scan)
name <- scan(what=character())
name
mode(name) # "character"

# GUI 편집기 : edit() 함수
df <- data.frame() # 빈 데이터 프레임 생성
df
#빈 데이터프레임 
df <- edit(df)
df

# 데이터를 가지고 있는 데이터프레임 열기
df <- edit(df)
df
