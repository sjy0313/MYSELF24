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
# dict
data = {
        'c0' : [1,2,3], # column, series(형태)
        'c1' : [4,5,6], # column, series
        'c2' : [7,8,9], # column, series
        'c3' : [10,11,12], # column, series
        'c4' : [13,14,15] # column, series
}

df = pd.DataFrame(data, index=['1행', '2행', '3행'])
print(type(df)) # <class 'pandas.core.frame.DataFrame'>
# ValueError: All arrays must be of the same length
# 반드시 행의 개수가 모든 컬럼의 행의 갯수가 일치해야함. # [1,2,3,4],(x)
print(df)
'''
     c0  c1  c2  c3  c4
1행   1   4   7  10  13
2행   2   5   8  11  14
3행   3   6   9  12  15
'''


