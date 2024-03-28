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


plt.plot([1, 4, 9, 16])
plt.title('simple line graph')
plt.show()


# In[3]:


fig, ax = plt.subplots()
ax.plot([1, 4, 9, 16])
ax.set_title('simple line graph')
fig.show()


# ## 그래프에 한글 출력하기

# 이 노트북은 맷플롯립 그래프에 한글을 쓰기 위해 나눔 폰트를 사용합니다. 코랩의 경우 다음 셀에서 나눔 폰트를 직접 설치합니다.

# In[4]:


# 노트북이 코랩에서 실행 중인지 체크합니다.
import sys
if 'google.colab' in sys.modules:
    get_ipython().system("echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections")
    # 나눔 폰트를 설치합니다.
    get_ipython().system('sudo apt-get -qq -y install fonts-nanum')
    import matplotlib.font_manager as fm
    font_files = fm.findSystemFonts(fontpaths=['/usr/share/fonts/truetype/nanum'])
    for fpath in font_files:
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
plt.rc('font', family='NanumBarunGothic')


# In[9]:


plt.rc('font', family='NanumBarunGothic', size=11)


# In[10]:


print(plt.rcParams['font.family'], plt.rcParams['font.size'])


# In[11]:


from matplotlib.font_manager import findSystemFonts
findSystemFonts()


# In[12]:


plt.plot([1, 4, 9, 16])
plt.title('간단한 선 그래프')
plt.show()


# In[13]:


plt.rc('font', size=10)


# ## 출판사별 발행 도서 개수 산점도 그리기

# In[14]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)


# In[15]:


import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()


# In[16]:


top30_pubs = ns_book7['출판사'].value_counts()[:30]
top30_pubs


# In[17]:


top30_pubs_idx = ns_book7['출판사'].isin(top30_pubs.index)
top30_pubs_idx


# In[18]:


top30_pubs_idx.sum()


# In[19]:


ns_book8 = ns_book7[top30_pubs_idx].sample(1000, random_state=42)
ns_book8.head()


# In[20]:


fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'])
ax.set_title('출판사별 발행도서')
fig.show()


# In[21]:


plt.rcParams['lines.markersize']


# In[22]:


fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'], s=ns_book8['대출건수'])
ax.set_title('출판사별 발행도서')
fig.show()


# In[23]:


fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'], 
           linewidths=0.5, edgecolors='k', alpha=0.3,
           s=ns_book8['대출건수']*2, c=ns_book8['대출건수'])
ax.set_title('출판사별 발행도서')
fig.show()


# In[24]:


fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(ns_book8['발행년도'], ns_book8['출판사'], 
                linewidths=0.5, edgecolors='k', alpha=0.3,
                s=ns_book8['대출건수']**1.3, c=ns_book8['대출건수'], cmap='jet')
ax.set_title('출판사별 발행도서')
fig.colorbar(sc)
fig.show()

