#백터(vector)
#합/교/차집합

#합집합: union()
#양쪽의 모든 데이터가 선택
#중복데이터는 하나만 선택
n <- c(1,3,5,7)
m <- c(3,5,9)
nm <- union(n,m) # 1 3 5 7 9

#교집합: intersect()
#양쪽에 동시에 존재하는 데이터만 선택
nxm <- intersect(n,m)
mxn <- intersect(m,n) # 3 5

#차집합: setdiff()
#n에는 있고 m에는 없는 데이터
ndm <- setdiff(n,m) # 1  7

#m에는 있고 n에는 없는 데이터 
mdn <- setdiff(m,n)
mdn # 9 

#######################문제


# n ,m에서 교집합(n,m)을 제외한 데이터
nmc <- c(n,m) # 단순결합(중복허용)
nmc # 1 3 5 7 9

# 결과 <- 차집합(합집합, 교집합)
nmx <- setdiff(nmc, intersect(n,m)) = nmu <- setdiff(nm, intersect(n,m))
nmx #  1 7 9



