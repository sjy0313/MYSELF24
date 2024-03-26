
# ### 5.2.4 표 데이터 통합

# [5장: 200페이지]

# In[ ]:
#%%
'''
axis : 0 : 세로방향(index방향) 기본값
axis : 1 : 가로방향(column방향)
ignore_index : 원복 데이터의 index 사용여부
    -원본 데이터의 index 사용여부
    -False: 연결할 데이터의 index를 그대로 사용
    -True: 원본 데이터를 무시하고 0부터 순차적으로 새롭게 지정
join:
    -'outer': 모든 데이터를 선택, 기본값
    -'inner': 공통 데이터만 선택
'''
#%%

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
'''
0    10
1    20
2    30
0    40
1    50
2    60
dtype: int64
'''

# [5장: 201페이지]

# In[ ]:


# 기존 index를 무시하고 새로운 index를 생성
pd.concat([s1, s2], ignore_index=True) 
'''
0    10
1    20
2    30
3    40
4    50
5    60
dtype: int64
'''

# In[ ]:


# 기존 index를 무시하고 새로운 index를 생성
pd.concat([s1, s2, s3], ignore_index=True) 
'''
0    10
1    20
2    30
3    40
4    50
5    60
6    70
7    80
8    90
dtype: int64
'''

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
'''
    물리  화학
0   95  91
1   92  93
2   98  97
3  100  99
4   87  85
5   89  90
'''

# In[ ]:


# 세로 방향으로 연결(기존 index를 무시)
# 칼럼의 갯수가 일치하지 않으면 데이터가 없는 부분은 NAN으로 채워짐
pd.concat([df2, df3], ignore_index=True) 
'''
   물리    화학
0  87  85.0
1  89  90.0
2  72   NaN
3  85   NaN
'''

# [5장: 204페이지]

# In[ ]:


# 세로 방향으로 공통 데이터만 연결(기존 index를 무시)
pd.concat([df2, df3], ignore_index=True, join='inner')


# In[ ]:


# 가로 방향으로 연결
pd.concat([df1, df4], axis=1)
'''
 물리  화학  생명과학  지구과학
0   95  91    94    86
1   92  93    91    94
2   98  97    94    89
3  100  99    83    93
'''

# In[ ]:


# 가로 방향으로 모든 데이터 연결 outer-join
pd.concat([df2, df4], axis=1) 
'''
   물리    화학  생명과학  지구과학
0  87.0  85.0    94    86
1  89.0  90.0    91    94
2   NaN   NaN    94    89
3   NaN   NaN    83    93
'''
# [5장: 205페이지]

# In[ ]:


# 가로 방향으로 공통 데이터만 연결 inner-join
pd.concat([df2, df4], axis=1, join='inner')
'''
 물리  화학  생명과학  지구과학
0  87  85    94    86
1  89  90    91    94
'''
#%%
# 세로 방향인 경우 공통된 칼럼이 없으므로 
# 결합 할 데이터가 없다
pd.concat([df2, df4], axis=0, join='inner')
'''
Empty DataFrame
Columns: []
Index: [0, 1, 0, 1, 2, 3]
'''

