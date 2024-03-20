# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:52:50 2024

@author: Shin
"""

# 판다스 (데이터프레임은 python기본 패키지에 존재 x)
# 데이터프레임 : Dataframe
# 2차원 배열, 행열(matrix)
# 행 : 인덱스, row index
# 열 : column, Series
# 
# 형식:
# df = pd.DataFrame(data[,index=index_data, columns=columns_data])
# 행/열 삭제

#%%
import pandas as pd
# list
data = [
    # 0    1       2
    [15, '남', '장안중'], # 0행
    [16, '여', '수성중']  # 1행      
        ]

df = pd.DataFrame(data, index=['정윤', '희애'],
                  columns=['나이','성별', '학교'])
print(df)
'''
   나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
'''
#%%
# reset_index()
# index가 칼럼으로 이동하여 새로운 칼럼이 생성
# index :0부터 순번 부여된다.
ndf = df.reset_index()
print(ndf)
'''
   index  나이 성별   학교
0    정윤  15  남  장안중
1    희애  16  여  수성중
'''
#%%
# set_index() :  칼럼을 index로 이동(변경)하고 기존 인덱스는 삭제
xdf = ndf.set_index('index')
print(xdf)
'''
       나이 성별   학교
index            
정윤     15  남  장안중
희애     16  여  수성중
''' 
#%%

xdf = ndf.set_index('학교') 
print(xdf)
'''
 index  나이 성별
학교              
장안중    정윤  15  남
수성중    희애  16  여
'''
ydf = xdf.set_index('학교') 
print(ydf)
'''
      나이 성별
학교        
장안중  15  남
수성중  16  여
'''








































