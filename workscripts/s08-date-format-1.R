#날짜형
now <- "24/02/19"
dt <- as.Date(now, '%y/%m/%d') #%y: 년도 2자리
dt
mode(dt) #numeric
class(dt) #Date

today <- "2024-03-01"
t1 <- as.Date(today,'%Y-%m-%d') # %Y : 년도 4자리 
#자열을 날짜열로 변경할때 
t1
class(t1) $Date
# 시스템 날짜 
syst <- Sys.time()
syst #"2024-02-19 17:16:20 KST"
mode(syst) #numeric
class(syst) #"POSIXct" "POSIXt"
help(strptime)
systm <- as.POSIlt(syst, format="%Y/%m/%d")
systm

txm <- as.Date(syst, format="%Y-%m-%d")
txm
strptime(syst, "%Y/%m/%d %H:%M:%S")

as.POSIXlt(syst, format="%Y/%m/%d %H:%M:%S")
#시스템 날짜 
format(Sys.time(), "%Y/%m/%d %H:%M:%S") #"2024/02/19 17:39:03"
#로케일 확인
Sys.getlocale()



