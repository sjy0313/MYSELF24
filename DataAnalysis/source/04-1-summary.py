#!/usr/bin/env python
# coding: utf-8

# # 04-1 통계로 요약하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/04-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/04-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 기술통계 구하기

# In[1]:


import gdown

gdown.download('https://bit.ly/3736JW1', './data/ns_book6.csv', quiet=False)
# quiet=False

# In[2]:


import pandas as pd

ns_book6 = pd.read_csv('./data/ns_book6.csv', low_memory=False)
ns_book6.head()
# low_memory 자료를 분활해서 다운 (True 기본값)
# low_memory=False를 설정하면 pandas는 대용량 데이터를 읽을 때 
# 한 번에 더 많은 메모리를 사용하게 됩니다. 이 옵션을 설정하는 이유는 때로는 
# 대용량 데이터를 처리할 때 메모리를 효율적으로 사용하는 것보다 읽기 속도를 높이는 것이
# 더 중요한 경우가 있기 때문입니다.

# In[3]:
# 기술통계는 자료의 내용을 압축하여 설명하는 방법
# 기술통계 자동 추출 describe()
# count -> 누락된 값을 제외한 데이터의 개수
# mean -> 평균 / std -> 표준편차 / min -> 최솟값 / 50% 중앙값 / 25%,75% -> 25%지점과 75% 지점
# 에 놓인 값 / max -> 최댓값
ns_book6.describe() 
'''
   번호           발행년도           도서권수           대출건수
count  379976.000000  379976.000000  379976.000000  379976.000000
mean   201726.332847    2008.516306       1.135874      11.504629
std    115836.454596       8.780529       0.483343      19.241926
min         1.000000    1947.000000       0.000000       0.000000
25%    102202.750000    2003.000000       1.000000       2.000000
50%    203179.500000    2009.000000       1.000000       6.000000
75%    301630.250000    2015.000000       1.000000      14.000000
max    401681.000000    2650.000000      40.000000    1765.000000
'''

# In[4]:

# 도서권수가 0권인 개수와 비율
sum(ns_book6['도서권수']==0) # 3206
ns_book6_len = len(ns_book6)  
ns_book6_sum = sum(ns_book6['도서권수']==0)  
ns_book6_rate = ns_book6_sum / ns_book6_len 
print(f"{round(ns_book6_rate * 100)}%") #(0.8437374992104764) 전체권수 대비 약 1%를 차지함.
# In[5]:

# '도서권수'가 0보다 큰 df 생성
ns_book7 = ns_book6[ns_book6['도서권수']>0] # 378876


# In[6]:

# 백분위수 범위 조정
# percentiles=[...]
# 30%, 60%, 90%
ns_book7.describe(percentiles=[0.3, 0.6, 0.9])


# In[7]:
# 열의 데이터 타입이 수치가 아닌 데이터 타입의 열의 기술통계를 보고싶다면
# include = 'object' 지정 
# 수치형에 대한 통계치 뿐만 아니라 Object 타입은 주로 문자열 데이터를 포함하며, 
#이러한 열에 대해서도 일부 통계 정보를 제공합니다. 이에는 열의 개수, 
#유일한 값의 개수, 가장 많이 나타나는 값과 해당 값의 빈도 등이 포함될 수 있습니다. 
ns_book7_object_describe = ns_book7.describe(include='object')
# 예시)
import pandas as pd

# Sample DataFrame
data = {'A': ['foo', 'bar', 'foo', 'bar', 'foo'],
        'B': [1, 2, 3, 4, 5],
        'C': [0.1, 0.2, 0.3, 0.4, 0.5]}
df = pd.DataFrame(data)

# 기본 요약 통계 정보
print(df.describe())

# 객체 열에 대한 요약 통계 정보 포함
print(df.describe(include='object'))
'''
              B         C
count  5.000000  5.000000
mean   3.000000  0.300000
std    1.581139  0.158114 # 표준편차 즉 데이터가 평균으로 부터 떨어진 정도
#  즉 평균 3 | 0.3보다 +-1.58 | +-0.158 만큼 데이터들이 분포해 있음을 의미
1.5 3 4.5 앞에 3개의 값들 사이에 데이터가 분포해 있음을 알 수 있다.
min    1.000000  0.100000
25%    2.000000  0.200000
50%    3.000000  0.300000
75%    4.000000  0.400000
max    5.000000  0.500000
          A
count     5
unique    2
top     foo
freq      3
'''
# count : 누락값을 제외한 데이터 개수
# unique : 행의 고유한 값의 개수
# top : 가장 많이 등장하는 값
# freq : top행에 등장하는 항목의 빈도수 

# ## 평균

# $평균 = \dfrac{a + b + c}{3}$
# 
# $평균 = \dfrac{x_1 + x_2 + x_3}{3}$

# In[8]:


x = [10, 20, 30]
sum = 0
for i in range(3):
    sum += x[i]
print("평균:", sum / len(x))
 # 평균: 20.0

# $평균 = \dfrac{x_1 + x_2 + x_3}{3} = \dfrac{\sum_{i=1}^{3} x_i}{3}$
# 
# $평균 대출건수 = \dfrac{\sum_{i=1}^{376770} x_i}{376770}$

# In[9]:


ns_book7['대출건수'].mean() 

# 11.593438968070707
# ## 중앙값

# In[10]:


ns_book7['대출건수'].median()
# 6.0

# In[11]:


temp_df = pd.DataFrame([1,2,3,4]) # (2+3)/2
temp_df.median() # 2.5


# In[12]:
# 교제 172쪽 참조
# df.duplicates()참조 # 중복값을 제거한 중앙값

ns_book7['대출건수'].drop_duplicates().median() # 183.0
# 객체를 따로 생성할 필요없이 위처럼 2개의 매서드를 .을 활용하여 연결
ns_book7_unique = ns_book7['대출건수'].drop_duplicates()
ns_book7_unique.median()  # 183.0
#drop_duplicates() 메서드는 Pandas에서 사용되며 데이터프레임에서 중복된 행을 제거하는 데 사용
# 행의 내용을 기준으로 중복을 식별하고, 중복된 행을 제거하고 새로운 df출력.
 


# ## 최솟값, 최댓값

# In[13]:


ns_book7['대출건수'].min() # 0


# In[14]:


ns_book7['대출건수'].max() # 1765


# ## 분위수

# In[15]:

 # 분위수 계산 하위 25%에 위치한 값 
ns_book7['대출건수'].quantile(0.25) # 2.0


# In[16]:

 # 한번에 여러개 분위 수 계산할 떄 []안에 여러개 지정하면 series 형태로 출력
ns_book7['대출건수'].quantile([0.25,0.5,0.75]) 
print(type(ns_book7['대출건수'].quantile([0.25,0.5,0.75])))
# <class 'pandas.core.series.Series'>

# In[17]:

 
pd.Series([1,2,3,4,5]).quantile(0.9) #  4.6


# In[18]:
# quantile()매서드의 parameter는 interpolation 
# interpolation에서 기본값은 linear이며 양쪽 분위수에 비례하여 결정된다는 뜻으로
# if, 분위수 0.75와, 0.9에 비례하여 결정된다.
# a= 0.9-0.75 ,A=1-.075, B = 5-4 일때,(A:a = B:b) 0.25:0.15 = 1:b, 이떄 b의 값은
# 두 비례값이 같을 떄 0.25b = 0.15, b= 0.15/0.25 = 0.6
4 + (0.9-0.75)*(5-4)/(1.0-0.75) #  0.6


# In[19]:

# interpolation 두 지점 사이에 놓인 특정 위치의 값을 구하는 방법을 보간
# 분위수에 상관없이 무조건 두 수 사이의 중앙값을 사용
pd.Series([1,2,3,4,5]).quantile(0.9, interpolation='midpoint') # 4.5

# In[20]:

# interpolation='nearest' 
# 두 수 중에서 가까운 값을 선택
# 4.6은 5에 더 가까움
pd.Series([1,2,3,4,5]).quantile(0.9, interpolation='nearest') # 5


# In[21]:
# 대출 데이터에서 대출권수 10이 위치한 백분위값
# 백분위 구하기 percentile rank
# 대출권수가 10권미만 이면 false 반대면 True
borrow_10_flag = ns_book7['대출건수'] < 10
print(borrow_10_flag)
'''
0         True
1         True
2         True
3         True
4         True

379971    True
379972    True
379973    True
379974    True
379975    True
Name: 대출건수, Length: 376770, dtype: bool
'''
# boolean array 출력

# In[22]:

# 판다스에서 불리언 자료를 산술연산하면 True = 1/ False= 0 취급
count_true= (borrow_10_flag).sum() # True값이 출력된 개수의 합
print(count_true) # 241235
count_true/len(borrow_10_flag) # 0.6402712530190833
# 위 과정은 대출권수가 10권 미만인 데이터 비율을 구하는 과정이다
# mean()매서드로 과정을 한 번에 요약하여 구할 수 있다. 
borrow_10_flag.mean() # 0.6402712530190833
# borrow_10_flag에서 mean()을 호출하여 평균을 구하면 10보다
#작은 값이 차지 하는 비율을 얻을 수 있음. 

# In[23]:

# 10에 대한 백분위는 0.65임을 알 수 있다.
ns_book7['대출건수'].quantile(0.65) #  10
#상위65%의 데이터들이 10권 미만으로 대출되었음.


# ## 분산
# 편차 : 평균을 뺸 값
# 분산 : 평균을 뺸값 = 편차제곱합의 평균
# 불편분산 : 편차제곱합 / n-1
# 표준편차 : 분산의 제곱근(루트)
#%%
# 분산(variance): 평균으로부터 데이터가 얼마나 퍼져있는지 나타내는 통계량
# 분산이 작다는 의미 : 데이터들이 평균으로 부터 가까운 거리에 분포해 있다는 뜻
# 반대로 분산이 크다는 의미는 평균으로 부터 값들이 멀리 분포해 있음을 의미
#%%

# $ s^2 = \dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}$
# 
# $ \bar{x} = \dfrac{\sum_{i=1}^n x_i}{n}$

# In[24]:

#분산
ns_book7['대출건수'].var() 
#표준편차
import numpy as np
import math
math.sqrt(371.69563042906674) # 19.279409493785508
np.sqrt(371.69563042906674)
ns_book7['대출건수'].std()
# 371.69563042906674

# ## 표준 편차

# $ s = \sqrt{\dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}}$

# In[25]:
# 파이썬 판다스에서 표준편차를 계산할 떄 std()활용

ns_book7['대출건수'].std()
# 19.279409493785508

# $\sqrt{4}=2$

# In[26]:

# Numpy 는 주로 머신러닝에 많이 사용되고/ Pandas는 데이터 분석에 사용되기 때문에 
# ddof()의 기본값이 numpy는 1 / pandas 는 0 

import numpy as np
# 편차 : 평균을 뺸 값 

diff = ns_book7['대출건수'] - ns_book7['대출건수'].mean()
# 표준편차 = np.sqrt(불편분산)
# 표본 분산(sample variance)  n-1 (불편분산)
'''
일반적으로, 모집단의 분산은 모든 데이터 포인트와 모평균(모집단의 평균) 간의 
차이의 제곱의 평균으로 정의됩니다. 그러나 표본을 이용하여 모집단의 분산을 추정할 때, 
일반적으로 모집단의 평균을 알 수 없기 때문에 모집단 평균 대신 표본의 평균을 사용합니다.

불편분산은 이러한 표본 평균 대신 모집단 평균을 사용하여 계산된 분산입니다. 
이렇게 함으로써 표본의 크기에 대한 보정을 수행하여 추정량의 편향을 줄입니다.
불편분산은 데이터의 퍼짐 정도를 측정하는 중요한 통계량 중 하나이며, 
표본의 크기가 크지 않을 때 표본 분산보다 더 정확한 추정치를 제공합니다.
따라서 많은 통계적 분석에서 불편분산을 사용하여 데이터의 분산을 계산합니다.
'''
# 표본분산(불편분산) 연산 
# 표준편차 = 제곱근(편차제곱의 합 /(n-1))
# sqrt 제곱근 구할 떄 
np.sqrt( np.sum(diff**2) / (len(ns_book7)-1) )


# ## 최빈값

# In[27]:


ns_book7['도서명'].mode()
'''
0    승정원일기
Name: 도서명, dtype: object
'''

# In[28]:


ns_book7['발행년도'].mode()
'''
0    2012.0
Name: 발행년도, dtype: float64
'''

# ## 데이터프레임에서 기술통계 구하기

# In[29]:


ns_book7.mean(numeric_only=True)
'''
번호      202977.476649
발행년도      2008.460076
도서권수         1.145540
대출건수        11.593439
dtype: float64
'''

# In[30]:

#최빈값
# 컬럼: 첫번 째 컬럼('번호') 제외한 모든 컬럼
# 각 컬럼은 서로 관계가 없으며 독립적인 최빈값
ns_book7.loc[:, '도서명':].mode()
'''
   도서명             저자             출판사    발행년도  ...  주제분류번호 도서권수 대출건수        등록일자
0  승정원일기  세종대왕기념사업회 [편]  문학동네  2012.0  ...  813.6            1       0           1970-01-01
'''

# In[31]:


ns_book7.to_csv('./data/ns_book7.csv', index=False)


# ## 넘파이의 기술통계 함수

# ### 평균 구하기

# In[32]:


import numpy as np
#대출건수의 평균값 
ns_book7['대출건수'].mean() # 11.593438968070707
np.mean(ns_book7['대출건수']) # 11.593438968070707


# $\dfrac{국어점수 \times 2 + 수학점수}{3}$
# 
# $\dfrac{국어점수 \times 국어가중치 + 수학점수 \times 수학가중치}{국어가중치 + 수학가중치}$ 
# 
# $가중평균 = \dfrac{x_1 \times w_1 + x_2 \times w_2}{w_1 + w_2} = \dfrac{\sum_{i=1}^{2} x_i \times w_i}{\sum_{i=1}^{2} w_i}$

# In[33]:
# 인공지능 = 가중치를 찾는 것.
#  weights=1/ns_book7['도서권수']) 를 구하는 것.

# 가중 평균: 각 값의 주요도에 따라 가중치를 부여하여 계산한 평균값 
# weights 매개변수에 가중치를 제공하면 가중 평균을 구함
# 도서권수의 역수로 지정하여 
print(ns_book7['도서권수'])
np.average(ns_book7['대출건수'], weights=1/ns_book7['도서권수'])  # 10.543612175385386


# In[34]:


np.mean(ns_book7['대출건수']/ns_book7['도서권수']) # 9.873029861445774


# In[35]:
# 전체 대출건수 / 전체 도서권수
# 도서에 상관 없이 한 권 당 대출건수를 구함
ns_book7['대출건수'].sum()/ns_book7['도서권수'].sum() # 10.120503701300958


# ### 중앙값 구하기

# In[36]:


np.median(ns_book7['대출건수'])


# ### 최솟값, 최댓값 구하기

# In[37]:


np.min(ns_book7['대출건수'])


# In[38]:


np.max(ns_book7['대출건수'])


# ### 분위수 구하기

# In[39]:

# interpolation 기본값 linear 양쪽 분위수에 비례하여 결정
# interpolation 매개변수가 numpy 1.22(python >= 3.8) 버전부터 method로 바뀜
np.quantile(ns_book7['대출건수'], [0.25,0.5,0.75]) # array([ 2.,  6., 14.])


# ### 분산 구하기
# numpy : n
# pandas: n-1
# numpy : ddof(0,1)

# In[40]:


np.var(ns_book7['대출건수']) # 371.6946438971496


# $ s^2 = \dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}$

# In[41]:

# pandas : 넘파이 방식, n
ns_book7['대출건수'].var(ddof=0) # 371.6946438971496


# In[42]:

# numpy : 판다스 방식, n-1
np.var(ns_book7['대출건수'], ddof=1) #  371.69563042906674


# ### 표준 편차 구하기

# In[43]:
 
ns_book7['대출건수'].std() # 19.279409493785508 # pandas
np.std(ns_book7['대출건수']) # 19.27938390865096 # numpy


# ### 최빈값 구하기

# In[44]:
# pandas 가 numpy 기반으로 만들어졌기 떄문에 결과값 동일
# unique() 고유한 값을 추출
#  return_counts=True 등장 횟수 추출
values, counts = np.unique(ns_book7['도서명'], return_counts=True)
max_idx = np.argmax(counts) # 등장 횟수가 가장 많은 값
values[max_idx] # '승정원일기'


# ## 확인문제

# #### 4. 241에서 만든 ns_book7 df에서 평균 대출건수가 
# 가장 높은 10개의 출판사를 추출하는 명령을 완성하라

# In[45]:

# 내림차순 False=ascending # True 면, 오름차순  # 대출건수를 정열을 하되 조건으로 내림차순으로 정열해라.
ns_book7[['출판사','대출건수']].groupby('출판사').mean().sort_values('대출건수', ascending=False).head(10)

# #### 5. 25%, 75% 경계에 해당하는 대출건수를 찾아 이 범위에 속한 전체 도서 중 몇 퍼센트를 차지하는지 
# 구하는 명령이다. 빈칸 채워 명령을 완성하라
# ns_book7 df의 대출건수 열에서 quantile() 매서드를 호출

# In[46]:
print(len(ns_book7)) # 376770

target_range = np.array(ns_book7['대출건수'].quantile(q=[0.25,0.75])) # 2,14
target_bool_idx = (ns_book7['대출건수'] >= target_range[0]) & (ns_book7['대출건수'] <= target_range[1])
# target_bool 구간사이값에 만족하는 값들 즉 True의 개수/총개수 X 100(백분율)
target_bool_idx.sum()/len(ns_book7)*100
# 51.51737134060568