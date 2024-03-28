#!/usr/bin/env python
# coding: utf-8

# # 05-2 선, 막대 그래프 그리기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/05-2.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/05-2.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 연도별 발행 도서 개수 구하기

# In[1]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()


# In[3]:


count_by_year = ns_book7['발행년도'].value_counts()
count_by_year


# In[4]:


count_by_year = count_by_year.sort_index()
count_by_year


# In[5]:


count_by_year = count_by_year[count_by_year.index <= 2030]
count_by_year


# ## 주제별 도서 개수 구하기

# In[6]:


import numpy as np

def kdc_1st_char(no):
    if no is np.nan:
        return '-1'
    else:
        return no[0]

count_by_subject = ns_book7['주제분류번호'].apply(kdc_1st_char).value_counts()
count_by_subject


# ## 선 그래프 그리기

# In[7]:


import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 100


# In[8]:


plt.plot(count_by_year.index, count_by_year.values)
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()


# In[9]:


plt.plot(count_by_year, marker='.', linestyle=':', color='red')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()


# In[10]:


plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()


# In[11]:


plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
    plt.annotate(val, (idx, val))
plt.show()


# In[12]:


plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
    plt.annotate(val, (idx, val), xytext=(idx+1, val+10))
plt.show()


# In[13]:


plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
    plt.annotate(val, (idx, val), xytext=(2, 2), textcoords='offset points')
plt.show()


# ## 막대 그래프 그리기

# In[14]:


plt.bar(count_by_subject.index, count_by_subject.values)
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (idx, val), xytext=(0, 2), textcoords='offset points')
plt.show()


# In[15]:


plt.bar(count_by_subject.index, count_by_subject.values, width=0.7, color='blue')
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (idx, val), xytext=(0, 2), textcoords='offset points', 
                 fontsize=8, ha='center', color='green')
plt.show()


# In[16]:


plt.barh(count_by_subject.index, count_by_subject.values, height=0.7, color='blue')
plt.title('Books by subject')
plt.xlabel('number of books')
plt.ylabel('subject')
for idx, val in count_by_subject.items():
    plt.annotate(val, (val, idx), xytext=(2, 0), textcoords='offset points', 
                 fontsize=8, va='center', color='green')
plt.show()


# ## 이미지 출력하고 저장하기

# In[17]:


# 노트북이 코랩에서 실행 중인지 체크합니다.
import sys
if 'google.colab' in sys.modules:
    # 샘플 이미지를 다운로드합니다.
    get_ipython().system('wget https://bit.ly/3wrj4xf -O jupiter.png')


# In[18]:


img = plt.imread('jupiter.png')
img.shape


# In[19]:


plt.imshow(img)
plt.show()


# In[20]:


plt.figure(figsize=(8, 6))
plt.imshow(img)
plt.axis('off')
plt.show()


# In[21]:


from PIL import Image

pil_img = Image.open('jupiter.png')
plt.figure(figsize=(8, 6))
plt.imshow(pil_img)
plt.axis('off')
plt.show()


# In[22]:


import numpy as np

arr_img = np.array(pil_img)
arr_img.shape


# In[23]:


plt.imsave('jupiter.jpg', arr_img)


# ## 그래프를 이미지로 저장하기

# In[24]:


plt.rcParams['savefig.dpi']


# In[25]:


plt.barh(count_by_subject.index, count_by_subject.values, height=0.7, color='blue')
plt.title('Books by subject')
plt.xlabel('number of books')
plt.ylabel('subject')
for idx, val in count_by_subject.items():
    plt.annotate(val, (val, idx), xytext=(2, 0), textcoords='offset points', 
                 fontsize=8, va='center', color='green')
plt.savefig('books_by_subject.png')
plt.show()


# In[26]:


pil_img = Image.open('books_by_subject.png')

plt.figure(figsize=(8, 6))
plt.imshow(pil_img)
plt.axis('off')
plt.show()

