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

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()


# In[3]:


import matplotlib.pyplot as plt

plt.scatter([1,2,3,4], [1,2,3,4])
plt.show()


# In[4]:


plt.scatter(ns_book7['번호'], ns_book7['대출건수'])
plt.show()


# In[5]:


plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'])
plt.show()


# In[6]:


plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()


# In[7]:


average_borrows = ns_book7['대출건수']/ns_book7['도서권수']
plt.scatter(average_borrows, ns_book7['대출건수'], alpha=0.1)
plt.show()


# ## 히스토그램 그리기

# In[8]:


plt.hist([0,3,5,6,7,7,9,13], bins=5)
plt.show()


# In[9]:


import numpy as np

np.histogram_bin_edges([0,3,5,6,7,7,9,13], bins=5)


# In[10]:


np.random.seed(42)
random_samples = np.random.randn(1000)


# In[11]:


print(np.mean(random_samples), np.std(random_samples))


# In[12]:


plt.hist(random_samples)
plt.show()


# In[13]:


plt.hist(ns_book7['대출건수'])
plt.show()


# In[14]:


plt.hist(ns_book7['대출건수'])
plt.yscale('log')
plt.show()


# In[15]:


plt.hist(ns_book7['대출건수'], log=True)
plt.show()


# In[16]:


plt.hist(ns_book7['대출건수'], bins=100)
plt.yscale('log')
plt.show()


# In[17]:


title_len = ns_book7['도서명'].apply(len)
plt.hist(title_len, bins=100)
plt.show()


# In[18]:


plt.hist(title_len, bins=100)
plt.xscale('log')
plt.show()


# ## 상자 수염 그림 그리기

# In[19]:


temp = ns_book7[['대출건수','도서권수']]


# In[20]:


plt.boxplot(temp)
plt.show()


# In[21]:


plt.boxplot(ns_book7[['대출건수','도서권수']])
plt.yscale('log')
plt.show()


# In[22]:


plt.boxplot(ns_book7[['대출건수','도서권수']], vert=False)
plt.xscale('log')
plt.show()


# In[23]:


plt.boxplot(ns_book7[['대출건수','도서권수']], whis=10)
plt.yscale('log')
plt.show()


# In[24]:


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

# #### 4.

# In[29]:


selected_rows = (1980 <= ns_book7['발행년도']) & (ns_book7['발행년도'] <= 2022)
plt.hist(ns_book7.loc[selected_rows, '발행년도'])
plt.show()


# #### 5.

# In[30]:


plt.boxplot(ns_book7.loc[selected_rows, '발행년도'])
plt.show()

