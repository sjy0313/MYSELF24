#!/usr/bin/env python
# coding: utf-8

# # 07-2 머신러닝으로 예측하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/07-2.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/07-2.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>


# 파이썬은 (공부+모델만드는 과정에 특화)
# 시스템 구축 및 서비스화를 하려면(tensor-flow 같은 framework 또는 C,C++을 활용이 필요하다)


# ## 모델 훈련하기 
# pip install scikit-learn
# model : 학습된 패턴을 저장하는 소프트웨어 객체(scikit-learn에서 어떤 클래스의 인스턴스가 객체)
# 만들어논 결과(알고리즘) -> 레시피 
# 지도학습(supervised learning) : 데이터의 각 샘플에 대한 정답(target)을 알고 있는 경우
# 재료(밀가루, 설탕)로 만든 빵(target) -> 여러가지 결과물이 될 수 있음. 
# input : 입력은 target을 맞추기 위해 모델이 재료로 사용하는 데이터
# 비지도학습(un-supervised learning) : 입력 데이터는 있지만 타깃이 없는 경우
# 대표적으로 군집 알고리즘(clustering algorithm)이 있다. 
# 모델을 훈련한다는 것은 지속적으로 샘플을 제공하여 정답에 가까운 답을 내기위해 훈련시키는 것.
# In[1]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', './data/ns_book7.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book7 = pd.read_csv('./data/ns_book7.csv', low_memory=False)
ns_book7.head()


# In[3]:
# 즉, 머신러닝은 입력값을 지원하면 모델을 활용하여 코딩을 자동으로 하여 결과값을 도출해준다.
# 핵심은 sample data가 모집단을 잘 설명해주냐를 찾는 것임.

# 파이썬의 대표적인 머신러닝 패키지는 scikit-learn 으로 머신러닝 모델을 만들 수 있다.
#아주 많은 경우의 수 중에 하나를 복잡한 알고리즘을 거쳐 선정하여 기능적으로 
'''
난수와 같도록 만든 결과 값이라고 하는 편이 정확합니다.
모델을 훈련시키거나, 샘플을 추출하거나, 표본에 셔플을 적용할 때 '무작위'라는 
원칙을 적용하는 것은 중요합니다. 하지만 '재현 가능성'을 염두에 둘 경우 '무작위'는 
완전한 재현을 어렵게 만드는 요소일 수도 있습니다.
'''
from sklearn.model_selection import train_test_split
# 훈련세트 : 75% train_test
# 테스트세트 : 25% test_set

train_set, test_set = train_test_split(ns_book7, random_state=42) # random seed


# In[4]:
ns_book7_len = len(ns_book7) # 376770
train_set_len = len(train_set) # 282577
test_set_len = len(test_set) # 94193
print('ns_book7_len : ', ns_book7_len) # 376770
print('train_set_len :', train_set_len, round(train_set_len / ns_book7_len, 2)) # 282577 0.75
# train_set_len : 282577 0.75
print('test_set_len : ', test_set_len, round(test_set_len / ns_book7_len, 2)) # 94193 0.25
# test_set_len :  94193 0.25 
print(len(train_set), len(test_set)) # 282577 94193

# 각 데이터 셋의 대출건수의 평균
ns_book7['대출건수'].mean() # 11.593438968070707
train_set['대출건수'].mean() #  11.598732380908567
ns_book7['대출건수'].mean() # 11.593438968070707

# In[5]:
# '도서권수'열을 사용해  '대출건수' 예측 : 
# 데이터 셋-> 머신러닝
# 사이킷 런 자체가 훈련데이터로 2차원 입력값 요함.
X_train = train_set[['도서권수']] # X는 입력 데이터 (데이터프레임 2차원 배열)
y_train = train_set['대출건수'] # (타깃)정답 : 시리즈(1차원)

print(X_train.shape, y_train.shape) # (282577, 1) (282577,)
# 2차원 배열인 입력은 행 방향 샘플이 나열/ 열 방향 샘플의 속성 나열


# In[6]:
# 선형회귀모델(함수생성) 알고리즘 -> 입력값을 넣을 수 있는 공식을 세워주는 것.
# 선형회귀모델 : LinearRegression 
from sklearn.linear_model import LinearRegression
# 선형회귀모델 생성
lr = LinearRegression()
# 훈련
lr.fit(X_train, y_train) 


# ## 훈련된 모델을 평가하기: 결정계수

# In[7]:
# 평가 : score()
#  결정계수가 1에 가까우면 정답(target)을 맞출 확율이 높아진다
# 즉 도서권수와 대출건수에 관계가 깊다고 볼 수 있다.
X_test = test_set[['도서권수']] # 입력
y_test = test_set['대출건수'] # 정답
# 결정계수(Coefficient of Determination)
# R**2 = 1 - (target - 예측)**2 / (target - 평균)**2
r2 = lr.score(X_test, y_test) 
print("결정계수(r2): ", r2) # 결정계수(r2):  0.10025676249337057
# 결과 : 0.1은 좋은 점수가 아니다
# 평균은 타깃의 평균을 의미한다
# 예측이 평균에 가까워지면 분모와 분자가 같아져 R**2점수는 0이 된다

#R²는 0부터 1사이의 값을 갖습니다.0에 가까울수록 설명변수 X와 반응변수
#Y는 선형 상관관계의 정도가 없다고 하고,1에 가까울수록 선형 상관관계의 정도가 크다고 할 수 있습니다.

# 기울기 : 12.87648822
# 절편 : -3.1455454195820653
print(lr.coef_, lr.intercept_) # [12.87648822] -3.1455454195820653
# In[8]:
# 대출건수(y-train)로 대출건수를 훈련하여 예측 : 
# 즉 정답 데이터로 훈련을 수행
# 결과 : 결정계수 1.0
X_train2 = train_set[['도서권수']] # X는 입력 데이터 (데이터프레임 2차원 배열)
y_train2 = train_set['대출건수'] # target

# 선형회귀모델 생성 (인스턴스 생성)
lr2 = LinearRegression()

# y_train은 시리즈 객체이므로 2차원 배열 형태로 변환
X_train2 = y_train.to_frame() # 대출건수 : 훈련 데이터
y_test2 = y_test.to_frame() # 대출건수 : 테스트 데이터 
# 훈련
#lr2.fit(y_train.to_frame(), y_train) 
#lr2.score(y_test.to_frame(), y_test) # 1.0
lr2.fit(X_train2, y_train) 
lr2.score(y_test2, y_test) # 1.0
# ## 연속적인 값 예측하기: 선형 회귀

# In[9]:
# 기울기 : 1.0
# 절편 : -1.2647660696529783e-12

print(lr.coef_, lr.intercept_)





# ## 평균제곱오차와 평균절댓값오차로 모델 평가하기

# In[14]:


lr.fit(X_train, y_train)


# In[15]:

# 예측 : 검증데이터로 '대출건수' 예측
y_pred = lr.predict(X_test)

#%%
# 평균절댓값오차 : MAE
# MAE = 합(절대값(타깃-예측)) / n

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
print(mae) # 10.358091752853873
# 결과가 타깃의 평균 정도의 오차가 발생

# In[17]:

# 타깃의 평균
y_test.mean() # 11.577558841952163
# 모집단(전체)의 '대출건수'의 평균을 구함
ns_book7['대출건수'].mean() # 11.593438968070707
#%%

import matplotlib.pyplot as plt

# 01 : 지정된 폴더에서 설치된 폰트 꺼내서 matplotlip 그래프에 적용
import matplotlib.font_manager as fm
# font_files = fm.findSystemFonts(fontpaths=['C:/Windows/Fonts'])
font_files = fm.findSystemFonts(fontpaths=['C:/Users/Shin/AppData/Local/Microsoft/Windows/Fonts'])
for fpath in font_files:
        print(fpath)
        fm.fontManager.addfont(fpath)
plt.rcParams['font.family'] = 'NanumBarunGothic'

# 산점도
fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(ns_book7['도서권수'], ns_book7['대출건수'])
ax.set_title("도서권수 대비 대출건수")
ax.set_xlabel("도서권수")
ax.set_ylabel("대출권수")
fig.show()






















