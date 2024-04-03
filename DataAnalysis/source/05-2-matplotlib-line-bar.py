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

gdown.download('https://bit.ly/3pK7iuu', './data/ns_book7.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book7 = pd.read_csv('./data/ns_book7.csv', low_memory=False)
ns_book7.head()


# In[3]:

# value_counts() 고유한 값의 등장 횟수
# (발행년도 별 건수 출력)
# 지정된 컬럼의 값이 인덱스
count_by_year = ns_book7['발행년도'].value_counts()
count_by_year


# In[4]:

# value_counts()
# 정렬: 오름차순
count_by_year = count_by_year.sort_index()
count_by_year


# In[5]:

# 인덱스 값이 2030이하인 자료하만 추출
count_by_year = count_by_year[count_by_year.index <= 2030]
count_by_year

import numpy as np 
# ## 주제별 도서 개수 구하기
print(ns_book7.info())
#  주제분류번호   359792 non-null  object 숫자가 아닌 문자열임.
ns_book_subject_type = ns_book7['주제분류번호'].dtype
print("ns_book_subject_type:", type(ns_book_subject_type))
# ns_book_subject_type: <class 'numpy.dtypes.ObjectDType'>
print(ns_book7['주제분류번호'].dtype) # object # 개별자료형 확인 
print(ns_book7.dtypes) # 전체 컬럼의 자료형 확인

print(isinstance(ns_book_subject_type, object)) # True
print(isinstance(ns_book_subject_type, str)) # False
print(isinstance(ns_book_subject_type, np.dtypes.ObjectDType))  # True
# In[6]:
# 열에서 -> ['주제분류번호']의 첫번 쨰 열을 기준으로 도서를 카운트 하면 
# 주제별 도서 개수를 구할 수 있다. 
# 열에는 NaN값이 포함되므로 NaN이 포함되면 -1을 반환하여 걸럼냄
# ['주제분류번호']열의 값을 받아 첫번 쨰 문자를 반환하는  kdc_1st_char()함수
# 선언 후 apply()에 넣어 df 반복

cnt = 0
def kdc_1st_char(no):
    global cnt
    cnt += 1
    print(f"[{cnt}] {no}", end=',')
    if no is np.nan:
        print(no)
        return '-1'
    else:
        print(f"{no[0]}") # 맨 앞자리 수/글자
        return no[0]
# ['주제분류번호']열에 대하여 위 함수에 no(첫번쨰문자)를 전달하여 해당하는 
# 출력값을 value_count()으로 받음 , ns_book7['주제분류번호'].apply(kdc_1st_char)이
# 지정된 컬럼으로 -1~8 까지의 값을 갖는다.
count_by_subject = ns_book7['주제분류번호'].apply(kdc_1st_char).value_counts()
count_by_subject


# ## 선 그래프 그리기

# In[7]:


import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 100 # 해상도 높이기 


# In[8]:

# 발행년도별 도서수 
plt.plot(count_by_year.index, count_by_year.values)
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()


# In[9]:

# linestyle='-'(실선), ':'(점선), '-.'(쇄선), '--'(파선)
# color #ff0000 16진수 컬러코드로 지정 또는 색 이름으로 지정
# marker='.' : 데이터 포인트의 위치를 드러냄 즉 분포도 확인 가능
plt.plot(count_by_year, marker='.', linestyle=':', color='red')
plt.plot(count_by_year, marker='.', linestyle='dotted', color='red')
plt.plot(count_by_year, marker='.', linestyle='dotted', color='#0000ff')
plt.plot(count_by_year, marker='.', linestyle='dotted', color='#000000') # black
plt.plot(count_by_year, marker='.', linestyle=':', color='red')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()


# In[10]:

# *-g: 별모양, solid, green
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()


# In[11]:
#  plt.annotate(val, (idx, val)) idx: 그래프에 나타낼 문자열을 지정하고,
# indx,val 두번 쨰 매개변수에 문자열이 나타낼 x,y 좌표를 튜플로 지정
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items(): #스텝옵션을 사용
    plt.annotate(val, (idx, val))
plt.show()


# In[12]:


plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
    plt.annotate(val, (idx, val), xytext=(idx+1, val+10)) # marker로 부터 xytext를 활용하여
    # 좌표이동 x축 1만큼 , y축 10만큼
plt.show()


# In[13]:

# y축의 눈금을 지정하려면 yticks()사용 , 서브플롯을 그릴 떄 x축,y축 눈금을 지정하려면
# set.xticks(), set.yticks() 활용
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
    plt.annotate(val, (idx, val), xytext=(2, 2), textcoords='offset points')
plt.show()
# y축의 스캐일이 0~17500사이로 10만큼 벌려봐야 
# textcoords 매개변수를 사용하여 포인트 상대 위치를 나타내는 offset points를 지정
# ## 막대 그래프 그리기

# In[14]:


plt.bar(count_by_subject.index, count_by_subject.values)
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (idx, val), xytext=(0, 2), textcoords='offset points')
plt.show()
#%% 
# y축의 값의 위치를 bar상단 중심부로 이동시키기 
plt.bar(count_by_subject.index, count_by_subject.values)
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (idx, val), xytext=(-12, 2), textcoords='offset points')
plt.show()


# In[15]:
# 세로 막대그래프 그리기
# width매개변수 기본값 0.8(1로 설정하면 막대의 두께가 눈금 간격과 동일해져서 막대사이에 간격이 사라짐  / 색 : blue
plt.bar(count_by_subject.index, count_by_subject.values, width=0.7, color='blue')
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (idx, val), xytext=(0, 2), textcoords='offset points', 
                 fontsize=8, ha='center', color='green')
plt.show()


# In[16]:

# 가로 막대그래프 그리기 
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
 # PIL package
pil_img = Image.open('./data/jupiter.png')
plt.figure(figsize=(8, 6))
plt.imshow(pil_img)
plt.axis('off')
plt.show()


# In[22]:


import numpy as np

arr_img = np.array(pil_img)
arr_img.shape


# In[23]:

# jpg로 저장하여 이미지 용량이 png에 비해 줄었다. png 데이터 무손실(원본데이터)
plt.imsave('./data/jupiter-save.jpg', arr_img)


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
plt.savefig('books_by_subject.png') # savefig() 그래프를 이미지로 저장  / dpi 따로 지정가능
# plt.rcParams['savefig.dpi'] 위처럼.
plt.show()


# In[26]:


pil_img = Image.open('books_by_subject.png')

plt.figure(figsize=(8, 6))
plt.imshow(pil_img)
plt.axis('off')
plt.show()

