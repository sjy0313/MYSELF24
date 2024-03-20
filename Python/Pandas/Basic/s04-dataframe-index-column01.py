# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:52:50 2024

@author: Shin
"""

# 판다스
# 데이터프레임 : Dataframe
# 2차원 배열, 행열(matrix)
# 행 : 인덱스, row index
# 열 : column, Series
# 
# 형식:
# df = pd.DataFrame(data[,index=index_data, columns=columns_data])

#%%
import pandas as pd
# list
data = [
    # 0    1       2
    [15, '남', '장안중'], # 0행
    [16, '여', '수성중']  # 1행      
        ]

df = pd.DataFrame(data)
print(df)
'''
   0  1    2
0  15  남  장안중
1  16  여  수성중
'''
#%%
# 새로운 인덱스 지정
df.index=['정윤', '희애']
'''
   나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
'''
# 새로운 컬럼 지정
df.columns = ['나이', '성별', '학교']
print(df)
'''
    나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
'''
#%%
# 인덱스 변경
ndf = df.rename(index={'희애' :'정희'})
print(ndf)
'''
    나이 성별   학교
정윤  15  남  장안중
정희  16  여  수성중
'''
# 원하는 컬럼 변경
ndf = df.rename(columns={'학교':'중학교'})
print(ndf)
'''
  나이 성별  중학교
정윤  15  남  장안중
희애  16  여  수성중
'''
#%%

# 원본 변경 : inplace=True 여러개의 index, colum 값을 바꾸고 싶을 떄 dict형태 + , 활용
# 리턴: None
xdf = ndf.rename(index={'정윤' :'신정윤', '희애':'신정희'},
           columns={'나이':'연령'}, inplace=True)
print(ndf)
'''
 연령 성별  중학교
신정윤  15  남  장안중
신정희  16  여  수성중
'''
print(xdf)  # None 




























