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

df = pd.DataFrame(data, index=['정윤', '희애'],
                  columns=['나이', '성별', '학교'])
print(df)
'''
         0  1    2
  정윤  15  남  장안중
  희애  16  여  수성중
'''

