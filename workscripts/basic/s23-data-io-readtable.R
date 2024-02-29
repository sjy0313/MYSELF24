# 파일 입출력


read.csv()
help(read.csv)
# read.table()
#칼럼: 공백, 텝, 콜론(;), 콤마 등으로 구분된 자료를 파일에서 읽음
# 옵션: header=T or F, sep=''

# 한 행이 하나의 컬럼으로 처리 됨
# 컬럼 구분자 (,)로 처리
student <- read.csv(file="./basic/student.csv", head=F)
student

# 한 행이 하나의 컬럼으로 처리 됨
student <- read.table(file="./basic/student.csv")
student

# sep: 컬럼의 구분자 지정, 콤마(,) csv(=,로 구분된 텍스트파일 comma-separated vales)
student1 <- read.table(file="./basic/student.csv", sep=',')
student1

# 존재하는 파일읽을 때 
student <- read.table(file="./basic/student.txt")
student
edit(student)

