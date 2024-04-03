#!/usr/bin/env python
# coding: utf-8

# # 05-1 맷플롯립 기본 요소 알아보기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/05-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/05-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## `Figure` 클래스

# In[1]:


# import gdown
# gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book7 = pd.read_csv('./data/ns_book7.csv', low_memory=False)
ns_book7.head()


# In[3]:


import matplotlib.pyplot as plt
# plt.show() colab에서는 따로 이 코드 실행하지 않아도 그래프 생성됨. 
# alpha=0.1 산점도의 투명도 지정
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
# scatter()함수활용하여 산점도 그릴 떄 figure 객체를 가짐
# figure 객체의 크기는 보통 그림의 폭과 높이를 인치(inches) 단위로 나타냅니다.
# 기본적으로 생성된 figure 객체는 6인치의 폭과 4인치의 높이를 갖습니다. 
# 이러한 크기는 필요에 따라 조절할 수 있습니다.
# In[4]:

# 기본 그래프의 크기 : 너비(width), 높이(height) 
# 인치(1인치): 2.54cm
print(plt.rcParams['figure.figsize']) # [6.0, 4.0] : 63.5pixel, 62
# figsize를 튜플로 지정가능

# In[5]:


plt.figure(figsize=(9, 6)) # 61pixel, 60
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()


# In[6]:


print(plt.rcParams['figure.dpi']) # 72 plt.show()함수가 호출되면 figure()함수로
# 만들어진 피겨 객체는 자동 소멸됨. 
# DPI(dot per inch) 인쇄물의 해상도 # 1인치를 몇 개의 점(pixel)으로 표현하는지 나타냄
# 27인치(1920 pixel) : 72
# PPI(pixel per inch) 화면 해상도

# In[7]:

dpi = plt.rcParams['figure.dpi']
print("DPI:", dpi)
plt.figure(figsize=(900/72, 600/72))
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()


# In[8]:

# bbox_inches': None 타이트 레이아웃을 사용하지 않으려면.(그래프 출력시 주변 공백을 최소화하는 레이아웃)
get_ipython().run_line_magic('config', "InlineBackend.print_figure_kwargs = {'bbox_inches': None}")
plt.figure(figsize=(900/72, 600/72))
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()


# In[9]:


get_ipython().run_line_magic('config', "InlineBackend.print_figure_kwargs = {'bbox_inches': 'tight'}")


# In[10]:
# plt.figure() 함수는 다양한 매개변수를 통해 그림의 크기나 기타 속성을 조절할 수 있습니다.
# dpi 매개변수를 활용하여 기본값인 72에서 144로 확대할 수 있음. 
plt.figure(dpi=144)
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()


# ## `rcParams` 객체
# 그래프의 기본값을 관리하는 객체 
# 객체에 담긴 값을 출력 + 새로운 값으로 바꿀 수도 있음.
# In[11]:


plt.rcParams['figure.dpi'] = 100


# In[12]:

# 데이터 포인트를 나타내는 마커
plt.rcParams['scatter.marker'] # 산점도 그래프의 마커 기본값 -> 'o'
 


# In[13]:


plt.rcParams['scatter.marker'] = '*' #marker 지정
plt.rcParams['scatter.marker'] = '^' 
'''
'.': 점(marker)
',': 픽셀(marker)
'o': 원(marker)
'v': 아래쪽 삼각형(marker)
'^': 위쪽 삼각형(marker)
'<': 왼쪽 삼각형(marker)
'>': 오른쪽 삼각형(marker)
's': 사각형(marker)
'p': 오각형(marker)
'P': 대각선 십자가(marker)
'*': 별(marker)
'h': 육각형(marker)
'H': 육각형(marker)
'+': 플러스(marker)
'x': 엑스(marker)
'D': 대각선 다이아몬드(marker)
'd': 작은 대각선 다이아몬드(marker)
'''

# In[14]:


plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()


# In[15]:


plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1, marker='+')
plt.show()


# ## 여러 개의 서브플롯 출력하기
# https://matplotlib.org/stable/api/index.html matplotlib 참고
# In[16]:

# 2개의 서브플롯 출력
fig, axs = plt.subplots(2) # 세로로 놓인 2개의 서브플롯 생성 
# 함수가 호출될 떄 생선된 Figure 객체를 참조하는 변수 : fig
#여기서 fig 변수는 전체 그림을 나타내는 Figure 객체를 참조하고
# 함수가 호출될 때 생성된 Axes 객체(또는 Axes 객체들의 배열)를 참조하는 변수 : axs
#Axes 객체는 서브플롯 하나를 나타내며, 그림에 데이터를 플로팅하고 스타일링하는 데 사용됩니다.
axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
# 두번쨰 
axs[1].hist(ns_book7['대출건수'], bins=100)
axs[1].set_yscale('log')

fig.show()


# In[17]:

# subplot(행, 열) 행과 열을 구분 
# 2행 1열(기본값1열)
fig, axs = plt.subplots(2, figsize=(6, 8))
# nrow = 2
# nocol = 1
# subplots(nrows: 'int'=1, ncols: 'int'=1)
# plt.subplot(nrows,ncols,index)
axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
axs[0].set_title('scatter plot')

axs[1].hist(ns_book7['대출건수'], bins=100)
axs[1].set_title('histogram') # 제목설정 
axs[1].set_yscale('log')

fig.show()


# In[18]:
# subplot(행, 열) 행과 열을 구분 원하는 서브플롯 개수의 figure를 만들수 있음.
# 1행 2열
# nrow = 1
# nocol = 2

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
axs[0].set_title('scatter plot')
axs[0].set_xlabel('number of books')
axs[0].set_ylabel('borrow count')

axs[1].hist(ns_book7['대출건수'], bins=100)  # bins = 100 100개의 구간 
axs[1].set_title('histogram')
axs[1].set_yscale('log') # y축의 스케일을 지정하여 데이터를 좀 더 자세히 관찰 
axs[1].set_xlabel('borrow count') # x축 이름 지정 
axs[1].set_ylabel('frequency')

fig.show()

