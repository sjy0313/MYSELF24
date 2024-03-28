#!/usr/bin/env python
# coding: utf-8

# # 07-1 통계적으로 추론하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/07-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/07-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 표준 점수 구하기

# In[1]:


import numpy as np

x = [0, 3, 5, 7, 10]

s = np.std(x)
m = np.mean(x)
z = (7 - m) / s
print(z)


# In[2]:


from scipy import stats

stats.zscore(x)


# In[3]:


stats.norm.cdf(0)


# In[4]:


stats.norm.cdf(1.0) - stats.norm.cdf(-1.0)


# In[5]:


stats.norm.cdf(2.0) - stats.norm.cdf(-2.0)


# In[6]:


stats.norm.ppf(0.9)


# ## 중심극한정리 알아보기

# In[7]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)


# In[8]:


import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()


# In[9]:


import matplotlib.pyplot as plt

plt.hist(ns_book7['대출건수'], bins=50)
plt.yscale('log')
plt.show()


# In[10]:


np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(30).mean()
    sample_means.append(m)


# In[11]:


plt.hist(sample_means, bins=30)
plt.show()


# In[12]:


np.mean(sample_means)


# In[13]:


ns_book7['대출건수'].mean()


# In[14]:


np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(20).mean()
    sample_means.append(m)
np.mean(sample_means)


# In[15]:


np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(40).mean()
    sample_means.append(m)
np.mean(sample_means)


# In[16]:


np.std(sample_means)


# In[17]:


np.std(ns_book7['대출건수']) / np.sqrt(40)


# ## 모집단의 평균 범위 추정하기: 신뢰구간

# In[18]:


python_books_index = ns_book7['주제분류번호'].str.startswith('00') & \
                     ns_book7['도서명'].str.contains('파이썬')
python_books = ns_book7[python_books_index]
python_books.head()


# In[19]:


len(python_books)


# In[20]:


python_mean = np.mean(python_books['대출건수'])
python_mean


# In[21]:


python_std = np.std(python_books['대출건수'])
python_se = python_std / np.sqrt(len(python_books))
python_se


# In[22]:


stats.norm.ppf(0.975)


# In[23]:


stats.norm.ppf(0.025)


# In[24]:


print(python_mean-1.96*python_se, python_mean+1.96*python_se)


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

