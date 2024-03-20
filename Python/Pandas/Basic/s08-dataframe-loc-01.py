# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:11:09 2024

@author: Shin
"""

# 데이터프레임 : Dataframe

import pandas as pd
# list
data = [
    # 0    1       2
    [14, '남', '수성중'],
    [15, '남', '장안중'], # 0행
    [16, '여', '수성중'],  # 1행 # ,를 꼭 붙여 정수/슬라이스여야함으로 튜플이 아니라
    [17, '여', '수원대']  # 2행   

        ]

df = pd.DataFrame(data, index=['길동', '정윤', '희애', '유라'],
                  columns=['나이','성별', '학교'])
print(df)
'''
    나이 성별   학교
길동  14  남  수성중
정윤  15  남  장안중
희애  16  여  수성중
유라  17  여  수원대
'''
#%%
# 단일행 선택
# loc : 인덱스 선택
# 결과 : Series
ndf = df.loc['희애']
print(ndf) # Series
'''
나이     16
성별      여
학교    수성중
Name: 희애, dtype: object
'''
#%%
# 단일행 선택
# loc : 인덱스 선택
# 결과 : Series
df2 = df.loc[['희애']]
print(df2) # DataFrame
'''
  나이 성별   학교
희애  16  여  수성중
'''

#%%
# 다중행 선택
# loc : 인덱스, 슬라이싱(범위지정)
# 결과: Dataframe
df3 = df.loc['정윤':'희애']
print(df3) # Dataframe
'''
    나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
'''
#%%
# 다중행 선택
# loc : 멀티 인덱스 지정
# 결과: Dataframe
df4 = df.loc[['정윤','희애', '길동']]
print(df4) # Dataframe
'''
       나이 성별   학교
   정윤  15  남  장안중
   희애  16  여  수성중
   길동  14  남  수성중
'''
































