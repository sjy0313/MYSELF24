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
#%%
import pandas as pd
# list

score = [
    [90, 98, 85, 100],
    [90, 98, 85, 100],
    [90, 98, 85, 100],
    [90, 98, 85, 100],         
]

df = pd.DataFrame(score, columns=['수학','영어','음악','체육'],
                  index=['서준','준서','인아','수성'])
print(df)
# 빈 인덱스(행) 생성
ndf = df.reset_index()
print(ndf)
# '인덱스
# s04-dataframe-index-column01.py, s06-dataframe-reset-index01.py 참조
ndf.rename(columns={'index':'이름'}, inplace=True) # 원본 변경
print(ndf)
pdf = ndf.set_index('이름')
print(pdf)

# 학생별 총점
df['총합'] = pdf.sum(axis=1)
print(df)

#%%
# 전체 지정 
df3 = df.loc[:,['수학','영어','음악','체육']]
print(df3)
df2 = df.iloc[:,:4]
print(df2)
# df2 = df3
#%%

# 시리즈 형태
df4 = df2.iloc[0]
print(df4)
'''
수학     90
영어     98
음악     85
체육    100
Name: 서준, dtype: int64
'''
# 시리즈에서 속성값인 value 참조
print(df4.values)
# [ 90  98  85 100]
#하나의 요소값을 참조할 떄는 series로 바꾼 후 속성값을 참조 가능하지만
#여러개의 속성값을 확인할 때는 
df.columns # Index(['수학', '영어', '음악', '체육'], dtype='object')
df.index # Index(['서준', '준서', '인아', '수성'], dtype='object')
#%%

# 반복문으로 총합 및 평균 구하기
# 총합
score1 = [90, 98, 85, 100]
total = [sum(score1) for score1 in score]
print(total)

# 과목별 총합
# 결과예시: 
# 이름 수학 영어 음악 체육 총점 평균
# 서준  90   98    85  100  373  93  
# 준서  90   98    85  100  373  93  
# 인아  90   98    85  100  373  93  
# 수성  90   98    85  100  373  93
# 총점 360  392   100  400    0   0
# 평균  90   98     80 100    0   0

# 수학 총합
math = df.iloc[:,0] 
print(math.values)
# [90 90 90 90]
tmath = sum(math.values)
print(tmath) # 360

# 영어 총합
english = df.iloc[:,1]
print(english.values)
tenglish = sum(english.values)
print(tenglish) # 392

# 평균: 
score1 = [90, 98, 85, 100]
avg = [sum(score1) / len(score1) for score1 in score]
print(avg) 

# 과목별 평균
#%%

ndf['총점'] = 0 
ndf['평균'] = 0
# 행추가
ndf.loc['평균'] = 0
print ("#학생별 총점 및 평균#")
for x in range(len(ndf)):
    rows = ndf.iloc[x, :]
    tot = 0 
    for val in rows: 
        tot += val
    ndf.iloc[x:4] = tot 
    ndf.iloc[x,5] = tot // cnt







