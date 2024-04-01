#!/usr/bin/env python
# coding: utf-8

# # 04-2 분포 요약하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/04-2.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/04-2.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 산점도 그리기

# In[1]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', './data/ns_book7.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book7 = pd.read_csv('./data/ns_book7.csv', low_memory=False)
ns_book7.head()


# In[3]:
# matplotlib
# pip install matplotlib
# 산점도
import matplotlib.pyplot as plt
# 데이터가 흩어진 정도 scatter() 매개변수 4개 포인트가 x축 좌표를 전달하고 두 번쨰
# 매개변수에 y축 좌표를 전달한다. show()함수를 호출하여 그래프 출력
plt.scatter([1,2,3,4], [1,2,3,4])
plt.show()


# In[4]:


plt.scatter(ns_book7['번호'], ns_book7['대출건수'])
plt.show()

#%%

plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'])
plt.show()


# In[6]:
# alpha: 투명도
# alpha=0.1 투명도 지정 0에 가까울 수록 투명하고 1에 가까울수록 불투명하게 그려짐.

plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()


# In[7]:
# 양의 상관관계: x축이 증가함에 따라 y축도 증가
# 도서권수 당 대출권수가 증가함에 따라 대출건수도 증가한다.
# 도서권수가 적을 수록 대출건수가 많다는 것은 음의 상관관계를 가진다. 
average_borrows = ns_book7['대출건수']/ns_book7['도서권수'] # 도서권수 당 대출건수 
# ns_book7['대출건수'] -> 대출건수
plt.scatter(average_borrows, ns_book7['대출건수'], alpha=0.1)


plt.show()


# ## 히스토그램 그리기
# 데이터의 분포
# 구간(bin) : 계급, bins 옵션
# 도수 : 데이터의 갯수
# In[8]:

# hist() 히스토그램(기본적으로 데이터를 10개의 구간으로 나눔)
# bins() 5로 지정하면 5개의 구간으로 나누어 그린다는 의미
# 즉 total 13 / 5 = 2.6 마다 구간이 나누어짐. 
plt.hist([0,3,5,6,7,7,9,13], bins=5)
plt.show()


# In[9]:


import numpy as np
# numpy를 활용하면 범위의 구간 별 값의 배열을 얻을 수 있음 .
np.histogram_bin_edges([0,3,5,6,7,7,9,13], bins=5)
#  array([ 0. ,  2.6,  5.2,  7.8, 10.4, 13. ])

# In[10]:
# 표준정규분포(standard normal distribution)
# 종 모양처럼 가운데가 볼록하고 평균을 중심으로 대칭인 분포를 정규분포
# 평균이 0이고 표준편차가 1인 정규분포
# randn()는 표준정규분포를 따르는 랜덤한 실수를 생성가능
# 이 함수에 원하는 샘플개수를 전달하여 난수(random number)얻을 수 있음
# seed()를 활용하면 유사난수(pseudorandom number)를 생성
# 즉 가짜 난수를 생성가능. 

# 요약하면, 정규분포는 평균과 표준편차를 가지는 일반적인 확률 분포를 의미하며, 
#표준 정규분포는 평균이 0이고 표준편차가 1인 특별한 경우의 정규분포를 나타냅니다.
#표준 정규분포는 데이터를 표준화하고 통계적 분석을 수행하는 데 사용됩니다.

np.random.seed(42)
random_samples = np.random.randn(1000) # 1000개의 난수


# In[11]:


print(np.mean(random_samples), np.std(random_samples))
# 0.04574194164571039 1.0330105359150537

# In[12]:

# 위의 실행 결과를 보면 평균값이 약 0.05, 표준편차 1.0으로 정규분포의 형태를 띈다. 
plt.hist(random_samples)
plt.show() 


# In[13]:


plt.hist(ns_book7['대출건수'])
plt.show()


# In[14]:

# 구간 조정 : log scale
# y 축에 로그함수를 적용한다는 의미 
# 크기 조정: 로그 함수를 사용하면 데이터의 범위를 조정할 수 있습니다.
# 특히, 데이터가 너무 크거나 작을 때 로그 변환을 통해 데이터의 크기를 조절하여 분석하기 편리해집니다.
# 이러한 장점들로 인해 로그 함수는 데이터 전처리, 특히 데이터 변환과정에서 널리 사용됩니다.
plt.hist(ns_book7['대출건수'])
plt.yscale('log')
plt.show()


# In[15]:

# yscale()구지 지정하지 안아도 log=True를 통해 y축을 축소할 수 있다. 
plt.hist(ns_book7['대출건수'], log=True)
plt.show()


# In[16]:

# hist()의 기본값은 bins = 10 이지만 구간을 100개로 나누게 되면 데이터 분포를 세밀하게 관찰가능
# 대출건수 : 0이 가장 많다. 
plt.hist(ns_book7['대출건수'], bins=100)
plt.yscale('log')
plt.show()


# In[17]:

# apply()를 활용하면 함수를 parameter로 지정할 수 있다.
# 도서명의 길이를 x값으로 본다는 의미로 y값(빈도수)은 해당 길이에 속하는 책의 권수이다
# 100개의 구간으로 쪼개는 히스토그램이다. 
title_len = ns_book7['도서명'].apply(len)
plt.hist(title_len, bins=100)
plt.show()


# In[18]:

# xscale() 를 활용하면 x축에 데이터가 골고루 그려지도록 바꿀 수 있다
# x축을 따라 작은 값과 큰 값의 차이가 줄어든다. 
plt.hist(title_len, bins=100)
plt.xscale('log')
plt.show()


# ## 상자 수염 그림 그리기

# In[19]:


temp = ns_book7[['대출건수','도서권수']]


# In[20]:

# boxplot() 이 함수에 다음처럼 한 개 이상의 df을 전달하여 그래프를 그린 것.
plt.boxplot(temp)
plt.show()


# In[21]:
# 1번 : 대출건수
# 2번 : 도서권수
plt.boxplot(ns_book7[['대출건수','도서권수']])
plt.yscale('log')
plt.show()


# In[22]:
# 로그 스케일 적용
# vert=False: 수평 그리기
# vert=True가 기본값으로 x-y축이 바뀌므로 로그 스케일도 x축에 지정해주어야 함. 
plt.boxplot(ns_book7[['대출건수','도서권수']], vert=False)
plt.xscale('log')
plt.show()


# In[23]:
# IQR(interquartile range) 
# 제 1사분면(25%)와 제3사분면(75%)사이의 거리 즉 box안 구간
# box구간안에 수평선은 중간값 즉 50%에 해당하는 지점임.
# 수염길이 조정 : 기본값 whis = 1.5
# 그래프의 이상치는 방울로 표현되며 1.5배 밖의 데이터를 의미하며 데이터 양이
# 많을 수록 영향이 줄기 때문에 반드시 제거해야 하는 것은 아니다.
plt.boxplot(ns_book7[['대출건수','도서권수']], whis=10)
plt.yscale('log')
plt.show()


# In[24]:

# 수염을 백분율로 지정
# whis=(0,100) : 0%~100% 수염으로 마지막 데이터까지 수염으로 그릴 수 있다.
plt.boxplot(ns_book7[['대출건수','도서권수']], whis=(0,100))
plt.yscale('log')
plt.show()


# ## 판다스의 그래프 함수

# ### 산점도 그리기

# In[25]:


ns_book7.plot.scatter('도서권수', '대출건수', alpha=0.1)
plt.show()


# ### 히스토그램 그리기

# In[26]:


ns_book7['도서명'].apply(len).plot.hist(bins=100)
plt.show()


# In[27]:


ns_book7['도서명'].apply(len).plot.hist(bins=100)
plt.show()


# ### 상자 수염 그림 그리기

# In[28]:


ns_book7[['대출건수','도서권수']].boxplot()
plt.yscale('log')
plt.show()


# ## 확인문제


# ns_book7 남산도서관 대출 데이터에서 1980~2022년 사이에 발행된 도서를 선택하여 
# 다음과 같은 발행년도의 히스토그램을 그려라.
selected_rows = (1980 <= ns_book7['발행년도']) & (ns_book7['발행년도'] <= 2022)
plt.hist(ns_book7.loc[selected_rows, '발행년도'])
plt.show()

# 위에서 선택한 도서로 '발행년도'열의 상자수염그림을 그려보시오
plt.boxplot(ns_book7.loc[selected_rows, '발행년도'])
plt.show()

