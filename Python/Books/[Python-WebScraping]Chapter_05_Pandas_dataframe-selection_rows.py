# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:29:19 2024

@author: Shin
"""

# ### 5.2.3 표 데이터 선택

# #### 행 데이터 선택

# [5장: 183페이지]

# In[ ]:


import pandas as pd
import numpy as np
#%%

# series 는 백터(1차원) 형태
index_data = ['a', 'b', 'c', 'd', 'e'] # index용 데이터
data = [0.0, 1.0, 2.0, 3.0, 4.0] # 데이터
s1 = pd.Series(data, index = index_data)
s1


# In[ ]:


s1.loc['a'] # index 라벨 지정으로 하나의 행 데이터 선택
# 0.0

# In[ ]:


s1.loc[['a', 'c', 'e']] # index 라벨 리스트 지정으로 여러 행의 데이터를 선택 #list로 한번 더 지정
'''
a    0.0
c    2.0
e    4.0
dtype: float64
'''

# In[ ]:


s1.loc[['e', 'b', 'a']] # index 라벨 리스트 지정으로 여러 행의 데이터를 선택


# [5장: 184페이지]

# In[ ]:

# 범위 지정 
s1.loc['b':'d'] # index 라벨 슬라이싱으로 여러 행의 데이터를 선택 
'''
b    1.0
c    2.0
d    3.0
dtype: float64
'''
# In[ ]:


s1.iloc[1] # index 위치 지정으로 하나의 행 데이터를 선택
# 1.0

# In[ ]:


s1.iloc[[0, 2, 4]] # index 위치 리스트 지정으로 여러 행의 데이터를 선택


# In[ ]:


s1.iloc[1:4] # index 위치 슬라이싱으로 여러 행의 데이터를 선택
'''
b    1.0
c    2.0
d    3.0
dtype: float64
'''
# In[ ]:


s1.loc['a':'c'] = 10 # 여러 행의 데이터에 스칼라 값을 지정
s1
'''
a    10.0
b    10.0
c    10.0
d     3.0
e     4.0
dtype: float64
'''

# [5장: 185페이지]

# In[ ]:


s1.iloc[3:5] = 20
s1 
'''
a    10.0
b    10.0
c    10.0
d    20.0
e    20.0
dtype: float64
'''

# In[ ]:
# 데이터 프레임 선택

import pandas as pd
import numpy as np
dict_data = {'A': [0, 10, 20, 30, 40],
             'B': [0, 0.1, 0.2, 0.3, 0.4],
             'C': [0, 100, 200, 300, 400]} # 딕셔너리 데이터

index_data = ['a', 'b', 'c', 'd', 'e'] # index 지정용 데이터

df1 = pd.DataFrame(dict_data, index=index_data) # 딕셔너리 데이터로부터 DataFrame 데이터 생성
df1


# In[ ]:

# 첫번 쨰 행 선택 # 선택 결과는 series임. dataframe이 아니라.
df1.loc['a'] # index 라벨 지정으로 하나의 행 데이터를 선택
'''
A    0.0
B    0.0
C    0.0
'''
# dataframe 형으로 결과를 얻을려면
df1.loc[['a']]
'''
   A    B  C
a  0  0.0  0
'''
# [5장: 186페이지]

# In[ ]:

# 다중 행 선택 
df1.loc[['a', 'c', 'e']] # index 라벨 리스트 지정으로 여러 행의 데이터를 선택


# In[ ]:


df1.loc['b':'d'] # index 라벨 슬라이싱으로 여러 행의 데이터를 선택


# In[ ]:
# index 위치 지정: 0부터 시작

cs1 = df1.iloc[2]
print(cs1)
'''
A     20.0
B      0.2
C    200.0
Name: c, dtype: float64
'''
 # index 위치 지정으로 하나의 행 데이터를 선택
print(type(cs1), cs1) # <class 'pandas.core.series.Series'>


# In[ ]:


df1.iloc[[1, 3, 4]] # index 위치 리스트 지정으로 여러 행의 데이터를 선택


# [5장: 187페이지]

# In[ ]:

# 인덱스 위치: 1~2번쨰 
df1.iloc[1:3] # index 위치 슬라이싱으로 여러 행의 데이터를 선택


# In[ ]:

# 인덱스 'a'부터 'c'까지의 모든 요소 값을 50으로 변경
df1.loc['a':'c'] = 50
df1


# [5장: 188페이지]

# In[ ]:


# Series 데이터 생성
# 값의 범위: -3부터 5까지
s = pd.Series(range(-3, 6)) 
s

#%%
s[s > 0] # 조건을 만족하는 행 데이터 가져오기
#%%
# AND : & 
# and는 지원하지 않음.

s[(s >= -2) & (s%2 == 0)] # 두 조건을 모두 만족하는 행 데이터 가져오기 
'''
1   -2
3    0
5    2
7    4
dtype: int64
'''
# In[ ]:


# DataFrame 데이터 생성
dict_data = {'지점': ['서울', '대전', '대구', '부산', '광주'],
             '1월': [558, 234, 340, 380, 213],
             '2월': [437, 216, 238, 290, 194], 
             '3월': [337, 196, 209, 272, 186]} # 딕셔너리 데이터

df = pd.DataFrame(dict_data) # 딕셔너리 데이터로부터 DataFrame 데이터 생성
df


# [5장: 189페이지]


# In[ ]:
    
jgt = df['1월'] >= 300
jgt # series
'''
0     True
1    False
2     True
3     True
4    False
Name: 1월, dtype: bool
'''
jlt = list(jgt)
print(jlt) # [True, False, True, True, False]

# 리스트의 True인 행만 선택
df[pd.Series(jlt)] # = df[jlt]
print(df[jlt])
'''
 지점   1월   2월   3월
0  서울  558  437  337
2  대구  340  238  209
3  부산  380  290  272
'''
df[df['1월'] >= 300] # 조건을 만족하는 행 데이터 가져오기


# In[ ]:

# OR : | 
df[(df['지점'] == '서울') | (df['지점'] == '부산')] # 둘 중 하나만 만족해도 행을 선택


# [5장: 190페이지]

# In[ ]:


df[df['지점'].isin(['서울','부산'])] 


# In[ ]:


dict_data = { '제품ID':['P501', 'P502', 'P503', 'P504', 'P505', 'P506', 'P507'],
              '판매가격':[6400, 5400, 9400, 10400, 9800, 1200, 3400],
              '판매량':[63, 56, 98, 48, 72, 59, 43],
              '이익률':[0.30, 0.21, 0.15, 0.25, 0.45, 0.47, 0.32]}  # 딕셔너리 데이터

df2 = pd.DataFrame(dict_data)
df2


# [5장: 191페이지]

# In[ ]:


df2.head() # 처음 5개의 행 데이터 선택


# In[ ]:


df2.head(2) # 처음 2개의 행 데이터 선택


# [5장: 192페이지]

# In[ ]:


df2.tail() # 마지막 5개의 행 데이터 선택


# In[ ]:


df2.tail(3) # 마지막 3개의 행 데이터 선택


# In[ ]:
# jupyter notebook
'''
with pd.option_context('display.max_rows',4):
    pd.set_option("show_dimensions", False)
    display(df2)
'''
