# 파일 입출력

# read.table() 입력할 떄
#칼럼: 공백, 텝, 콜론(;), 콤마 등으로 구분된 자료를 파일에서 읽음
# 옵션: header=T or F, 
#student.txt에서 4라인에서 enter를 쳐야지 마지막 라인으로 인식

#파일 읽기
student <- read.table(file="./student.txt")
student
student <- edit(student)
student

#헤더 포함 
student_hdr <- read.table(file="student-header.txt", header=TRUE)
student_hdr
View(student_hdr)

student_hdr$번호
student_hdr$이름
student_hdr$신장
student_hdr$몸무게

# 번호   이름 신장 몸무게
# 1 1010 김좌진  156  45
# 2 1020 홍길동  180  56
# 3 2010 이순신  190  86
# 4 3010 전우치  178  78



#write.table()
#데이터프레임을 파일로 저장

#파일 읽기
student <- read.table(file="./student.txt")
student


student <- read.table(file="./student-header.txt", header=TRUE)
student

new_student <- data.frame(번호=c("4000", "5000"),
                          이름=c("사오정", "오징어"),
                          신장=c(140,70),
                          몸무게=c(44, 7))
new_student 

#행 추가 : rbind() 함수 = 행추가/ cbind)() = 열추가
df_student <- rbind(student, new_student)
df_student
# 번호   이름 신장 몸무게
# 1 1010 김좌진  156     45
# 2 1020 홍길동  180     56
# 3 2010 이순신  190     86
# 4 3010 전우치  178     78
# 5 4000 사오정  140     44
# 6 5000 오징어   70      7


#파일 저장 (변경 데이터프레임 저장) 
# row.names = 행 이름 지정 유무
# col.names = 열 이름 지정 유무
# = 데이터 프레임을 ./studen_wt.txt에 저장 옵션으로 행/열 이름 무시
write.table(df_student,"./student_wt.txt",row.names=T, col.names=T)

help(write.table)

write.table(student,"./studen-header-wt.txt",row.names=T, col.names=T)
write.table(student,"./studen_wt.txt",row.names=F, col.names=F)





