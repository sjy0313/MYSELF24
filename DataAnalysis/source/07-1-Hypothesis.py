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
# 모수검정(population)
# 통계학에서 모집단에 대한 파라미터(평균, 분산) 를 추정하는 방법
# 모집단은 관심 대상이 되는 데이터를 의미
# 모집단에서 선택한 일부 샘플 즉 표본을 조사한다음 다음 평균을 추정하는 것이 모수검정
# 모수검정은 모집단의 데이터에 대한 정규분포를 따른다는 가정을 전제로 하고 수행되는 경우가 많다
# 실제로 전체 데이터를 알지 못하지만 자연세계의 데이터는 정규분포를 따른다.
#%%
# [누적분포]
# 표준정규분포 평균이 0이고 표준편차가 1인 정규분포
# 평균이 0이고 표준편차가 1을 z점수 공식을 대입하면 z = x
# z점수를 사용해 전체 데이터가 어떻게 분포되어 있는지 표시

#%%
# 데이터는 정규분포를 따른다고 가정
# 각 값이 평균에서 얼마나 떨어져 있는지 표준편차를 사용해 변환한 점수를 표준점수
# 표준 점수(Standard score) -> z-score
# 표준 점수 클 수록 평균으로 부터 거리가 멀어진다.
# 표준정규분포에서 z점수가 1.0이내에 위치한 샘플은 전체의 68%에 해당
# 표준정규분포에서 z점수가 2.0이내에 위치한 샘플은 전체의 95%에 해당
from scipy import stats
# 누적분포를 구하는 파이썬 함수 stats.norm.cdf(z)
stats.norm.cdf(0) # 0.5 -> 50% 구간 평균
stats.norm.cdf(1.0) - stats.norm.cdf(-1.0) # 0.6826894921370859 -> 68%
stats.norm.cdf(2.0) - stats.norm.cdf(-2.0) # 0.9544997361036416 -> 95%
# 누적분포로 z-score 구하는 파이썬 함수:
stats.norm.cdf(0)

# In[1]:
# 표준점수 구하기

import numpy as np

x = [0, 3, 5, 7, 10]

s = np.std(x) # 표준편차
m = np.mean(x)# 평균
z = (7 - m) / s # 표준점수 모집단에서 고른 7 - mean / std = 0.5872202195147035
print(z) # 0.5872202195147035
#%%
print("표준편차: ",s) # 표준편차:  3.40587727318528
print("평균: ",m) # 평균:  5.0
#%%

zs = []
for n in x: 
    z = (n - m) / s
    zs.append.round(z, 8)

print(zs) # [-1.4680505487867588, -0.5872202195147035, 0.0, 0.5872202195147035, 1.4680505487867588]

# In[2]:

# 사이파이 활용
#conda activate YSIT24
#pip install scipy
from scipy import stats

stats.zscore(x) #  array([-1.46805055, -0.58722022,  0.        ,  0.58722022,  1.46805055])


# In[3]:

# 누적분포를 구하는 파이썬 함수 stats.norm.cdf(z)
stats.norm.cdf(0) # 0.5
 

# In[4]:

# 누적분포를 구하는 파이썬 함수 stats.norm.cdf(z)
stats.norm.cdf(1.0) - stats.norm.cdf(-1.0) # 0.6826894921370859 -> 68%


# In[5]:

# 누적분포를 구하는 파이썬 함수 stats.norm.cdf(z)
stats.norm.cdf(2.0) - stats.norm.cdf(-2.0)  # 0.9544997361036416 -> 95%


# In[6]:

# 누적분포로 z-score 구하는 파이썬 함수:
stats.norm.ppf(0.9) # 1.2815515655446004 
# 누적분포로 z-score 구하는 파이썬 함수:
stats.norm.ppf(0.95) # 1.6448536269514722
# 누적분포로 z-score 구하는 파이썬 함수:
stats.norm.ppf(0.68) # 0.4676987991145084


