# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:31:46 2024

@author: Shin
"""

# ## 중심극한정리 알아보기
# "무작위로 샘플을 뽑아 만든 표본의 평균은 정규분포에 가깝다"
# 표준정규분포를 따르지 않는 데이터는?
# 정규분포 특성을 유도하는 방법으로 중심극한정리를 사용한다
# 무작위로 모집단에서 뽑은 sample(표본)의 평균을 구하는 과정을 여러번 반복해서 
# 평균을 구하여 이 평균들의 값들을 히스토그램에 옮겨 놓으면 정규분포를 따른다
# 히스토그램
# 히스토그램은 데이터 분포를 시각적으로 나타내기 위한 중요 도구입니다. 
# 이 차트는 대량의 데이터를 요약하고 값의 빈도를 나타냅니다. 
#따라서 데이터 분포 추세와 중앙값을 결정하는데 도움이 됩니다. 
#또한 데이터의 간격과 특이치를 강조하는 데에도 효과적입니다.

#%%
"""
모분산 (Population Variance):

모분산은 모집단의 분산을 나타냅니다. 모집단이란 분석하고자 하는 전체 집단을 의미합니다.
모분산은 모든 개별 데이터 포인트와 모평균 간의 편차의 제곱의 평균으로 계산됩니다.
모분산은 모집단의 특성을 설명하기 위해 사용됩니다. 하지만, 모집단 전체를 조사하는 것은 현실적
으로 불가능할 수 있습니다.
표본분산 (Sample Variance):

표본분산은 표본 데이터 집합의 분산을 나타냅니다. 표본은 모집단에서 추출된 부분 집합을 의미합니다.
표본분산은 각 개별 데이터 포인트와 표본평균 간의 편차의 제곱의 평균으로 계산됩니다.
표본분산은 모집단의 특성을 추정하기 위해 사용됩니다. 모집단의 모분산과 유사하지만, 
표본에서 계산되었기 때문에 모집단의 실제 분산과 정확히 일치하지 않을 수 있습니다.
표본분산은 통계적 추론 및 가설 검정에서 중요한 역할을 합니다.
따라서, 모분산은 모집단의 특성을 나타내고, 표본분산은 표본 데이터를 기반으로 
모집단의 특성을 추정하는 데 사용됩니다. 표본분산은 보다 현실적이고 실용적인 분석을 위해 
모집단의 특성을 추정하는 데 사용됩니다.
"""




# In[7]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', './data/ns_book7.csv', quiet=False)


# In[8]:


import pandas as pd

ns_book7 = pd.read_csv('./data/ns_book7.csv', low_memory=False)
ns_book7.head()


# In[9]:


import matplotlib.pyplot as plt
# 대출건수의 히스토그램
plt.hist(ns_book7['대출건수'], bins=50)
plt.yscale('log') # log scale 
plt.show()


# In[10]:
import numpy as np

np.random.seed(42) # 유사난수 생성을 위한 초깃값 지정 
# 1000번을 30건씩 샘플링하여 '대출건수'의 평균을 구함
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(30).mean()
    sample_means.append(m)


# In[11]:

 # 좌우 대칭이 완벽하지 않지만, 종모양과 유사한 분포 형성
plt.hist(sample_means, bins=30)
plt.show()


# In[12]:
# 매직넘버 : 30
#1000번을 30건씩 샘플링하여 '대출건수'의 평균을 구함
 # 샘플 데이터의 총 평균
np.mean(sample_means) # 11.539900000000001


# In[13]:


ns_book7['대출건수'].mean() # 11.593438968070707


# In[14]:

#1000번을 20건씩 샘플링하여 '대출건수'의 평균을 구함
np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(20).mean()
    sample_means.append(m)
np.mean(sample_means)
# 모집단(전체)의 '대출건수'의 평균(11.5934)로부터 더 가까워짐.
np.mean(sample_means)  #  11.39945
#%%
#1000번을 50건씩 샘플링하여 '대출건수'의 평균을 구함
np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(50).mean()
    sample_means.append(m)
np.mean(sample_means) # 11.53212
#%%
#1000번을 60건씩 샘플링하여 '대출건수'의 평균을 구함
np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(60).mean()
    sample_means.append(m)
np.mean(sample_means) # 11.511583333333332
#%%
#1000번을 40건씩 샘플링하여 '대출건수'의 평균을 구함
np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(40).mean()
    sample_means.append(m)
np.mean(sample_means) # 11.5613
#%%
# ns_book7 모집단
# 샘플의 갯수에 따른 평균값
# 전체 : 11.593438968070707
# 20건 : 11.39945
# 30건 : 11.539900000000001
# 40건 : 11.5613 # 40건이 전체에 가장 가까움
# 50건 : 
# 60건 : 11.511583333333332
# In[16]:

# 샘플(40)의 평균의 표준편차
np.std(sample_means) #  3.0355987564235165


# In[17]:
# 표준오차(Standard Error)
# 표본 평균의 표준편차 = 모집단의 표준편차 / 제곱근(표본에 포합된 샘플개수)
np.std(ns_book7['대출건수']) / np.sqrt(40) # 3.048338251806833

# 신뢰구간(Confidence Interval)
# ## 모집단의 평균 범위 추정하기: 신뢰구간
# 전제조건: 
# 만약 딱 하나의 표본이 있다면 모집단의 평균을 추정할 수 있는가? 
# 신뢰구간은 표본의 파라미터(평균)가 속할 것이라 믿는 모집단의 파라미터 범위이다 

# In[18]:
# '파이썬'도서의 대출건수를 사용해 신뢰구간을 계산
# 주제분류번호'의 앞의 문자가 00으로 시작하고 도서명이 파이썬을 포함하는 것.
python_books_index = ns_book7['주제분류번호'].str.startswith('00') & \
                     ns_book7['도서명'].str.contains('파이썬')
python_books = ns_book7[python_books_index]
python_books.head()

# In[19]:


len(python_books) #  251건


# In[20]:

# 파이썬 도서의 대출건수 평균
python_mean = np.mean(python_books['대출건수'])
python_mean # 14.749003984063744


# In[21]:

# 중심극한정리의 표준오차
# 표준오차(Standard Error)
# 표본 평균의 표준편차 = 표본의 표준편차 / 제곱근(표본에 포합된 샘플개수)
python_std = np.std(python_books['대출건수'])
python_se = python_std / np.sqrt(len(python_books))
python_se #  0.8041612072427442


# In[22]:
# 누적분포 z-score
from scipy import stats
# 0.975 = 1 - 0.025
# 평균을 중심으로 95%영역의 좌우 각각 2.5%구간
stats.norm.ppf(0.975) # 1.959963984540054


# In[23]:


stats.norm.ppf(0.025)


# In[24]:
    
# 파이썬 도서의 대출건수 평균
python_mean = np.mean(python_books['대출건수'])
python_mean # 14.749003984063744

# 모집단의 표준편차가 표본의 표준편차와 비슷하다고 가정한다
# 모집단의 표준편차 대신 표본이라고 할 수 있는 남산도서관의 파이썬 도서 대출건수로 
# 표준편차를 구한다음 표준오차를 구해보면  
# 중심극한정리의 표준오차( 표본평균의 표준평균)
python_se #  0.8041612072427442


# 모집단 평균('대출건수') : 11.593438968070707
# 표본의 평균 python_mean 값과 표준 오차 python_se를 바탕으로 모집단의 평균이

# 13.2에서 16.3사이에 놓여 있을 것이라고 95%확신
# 95%신뢰구간에서 파이썬 도서의 모집단 평균이 13.2에서 16.3사이에 놓여있다

# 모집단의 평균 추측 (표본 평균)
print(python_mean-1.96*python_se, python_mean+1.96*python_se)
# 13.172848017867965 16.325159950259522
# 13.2에서 16.3사이에 놓여 있다고 추측


# ## 통계적 의미 확인하기: 가설검정

# In[25]:


cplus_books_index = ns_book7['주제분류번호'].str.startswith('00') & \
                    ns_book7['도서명'].str.contains('C++', regex=False)
cplus_books = ns_book7[cplus_books_index]
cplus_books.head()


# In[26]:


len(cplus_books)


# In[27]:


cplus_mean = np.mean(cplus_books['대출건수'])
cplus_mean


# In[28]:


cplus_se = np.std(cplus_books['대출건수'])/ np.sqrt(len(cplus_books))
cplus_se


# In[29]:


(python_mean - cplus_mean) / np.sqrt(python_se**2 + cplus_se**2)


# In[30]:


stats.norm.cdf(2.50)


# In[31]:


p_value = (1-0.995)*2
p_value


# In[32]:


t, pvalue = stats.ttest_ind(python_books['대출건수'], cplus_books['대출건수'])
print(t, pvalue)


# ## 정규분포가 아닐 때 가설 검증하기: 순열검정

# In[33]:


def statistic(x, y):
    return np.mean(x) - np.mean(y)


# In[34]:


def permutation_test(x, y):
    # 표본의 평균 차이를 계산합니다.
    obs_diff = statistic(x, y)
    # 두 표본을 합칩니다.
    all = np.append(x, y)
    diffs = []
    np.random.seed(42)
    # 순열 검정을 1000번 반복합니다.
    for _ in range(1000):
        # 전체 인덱스를 섞습니다.
        idx = np.random.permutation(len(all))
        # 랜덤하게 두 그룹으로 나눈 다음 평균 차이를 계산합니다.
        x_ = all[idx[:len(x)]]
        y_ = all[idx[len(x):]]
        diffs.append(statistic(x_, y_))
    # 원본 표본보다 작거나 큰 경우의 p-값을 계산합니다.
    less_pvalue = np.sum(diffs < obs_diff)/1000
    greater_pvalue = np.sum(diffs > obs_diff)/1000
    # 둘 중 작은 p-값을 선택해 2를 곱하여 최종 p-값을 반환합니다.
    return obs_diff, np.minimum(less_pvalue, greater_pvalue) * 2


# In[35]:


permutation_test(python_books['대출건수'], cplus_books['대출건수'])


# In[36]:


# scipy 1.8 버전 이상에서만 실행됩니다.
# res = stats.permutation_test((python_books['대출건수'], cplus_books['대출건수']), 
#                              statistic, random_state=42)
# 결과는 약 3.153 0.0258입니다.
# print(res.statistic, res.pvalue)


# In[36]:


java_books_indx = ns_book7['주제분류번호'].str.startswith('00') & \
                  ns_book7['도서명'].str.contains('자바스크립트')
java_books = ns_book7[java_books_indx]
java_books.head()


# In[37]:


print(len(java_books), np.mean(java_books['대출건수']))


# In[38]:


permutation_test(python_books['대출건수'], java_books['대출건수'])
