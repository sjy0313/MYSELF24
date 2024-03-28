#!/usr/bin/env python
# coding: utf-8

# # 02-2 스크래핑 사용하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/02-2.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/02-2.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 검색 결과 페이지 가져오기

# In[1]:


import gdown

gdown.download('https://bit.ly/3q9SZix', './data/20s_best_book.json', quiet=False)


# In[2]:


import pandas as pd

books_df = pd.read_json('./data/20s_best_book.json')
books_df.head()


# In[3]:

# 컬럼선택
books = books_df[['no','ranking','bookname','authors','publisher',
                 'publication_year','isbn13']]
books.head()


# In[4]:

# 인덱스 : 0,1 행
# 컬럼:  ['bookname','authors']
books_df.loc[[0,1], ['bookname','authors']]
'''
0  우리가 빛의 속도로 갈 수 없다면 :김초엽 소설   지은이: 김초엽
1         달러구트 꿈 백화점.이미예 장편소설   지은이: 이미예
'''

# In[5]:

# 인덱스 : 0,1 행
# 컬럼:  'bookname':'authors' 범위
books_df.loc[0:1, 'bookname':'authors']


# In[6]:

# 인덱스 : 0,1 행
# 컬럼:  'no':'isbn13'' 범위
books = books_df.loc[:, 'no':'isbn13']
books.head()


# In[7]:
    
# 인덱스 : 0부터 끝까지 2steps 씩
# 컬럼:  'no':'isbn13'' 범위
# 처음부터 5개의 행을 선택
books_df.loc[::2, 'no':'isbn13'].head()
'''
   no  ranking  ... publication_year         isbn13
0   1        1  ...             2019  9791190090018
2   3        3  ...             2019  9791188862290
4   5        5  ...             2017  9788936434267
6   7        7  ...             2020  9791165300005
8   9        9  ...             2019  9788936477196


[5 rows x 7 columns]
'''
books_df.loc[[5], ['isbn13']].head()
#          isbn13
#5  9788936434243
# In[8]:

# DH_KEY_TOO_SMALL 에러가 발생하는 경우 다음 코드의 주석을 제거하고 실행하세요.
# https://stackoverflow.com/questions/38015537/python-requests-exceptions-sslerror-dh-key-too-small
# import requests

# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
# try:
#     requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
# except AttributeError:
#     # no pyopenssl support used / needed / available
#     pass

# In[9]:


import requests

isbn = 9791190090018      # '우리가 빛의 속도로 갈 수 없다면'의 ISBN
url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'

r = requests.get(url.format(isbn)) # 해당 데이터를 url에 get요청을 보내 받아옴 그 값을 r변수에 할당
# r : models.Response 
# "model.response"는 Python에서 머신 러닝 또는 딥 러닝 모델을 훈련하거나
# 사용할 때 사용되는 용어 중 하나입니다. 이 용어는 일반적으로 
#모델이 입력 데이터에 대한 예측 또는 출력을 나타내는 데 사용됩니다.

#예를 들어, 회귀 모델의 경우 "model.response"는 모델이 예측한 연속적인 값일 수 있습니다. 
#분류 모델의 경우 "model.response"는 클래스 레이블에 대한 확률 또는 예측된 클래스일 수 있습니다.

# In[10]:

# HTML
print(r.text)


# ## 뷰티플수프

# In[11]:


from bs4 import BeautifulSoup


# In[12]:


soup = BeautifulSoup(r.text, 'html.parser')


# In[13]:


prd_link = soup.find('a', attrs={'class':'gd_name'})


# In[14]:


print(prd_link)
'''
<a class="gd_name" href="/Product/Goods/74261416" onclick="wiseLogV2('S', '101_005_003_001', '');
setGoodsClickExtraCodeHub('032', '9791190090018', '74261416', '0');">우리가 빛의 속도로 갈 수 없다면</a>
'''

# In[15]:


print(prd_link['href']) # /Product/Goods/74261416


# In[16]:


# '우리가 빛의 속도로 갈 수 없다면'의 상세 페이지 가져오기
# Python에서 ['href']는 HTML 요소에서 'href' 속성의 값을 가져오는 것을 의미
# 이를 통해 웹 스크래핑을 할 때 특정 링크의 URL을 추출하거나 해당 링크로 이동할 수 있습니다.
url = 'http://www.yes24.com'+prd_link['href']
r = requests.get(url)
# https://www.yes24.com/Product/Goods/74261416 

# In[17]:


print(r.text)


# In[18]:


soup = BeautifulSoup(r.text, 'html.parser')
prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
print(prd_detail) # None


# In[19]:


prd_tr_list = prd_detail.find_all('tr')
print(prd_tr_list)


# In[20]:


for tr in prd_tr_list:
    if tr.find('th').get_text() == '쪽수, 무게, 크기':
        page_td = tr.find('td').get_text()
        break


# In[21]:


print(page_td) # 330쪽 | 496g | 130*198*30mm


# In[22]:
# 파이썬의 split() 메서드는 문자열(str) 자료형에 대해서 사용가능
print(page_td.split()) #['330쪽', '|', '496g', '|', '130*198*30mm']
print(page_td.split()[0]) # 330쪽


# ## 전체 도서의 쪽수 구하기

# In[23]:


def get_page_cnt(isbn):
    # Yes24 도서 검색 페이지 URL
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져옵니다.
    r = requests.get(url.format(isbn))
    soup = BeautifulSoup(r.text, 'html.parser')   # HTML 파싱
    # 검색 결과에서 해당 도서를 선택합니다.
    prd_info = soup.find('a', attrs={'class':'gd_name'})
    if prd_info == None:
        return ''
    # 도서 상세 페이지를 가져옵니다.
    url = 'http://www.yes24.com'+prd_info['href']
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # 상품 상세정보 div를 선택합니다.
    prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
    # 테이블에 있는 tr 태그를 가져옵니다.
    prd_tr_list = prd_detail.find_all('tr')
    # 쪽수가 들어 있는 th를 찾아 td에 담긴 값을 반환합니다.
    for tr in prd_tr_list:
        if tr.find('th').get_text() == '쪽수, 무게, 크기':
            return tr.find('td').get_text().split()[0]
    return ''


# In[24]:


get_page_cnt(9791190090018) # '330쪽'

get_page_cnt(9791167901484) # '456쪽' 


# In[25]:


top10_books = books.head(10)



# In[26]:

# 방법[1]
def get_page_cnt2(row):
    isbn = row['isbn13']
    return get_page_cnt(isbn)


# In[27]:

# 리턴 : Series, 요소 10개
page_count = top10_books.apply(get_page_cnt2, axis=1)
print(page_count)
'''
0    330쪽
1    300쪽
2    228쪽
3    340쪽
4    264쪽
5    396쪽
6    272쪽
7    get_page_cnt(9791167901484) # '456쪽' 
8    244쪽
9    296쪽
Name: page_count, dtype: object
'''

# In[28]:

# 방법[2]
page_count2 = top10_books.apply(lambda row: get_page_cnt(row['isbn13']), axis=1) # axis = 1 열단위


# In[29]:


page_count.name = 'page_count'
print(page_count)
'''
0    330쪽
1    300쪽
2    228쪽
3    340쪽
4    264쪽
5    396쪽
6    272쪽
7  get_page_cnt(9791167901484) # '456쪽' 
8    244쪽
9    296쪽
Name: page_count, dtype: object
'''

# In[30]:

# 스크래핑한 책 정보 (merge()를 활용해서 폐이지 정보를 합쳐준다)
top10_with_page_count = pd.merge(top10_books, page_count,
                                 left_index=True, right_index=True)
top10_with_page_count


# ## `merge()` 함수의 매개변수

# In[31]:


df1 = pd.DataFrame({'col1': ['a','b','c'], 'col2': [1,2,3]})
df1
'''
  col1  col2
0    a     1
1    b     2
2    c     3
'''

# In[32]:


df2 = pd.DataFrame({'col1': ['a','b','d'], 'col3': [10,20,30]})
df2
'''
 col1  col3
0    a    10
1    b    20
2    d    30
'''

# In[33]:
# merge()는 집합에서의 조건제시법과 유사, 조건에 맞는 집합만 데이터로 추출하여 df형태로 만들어줌 
# 두 데이터프레임에 모두 존재하는 요소만 선택
pd.merge(df1, df2, on='col1')
'''
  col1  col2  col3
0    a     1    10
1    b     2    20
'''
# concat()은 두 데이터를 연결시켜주는 역할을 하지만 merge()는 두 데이터를 병합하여 준다.
# 이때 axis=0 이면 행방향 정열을 시켜 series 값으로 변환된다.
pd.concat([df1,df2], axis=1)
'''
  col1  col2 col1  col3
0    a     1    a    10
1    b     2    b    20
2    c     3    d    30
'''
# In[34]:

# how: 'inner', 기본값
# how: 'left', 왼쪽에 지정된 데이터프레임 기준
pd.merge(df1, df2, how='left', on='col1') # 기본값인 inner는 공통된 데이터를 병합(교집합)
'''
 col1  col2  col3
0    a     1  10.0
1    b     2  20.0
2    c     3   NaN
'''

# In[35]:


pd.merge(df1, df2, how='right', on='col1')
'''
col1  col2  col3
0    a   1.0    10
1    b   2.0    20
2    d   NaN    30
'''

# In[36]:

# col1기준으로 합치된 
pd.merge(df1, df2, how='outer', on='col1') # outer -> 모든 데이터를 병합(합집합)
# 어는 한쪽이라도 없는 데이터가 존재할 경우 NaN값이 지정됨. 
'''
 col1  col2  col3
0    a   1.0  10.0
1    b   2.0  20.0
2    c   3.0   NaN
3    d   NaN  30.0
'''

# In[37]:

# 병합할 열의 이름이 서로 다른 경우
# merge() 함수에서 right_on과 left_on은 두 데이터프레임을 병합할 때
# 사용되는 열의 이름을 지정하는 매개변수입니다.
pd.merge(df1, df2, left_on='col1', right_on='col1')
'''
 col1  col2  col3
0    a     1    10
1    b     2    20
'''

# In[38]:

# 공통된 column의 열의 이름을 임의로 설정
# 인덱스 기준으로 두 객체를 병합할 수 있습니다. 
# right_index=True -> df2 기준으로 병합
pd.merge(df1, df2, left_on='col2', right_index=True)
'''
  col1_x  col2 col1_y  col3
0      a     1      b    20
1      b     2      d    30
'''
#%%
# join() 함수는, merge()함수를 기반으로 만들어졌지만 join()는 행 인덱스를 기준(즉, 왼쪽첫번쨰
# 데이터프레임 how='left')을 기준으로 병합하는 반면에 
# merge()함수는, 함수의 기본값은 'inner'(공통된 데이터들의 집합[=교집합])으로 병합 방법을 
# 지정하지 않으면 inner-join이 기본적으로 수행.
# 따라서 정리하자면 pd.merge(df1,df2) = df1.join(df2)

# merge() 활용
pd.merge(df1,df2)
'''
  col1  col2  col3
0    a     1    10
1    b     2    20
'''
#%%
# join() 활용
#df1.join(df2, how='inner'), df1.join(df2) (x) 

#이 에러는 두 데이터프레임을 병합하려고 할 때 열 이름이 겹치지만 
#접미사(suffix)가 지정되지 않았기 때문에 발생합니다. 

# 해결방안)
#이런 경우에는 suffixes 매개변수를 사용하여 겹치는 열 이름에 대해 접미사를 지정해야 합니다.

# 예를 들어, 두 데이터프레임에 모두 'col1'이라는 열이 있고
# 이 열들을 기준으로 병합하려고 할 때 발생하는 문제입니다.

# 이 경우에는 suffixes 매개변수를 사용하여 두 번째 데이터프레임의 열에
# 접미사를 추가하여 겹치는 열 이름을 구분해야 합니다.

# merge() 함수를 사용할 때 suffixes 매개변수를 사용하여 겹치는 열에 대한 접미사 지정

pd.merge(df1, df2, on='col1', suffixes=('_left', '_right'))
'''
  col1  col2  col3
0    a     1    10
1    b     2    20
'''




pd.merge(df1, df2, left_on='col2', right_index=True)
'''
  col1_x  col2 col1_y  col3
0      a     1      b    20
1      b     2      d    30
'''
result = df1.join(df2.set_index('col1'), on='col1', how='inner')
print(result)
'''
  col1  col2  col3
0    a     1    10
1    b     2    20
'''
df1.join(df2, lsuffix='_left', rsuffix='_right', how='inner')

'''
    col1_left  col2 col1_right  col3
  0         a     1          a    10
  1         b     2          b    20
  2         c     3          d    30
'''






















