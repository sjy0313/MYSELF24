#작업공간
#working directory 현재작업 디렉토리 얻기
getwd()
#change working directory 작업 디렉토리 변경 
setwd("d:/WORKSPACE(SHIN)/Rlang")
getwd()
#히스토그램을 파일로 저장
par(mfrow=c(1,1)) #그래프 영역 1개 지정 
pdf("./hist-1.pdf") #지정된 경로에 파일로 결과를 출력 (./ 어딘지 뭐르는 위치에 hist-1저장)
hist(rnorm(30)) #난수 30개를 발생하여 히스토그램 그리기
dev.off() #출력 닫기

#작업 디렉토리 변경

setwd("d:/WORKSPACE(SHIN)/Rlang")
getwd()
