
# #### 열 데이터 선택

# [5장: 193페이지]

# In[ ]:


df2['제품ID']


# [5장: 194페이지]

# In[ ]:


df2[['제품ID']]


# In[ ]:


df2[['제품ID', '이익률', '판매가격']]


# [5장: 195페이지]

# In[ ]:


# 지정한 열 데이터의 모든 값을 스칼라 값으로 변경
df2['이익률'] = 0.5 # '이익률' 열 데이터를 0.5로 변경
df2


# #### 행과 열 데이터 선택

# In[ ]:


dict_data = {'A': [0, 1, 2, 3, 4],
             'B': [10, 11, 12, 13, 14],
             'C': [20, 21, 22, 23, 24]} # 딕셔너리 데이터

index_data = ['a', 'b', 'c', 'd', 'e'] # index 지정용 데이터

df = pd.DataFrame(dict_data, index=index_data) # DataFrame 데이터 생성
df


# [5장: 196페이지]

# In[ ]:


df.loc['a', 'A'] # loc 이용


# In[ ]:


df.iloc[0, 0] # iloc 이용


# In[ ]:


df.loc['a':'c', ['A', 'B']] # loc 이용


# In[ ]:


df.iloc[0:3, 0:2] # iloc 이용


# [5장: 197페이지]

# In[ ]:


df.loc[:, ['A', 'B']] # loc 이용


# In[ ]:


df.iloc[:, 0:2] # iloc 이용


# In[ ]:


df.loc[df['A']>2, ['A', 'B']] # loc 이용


# [5장: 198페이지]

# In[ ]:


df.loc['a':'c', ['A', 'B']] = 50 # 스칼라 값 지정
df


# In[ ]:


df.iloc[3:5, 1:3] = 100 # 스칼라 값 지정
df


# In[ ]:


df.loc[df['B']<70, 'B'] = 70 # 스칼라 값 지정
df


# [5장: 199페이지]

# In[ ]:


df.loc[df['C']<30, 'D'] = 40 # loc 이용. 스칼라 값 지정
df


# ### 5.2.4 표 데이터 통합

# [5장: 200페이지]

# In[ ]:


import pandas as pd

s1 = pd.Series([10, 20, 30])
s1


# In[ ]:


s2 = pd.Series([40, 50, 60])
s2


# In[ ]:


s3 = pd.Series([70, 80, 90])
s3


# In[ ]:


# 세로 방향으로 연결
pd.concat([s1, s2])


# [5장: 201페이지]

# In[ ]:


# 기존 index를 무시하고 새로운 index를 생성
pd.concat([s1, s2], ignore_index=True) 


# In[ ]:


# 기존 index를 무시하고 새로운 index를 생성
pd.concat([s1, s2, s3], ignore_index=True) 


# [5장: 202페이지]

# In[ ]:


df1 = pd.DataFrame({'물리':[95, 92, 98, 100],
                    '화학':[91, 93, 97, 99]})
df1


# In[ ]:


df2 = pd.DataFrame({'물리':[87, 89],
                    '화학':[85, 90]})
df2


# In[ ]:


df3 = pd.DataFrame({'물리':[72, 85]})
df3


# In[ ]:


df4 = pd.DataFrame({'생명과학':[94, 91, 94, 83],
                    '지구과학':[86, 94, 89, 93]})
df4


# [5장: 203페이지]

# In[ ]:


# 세로 방향으로 연결(기존 index를 무시)
pd.concat([df1, df2], ignore_index=True)


# In[ ]:


# 세로 방향으로 연결(기존 index를 무시)
pd.concat([df2, df3], ignore_index=True) 


# [5장: 204페이지]

# In[ ]:


# 세로 방향으로 공통 데이터만 연결(기존 index를 무시)
pd.concat([df2, df3], ignore_index=True, join='inner')


# In[ ]:


# 가로 방향으로 연결
pd.concat([df1, df4], axis=1)


# In[ ]:


# 가로 방향으로 모든 데이터 연결
pd.concat([df2, df4], axis=1) 


# [5장: 205페이지]

# In[ ]:


# 가로 방향으로 공통 데이터만 연결
pd.concat([df2, df4], axis=1, join='inner')


# ## 5.3 정리
