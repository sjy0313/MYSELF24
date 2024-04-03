#!/usr/bin/env python
# coding: utf-8

# # 06-1 객체지향 API로 그래프 꾸미기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/06-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/06-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## pyplot 방식과 객체지향 API 방식

# In[1]:


import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 100


# In[2]:

# figure 객체를 명시적으로 생성하지 않고 사용
plt.plot([1, 4, 9, 16]) # default figure객체가 존재하기 때문에 출력된 것
plt.title('simple line graph')
plt.show()


# In[3]:
# 이 형태로 그래프 만드는 것이 위에 fig객체를 명시적으로 주지않았을 떄 보다 clear 함.
# fig라는 틀에 ax라는 종이를 놓고 그 위해 그래프를 그린다고 생각
# 명시적으로 figure객체를 얻어서 사용 
fig, ax = plt.subplots()
ax.plot([1, 4, 9, 16])
ax.set_title('simple line graph')
fig.show()


# ## 그래프에 한글 출력하기

# 이 노트북은 맷플롯립 그래프에 한글을 쓰기 위해 나눔 폰트를 사용합니다. 코랩의 경우 다음 셀에서 나눔 폰트를 직접 설치합니다.

# In[4]:


# 노트북이 코랩에서 실행 중인지 체크합니다.
'''
import sys
if 'google.colab' in sys.modules:
    get_ipython().system("echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections")
    # 나눔 폰트를 설치합니다.
    get_ipython().system('sudo apt-get -qq -y install fonts-nanum')
    ''' 
#폰트 설치 
# https://hangeul.naver.com/font
# 압축하기 후 ttf 파일선택 -> 종류별 파일선택 후 들어가서 
# 개별적(개인용)으로 설치(우클릭 -> 모든 사용자용으로 설치)
# 나눔고딕 : NanumGothic.ttf
# 나눔스퀘어 폰트 ppt만들 떄 활용하면 가독성 올라감.
import matplotlib.font_manager as fm
font_files = fm.findSystemFonts(fontpaths=['C:/Users/Shin/AppData/Local/Microsoft/Windows/Fonts'])
# \는 escape 문자로 인식하여 error 발생
for fpath in font_files:
        print(fpath)
        fm.fontManager.addfont(fpath)


# In[5]:


plt.rcParams['figure.dpi'] = 100


# In[6]:


plt.rcParams['font.family']


# In[7]:


# 나눔고딕 폰트를 사용합니다.
plt.rcParams['font.family'] = 'NanumGothic'


# In[8]:


# 위와 동일하지만 이번에는 나눔바른고딕 폰트로 설정합니다.
plt.rc('font', family='NanumBarunGothic') # rc() -> font 그룹/ family 하위그룹


# In[9]:


plt.rc('font', family='NanumBarunGothic', size=11) 


# In[10]:


print(plt.rcParams['font.family'], plt.rcParams['font.size'])


# In[11]:


from matplotlib.font_manager import findSystemFonts
findSystemFonts()


# In[12]:
plt.rcParams['font.family'] = 'NanumBarunGothic'
#plt.rcParams['font.family'] = 'NanumGothic'
plt.plot([1, 4, 9, 16])
plt.title('간단한 선 그래프')
plt.show()


# In[13]:


plt.rc('font', size=10) # rc()함수 font가 그룹


# ## 출판사별 발행 도서 개수 산점도 그리기

# In[14]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', './data/ns_book7.csv', quiet=False)


# In[15]:


import pandas as pd

ns_book7 = pd.read_csv('./data/ns_book7.csv', low_memory=False)
ns_book7.head()


# In[16]:

# 상위 30개 출판사 ( 마지막 인덱스는 범위에 포함x 가져오려는 인덱스보다 하나 더 크게 지정)
top30_pubs = ns_book7['출판사'].value_counts()[:30]
top30_pubs


# In[17]:

 # 상위 30개에 해당 하는 출판사 True, 아닌 출판사는 False로 반환
top30_pubs_idx = ns_book7['출판사'].isin(top30_pubs.index)
top30_pubs_idx
# isin()에 값을 전달하면 df에 일치하는 값을 찾아 boolean array 반환

# In[18]:

#true인 원소의 개수 : 상위 30개 출판사에 해당하는 책의 개수
top30_pubs_idx.sum() # 51886


# In[19]:

# random_state는 seed()와 유사하게 동일한 값을 전달하면 항상 같은 결과를 얻을 수 있음
ns_book8 = ns_book7[top30_pubs_idx].sample(1000, random_state=42)
ns_book8.head()


# In[20]:


fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'])
ax.set_title('출판사별 발행도서')
fig.show()


# In[21]:


plt.rcParams['lines.markersize'] # 6.0 default size 


# In[22]:

# 마커 사이즈 : s=ns_book8['대출건수'])
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'], s=ns_book8['대출건수'])
ax.set_title('출판사별 발행도서')
fig.show()


# In[23]:
# 마커 꾸미기
#  s=ns_book8['대출건수']*2 크기를 부각시키기 위함. 
# alpha=0.3 투명도 조절
# edgecolors() 마커 테두리의 색 변경
# linewidth 마커 테두리 선 두께 기본값 1.5, 0.5로 지정하여 얇은 테두리 그림
# c : 산점도의 색, s도 마찬가지로 데이터 개수와 동일한 길이의 배열을 전달하면
# 큰 값은 밝은 노란색 , 낮은 값은 진한 녹색으로 그린다.

fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'], 
           linewidths=0.5, edgecolors='k', alpha=0.3,
           s=ns_book8['대출건수']*2, c=ns_book8['대출건수'])
ax.set_title('출판사별 발행도서')
fig.show()


# In[24]:

# cmap컬러맵(jet -> 낮은 값-> 짙은 파란/ 높은 값 -> 노란색-> 붉은 색)
fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(ns_book8['발행년도'], ns_book8['출판사'], 
                linewidths=0.5, edgecolors='k', alpha=0.3,
                s=ns_book8['대출건수']**1.3, c=ns_book8['대출건수'], cmap='jet')
ax.set_title('출판사별 발행도서')
fig.colorbar(sc)
fig.show()

