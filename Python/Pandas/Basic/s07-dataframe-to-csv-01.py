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
    [15, '남', '장안중'], # 0행
    [16, '여', '수성중'],  # 1행 # ,를 꼭 붙여 정수/슬라이스여야함으로 튜플이 아니라
    [17, '여', '수원대']  # 2행     
        ]

df = pd.DataFrame(data, index=['정윤', '희애', '유라'],
                  columns=['나이','성별', '학교'])
print(df)
'''
  나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
유라  17  여  수원대
'''

#%%
# 파일저장 
# 기본값: index=True, header=True, sep=' ')
df.to_csv("./학생성적.txt")

# 저장결과: 학생성적.txt
'''
,나이,성별,학교
정윤,15,남,장안중
희애,16,여,수성중
유라,17,여,수원대
'''
df.to_csv("./학생성적-noindex.txt", index=False)
# 저장결과: 학생성적-noindex.txt
'''
나이,성별,학교
15,남,장안중
16,여,수성중
17,여,수원대
'''
#%%

ndf = df.reset_index()
ndf.rename(columns={'index':'이름'}, inplace=True)
ndf.to_csv("./학생성적-index-이름.txt", index=False)
# 저장결과: 학생성적-index-column.txt
'''
이름,나이,성별,학교
정윤,15,남,장안중
희애,16,여,수성중
유라,17,여,수원대
'''

#%%
# 위에서 저장한 파일 읽기
rdf = pd.read_csv("./학생성적-index-이름.txt")
rdf.set_index('이름', inplace=True)
print(rdf)
'''
   나이 성별   학교
이름            
정윤  15  남  장안중
희애  16  여  수성중
유라  17  여  수원대
'''
#%%

odf = pd.read_csv("./학생성적.txt")
print(odf)
'''
 Unnamed: 0   나이 성별   학교
0         정윤  15  남  장안중
1         희애  16  여  수성중
2         유라  17  여  수원대
'''
odf.rename(columns={'Unnamed: 0':'이름'}, inplace=True) # inplace=True 원본변경
print(odf)
'''
  이름  나이 성별   학교
0  정윤  15  남  장안중
1  희애  16  여  수성중
2  유라  17  여  수원대
'''





















