# -*- coding: utf-8 -*-
'''
Created on Wed Apr  3 15:31:46 2024

@author: Shin
'''

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
'''
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
'''


#%%


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
# 50건 : 11.53212
# 60건 : 11.511583333333332
# In[16]:

# 샘플(40)의 평균의 표준편차
np.std(sample_means) #  3.0355987564235165


# In[17]:
# 표준오차(Standard Error)
# 모집단의 평균은 알 수 없고  표본의 평균에 대한 z점수 공식:
# z = (14.75 - 모집단의 평균) / (표본평균의 표준편차)
# 표본 평균의 표준편차 = 모집단의 표준편차 / 제곱근(표본에 포합된 샘플개수)
np.std(ns_book7['대출건수']) / np.sqrt(40) # 3.048338251806833
print(np.std(ns_book7['대출건수'])) # 19.27938390865096
print(np.sqrt(40)) # 6.324555320336759

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
# 가설검정 hypothesis test p397/ 순열검정 permutaiton test p 402
# 귀무가설 또는 영가설(null hypothesis)
#이가 없거나 의미있는 차이가 없는 경우의 가설이며 이것이 맞거나 맞지 
#않다는 통계학적 증거를 통해 증명하려는 가설이다.
#   -표본 사이에 통계적으로 의미가 없다고 예상되는 가설
#   -H0  
#   -도서 : 파이썬과 C++도서의 평균 대출건수가 같다.
# 대립가설 alternative hypothesis
#   -Ha 
#   -가설: 파이썬과 C++도서의 평균 대출건수가 같지않다.
#   - 
# 유의수준(Significance level)
#   - 0.05(5%), 0.01(1%)
#   - 일반적으로 많이 사용하는 기준은 정규분포의 양쪽 꼬리 면적의 더해 5%가 되는 지점이다
#   - p-value가 0.05% 미만일 떄 영가설 기각되고 대안적으로 참이 되는 가설이 대립가설 
#   - z-score에 대한 기준을 유의수준이다.
# 유의확률(Significance Porbability, p-value)
#   -귀무가설(H0)과 대립가설(Ha) 설정
#   -적절한 통계량 선택 : z-통계량, t-통계량
#   -p-value 계산


# 두 모집단의 평균에 대한 z-score(표준점수: 정규분포 상에서 데이터 포인트가 
# 원점에서부터 얼마나 떨어져 있는지 표준편차의 비율을 나타내는 비율)
# z = ((x1-x2) - (u1-u2)) / sqrt((s2**2/n1) + (s2**2/n2)) 
# x1 : 파이썬의 표본의 평균 / x2 : c++의 표본의 평균
# u1 : 파이썬의 모집단의 평균 / u2 : c++의 모집단의 평균
# s1 : 파이썬 표본의 표준편차(표준오차) / s2 : c++의 표본의 표준편차(표준오차) 
# n1 : 파이썬 표본의 개수 / n2 : c++ 표본의 개수 

# 표준오차(Standard Error)
# 평균의 추정치에 대한 불확실도를 수치화한것
# 표본의 평균이 얼마나 모평균에 가까운지 나타내는 지표
# 표본평균의 오차(error of sanple mean)는 모평균을 기준으로하는 표본평균의 편차입니다. 
#   -공식 : 표본의 표준편차 = 모집단의 표준편차 / 제곱근(표본에 포함된 샘플갯수)
#   -표본의 표준편차와 모집단의 표준편차가 거의 동일(비슷)

# random sample을 모집단에서 뽑아 random sample의 평균은 알 수 없기에 모집단의 표준편차를 빌려와 
# 비슷하다고 가정하에 평균을 추정한다.
# random sample 이 x1~x5까지 있고 이 값들의 합이 100이라고 가정하자 여기서 
# random sample의 각각의 값을 모르는 상태에서 x1~x5의 값이 100이 넘지않게 설정하려고 
# 5개의 x(random sample)값 중 4개는 자유로운 반면에 하나의 x값은 100을 맞춰주기 위해 존재하므로 
# 자유롭지 못하다 이 경우 자유도는 4가 된다 
# 따라서 표본평균의 표준편차를 구할 떄 sample의 개수보다 1개 적은 sample-1로 나누어 표본의 표준편차를 구한다



# 우리의 목표는 수집한 표본 데이터를 바탕으로 귀무가설의 유의성(즉, 옮은지/옮다고 볼 수 없는지)
# 검정을 하는 것이다.귀무가설이 참이면 통계적으로 유의하지 않음을 의미하고 거짓


#%%
# regex=False 이유: 
#str.contains 매서드가 정규 표현식을 사용하여 패턴 매칭을 수행하는 것이 기본 동작이기 때문입니다.
# 그러나 이 경우에는 정규 표현식이 필요하지 않으며, 단순히 문자열이
# 다른 문자열에 포함되어 있는지 확인하면 되므로 regex=False를 사용
cplus_books_index = ns_book7['주제분류번호'].str.startswith('00') & \
                    ns_book7['도서명'].str.contains('C++', regex=False)
cplus_books = ns_book7[cplus_books_index]
cplus_books.head()


# In[26]:

python_mean = np.mean(python_books['대출건수'])
python_mean # 14.749003984063744
len(cplus_books) # 89
 

# In[27]:
import numpy as np
# 표본의 평균 : c++
cplus_mean = np.mean(cplus_books['대출건수'])
cplus_mean # 11.595505617977528


# In[28]:

# 표준오차(Standard-Error)
cplus_se = np.std(cplus_books['대출건수'])/ np.sqrt(len(cplus_books))
cplus_se # 0.9748405650607009


# In[29]:
# python_mean : 14.749003984063744
# cplus_mean : 11.595505617977528
# python_se : 0.8041612072427442
# cplus_se : 0.9748405650607009

# z-score : 
pc_z_score = (python_mean - cplus_mean) / np.sqrt(python_se**2 + cplus_se**2)
pc_z_score = round(pc_z_score, 2)
print(pc_z_score) # 2.5

# In[30]:
# 누적부포 : 0.9937903346742238
from scipy import stats

# stats.norm.cdf(2.50) # 0.9937903346742238
pc_norm_cdf = stats.norm.cdf(pc_z_score)
pc_norm_cdf = round(pc_norm_cdf, 3)
print(pc_norm_cdf) # 0.994

# In[31]:


p_value = (1-0.995)*2
p_value # 0.010000000000000009
#%%
p_value = (1-pc_norm_cdf) * 2
p_value # 0.01200000000000001
#%%
# 결과 : 영가설을 기각한다 : 파이썬과 c++도서의 평균에 차이가 있다. 
# True = p_value(0.012) < p_level(0.05)
p_level = 0.05
p_tf = p_value < p_level
print(p_tf) # True

# In[32]:
# t 검정으로 가설 검증하기 ttest_ind() 
# t분포인 두 표본을 비교하는 t-검정을 수행 t분포는 정규분포와 비슷하지만
# 중앙은 조금 더 낮고 꼬리가 두꺼운 분포임. # 표본의 크기가 30이하일 떄 t-분포
# 사용하는 것이 좋음.

## 이 함수를 사용하여 표본크기에 상관 없이 평균을 비교할 수 있음.##

# 앞에서 구한 파이썬/ c++ 도서의 데이터를 ttest_ind에 넣어주면 t점수와 p-값을 반환

t, pvalue = stats.ttest_ind(python_books['대출건수'], cplus_books['대출건수'])
print(t, pvalue) # 2.1390005694958574 0.03315179520224784
# 0.03315179520224784 p값
t_value = 0.03315179520224784
t_tf2 =  t_value < p_level
print(t_tf2) # True
# 따라서 영가설을 기각하며 두 도서의 대출건수의 평균 차이는 우연이 아님.

# 위의 모든 과정은 모집단의 평균이 정규분포를 따른다는 가정하에 진행되었다.

# (모집단의 파라미터(평균,분산)을 추정x -> 비모수검정 nonparametric-test)
# 만약 정규분포가 아닐 때 가설 검증하기: 순열검정
# 모집단의 분포가 정규분포가 아니거나 모집단의 분포를 알 수 없을 떄 
# 두 그룹에서 다시 평균의 차이를 계산한다
# 위 과정을 여러번 반복
# 원래 표본의 평균 차이가 무작위로 나눈 그룹의 평균 차이보다 
# 크거나 작은 경우를 헤아려서 p-값을 계산
# In[33]:

# 먼저 두 배열을 받아 평균을 구하는 statistic 함수생성
def statistic(x, y):
    return np.mean(x) - np.mean(y)


# In[34]:

# 순열검정 실행 함수: 
# 두 배열을 numpy.append()로 합친 후 무작위로 추출하기 위해 permutation활용
# 두 그룹은 원래 표본의 크기와 동일하게 만듬.(두그룹의 표본개수 = 모집단 표본개수) 
# 무작위로 섞인 배열을 만들고 여기에 전체 배열 길이만큼 랜덤한 인덱스 생성
# 인덱스로 x_, y_로 두 그룹을 나눈 후 그룹사이의 평균차이를 계산
# 이런식으로 1000번 반복

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
print(['대출건수'])
print(python_books['대출건수']) # 251
print(cplus_books['대출건수']) # 89
# 모집단 전체 대출건수가 되며 표본의 대상은 python이 제목에 포함된 도서였다
# 이 떄 표본평균 즉, 파이썬이 들어가 도서의 평균 대출건수는 np.mean()로 계산된다
#def statistic(x, y):
#   return np.mean(x) - np.mean(y)
# 위에서 두 value x,y에 대하여 평균을 구하는 함수를 생성했었다.
# obs_diff = statistic(x,y) 정의했었다. 이는 두 표본평균의 차이를 말한다 

np.mean(ns_book7['대출건수']) # 11.593438968070707 # 모집단의 평균 대출건수
np.mean(python_books['대출건수'])  # 14.749003984063744 # python도서 평균 대출건수
np.mean(cplus_books['대출건수']) # 11.595505617977528 # C++도서 평균 대출건수



pm_test = permutation_test(python_books['대출건수'], cplus_books['대출건수'])
print(pm_test) # (3.1534983660862164, 0.022)

# 두 그룹의 평균의 차이 : 3.1534983660862164
# p-value :  0.022

# 결과   p-value(0.022) < 0.05 보다 작음
# 유의수준에 미치지 않으므로 영가설을 기각한다
# 두 도서의 평균 대출건수에는 차이가 있음을 알 수 있음.  

# In[36]:


# scipy 1.8 버전 이상에서만 실행됩니다.
res = stats.permutation_test((python_books['대출건수'], cplus_books['대출건수']), 
                              statistic, random_state=42)
p_value = 0.0258
# 결과는 약 3.153 0.0258입니다.
print(res.statistic, res.pvalue) # 3.1534983660862164 0.0258

res1 = stats.permutation_test((python_books['대출건수'], cplus_books['대출건수']), 
                              lambda x, y : np.mean(x) - np.mean(y), random_state=42)
'''
random_state:

주로 머신러닝 라이브러리인 scikit-learn에서 사용됩니다.
scikit-learn의 대부분의 모델은 random_state 매개변수를 가지고 있습니다
'''
# In[36]:

#['주제분류번호'].str.startswith('00') 는 주제분류번호가 00 으로 시작한다는 조건
java_books_indx = ns_book7['주제분류번호'].str.startswith('00') & \
                  ns_book7['도서명'].str.contains('자바스크립트')
java_books = ns_book7[java_books_indx]
java_books.head()


# In[37]:
# 파이썬 평균 대출건수 : python_mean = np.mean(python_books['대출건수'])
python_mean # 14.749003984063744
# 105권중 java 평균 대출건수 : 
print(len(java_books), np.mean(java_books['대출건수'])) # 105 15.533333333333333


# In[38]:


permutation_test(python_books['대출건수'], java_books['대출건수']) # (-0.7843293492695889, 0.566)
# 결과
# p_value(0.566)는 0.05보다 크다
p_value = 0.566
p_value < 0.5
print(p_value)
# 영가설을 기각할 수 없다 
