# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:52:16 2024

@author: Shin
"""

# 문제
# 데이터프레임을 이용하여 총점과 평균을 구하라
# 1. '이름'을 인덱스로 지정
# 2. 각 학생의 총점과 평균
# 3. 각 과목별 총점과 평균
# 4. 처리 결과를 전체의 새로운 하나의 프레임으로 구성
#
# 결과예시: 
# 이름 수학 영어 음악 체육 총점 평균
# 서준  90   98    85  100  373  93  
# 준서  90   98    85  100  373  93  
# 인아  90   98    85  100  373  93  
# 수성  90   98    85  100  373  93
# 총점 360  392   100  400    0   0
# 평균  90   98     80 100    0   0
# 조건:
#   1. 반복문을 사용하라
#   2. 각 행과 열을 하나씩 읽어서 처리
#
import pandas as pd
# list

score = [
    [90, 98, 85, 100],
    [90, 98, 85, 100],
    [90, 98, 85, 100],
    [90, 98, 85, 100],         
]

df = pd.DataFrame(score, columns=['수학','영어','음악','체육'],
                  index=['서준', '준서', '인아', '수성'])
print(df)
# 빈 인덱스(행) 생성
ndf = df.reset_index()
print(ndf)
# '인덱스
# s04-dataframe-index-column01.py, s06-dataframe-reset-index01.py 참조
ndf.rename(columns={'index':'이름'}, inplace=True) # 원본 변경

pdf = ndf.set_index('이름')
print(pdf)


xdf = ndf.rename(index={'정윤' :'신정윤', '희애':'신정희'},
           columns={'나이':'연령'}, inplace=True)
print(ndf)






'총점', '평균'
print(df)



score = [90, 98, 85, 100]
total = 0
for sc in range(4) : 
   total += score[sc]
print(total)