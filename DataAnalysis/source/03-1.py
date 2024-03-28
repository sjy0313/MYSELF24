#!/usr/bin/env python
# coding: utf-8

# # 03-1 불필요한 데이터 삭제하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/03-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/03-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 열 삭제하기

# In[40]:


import gdown

gdown.download('https://bit.ly/3RhoNho', 'ns_202104.csv', quiet=False)


# In[41]:


import pandas as pd

ns_df = pd.read_csv('ns_202104.csv', low_memory=False)
ns_df.head()


# In[42]:


ns_book = ns_df.loc[:, '번호':'등록일자']
ns_book.head()


# In[43]:


print(ns_df.columns)


# In[44]:


print(ns_df.columns[0])


# In[45]:


ns_df.columns != 'Unnamed: 13'


# In[46]:


selected_columns = ns_df.columns != 'Unnamed: 13'
ns_book = ns_df.loc[:, selected_columns]
ns_book.head()


# In[47]:


selected_columns = ns_df.columns != '부가기호'
ns_book = ns_df.loc[:, selected_columns]
ns_book.head()


# In[48]:


ns_book = ns_df.drop('Unnamed: 13', axis=1)
ns_book.head()


# In[49]:


ns_book = ns_df.drop(['부가기호','Unnamed: 13'], axis=1)
ns_book.head()


# In[50]:


ns_book.drop('주제분류번호', axis=1, inplace=True)
ns_book.head()


# In[51]:

# 열에 하나라도 nan이 포함되어 있으면 칼럼을 삭제
ns_book = ns_df.dropna(axis=1)
ns_book.head()


# In[52]:

# 칼럼의 모든 데이터가 nan이면 칼럼을 삭제
ns_book = ns_df.dropna(axis=1, how='all')
ns_book.head()


# ## 행 삭제하기

# In[53]:


# 행의 인덱스 0,1 삭제
ns_book2 = ns_book.drop([0,1])
ns_book2.head()


# In[54]:


ns_book2 = ns_book[2:]
ns_book2.head()


# In[55]:

# 슬라이스는 끝 번호가 포함되지 않음: 0,1 행 선택
ns_book2 = ns_book[0:2]
ns_book2.head()


# In[56]:


selected_rows = ns_df['출판사'] == '한빛미디어'
ns_book2 = ns_book[selected_rows]
ns_book2.head()


# In[57]:


ns_book2A = ns_book.loc[selected_rows]
ns_book2A.head()


# In[58]:

ns_book2_selected = ns_book['대출건수'] > 1000
# ns_book2 = ns_book[ns_book['대출건수'] > 1000]
ns_book2 = ns_book[ns_book2_selected]
ns_book2.head()


# ## 중복된 행 찾기

# In[59]:


# 전체 칼럼을 기준으로 중복되는 행
sum(ns_book.duplicated())


# In[60]:

# 칼럼이 '도서명','저자','ISBN'에서 중복되는 행
sum(ns_book.duplicated(subset=['도서명','저자','ISBN']))


# In[61]:


dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN'], keep=False)
ns_book3 = ns_book[dup_rows]
ns_book3.head()


# In[62]:


count_df = ns_book[['도서명','저자','ISBN','권','대출건수']]


# In[63]:


group_df = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False)
loan_count = group_df.sum()


# In[64]:


loan_count = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False).sum()
loan_count.head()


# In[65]:


dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN','권'])
unique_rows = ~dup_rows
ns_book3 = ns_book[unique_rows].copy()


# In[66]:


sum(ns_book3.duplicated(subset=['도서명','저자','ISBN','권']))


# In[67]:


ns_book3.set_index(['도서명','저자','ISBN','권'], inplace=True)
ns_book3.head()


# In[68]:


ns_book3.update(loan_count)
ns_book3.head()


# In[69]:


ns_book4 = ns_book3.reset_index()
ns_book4.head()


# In[70]:


sum(ns_book['대출건수']>100)


# In[71]:


sum(ns_book4['대출건수']>100)


# In[72]:


ns_book4 = ns_book4[ns_book.columns]
ns_book4.head()


# In[73]:


ns_book4.to_csv('ns_book4.csv', index=False)


# In[74]:


def data_cleaning(filename):
    """
    남산 도서관 장서 CSV 데이터 전처리 함수
    
    :param filename: CSV 파일이름
    """
    # 파일을 데이터프레임으로 읽습니다.
    ns_df = pd.read_csv(filename, low_memory=False)
    # NaN인 열을 삭제합니다.
    ns_book = ns_df.dropna(axis=1, how='all')

    # 대출건수를 합치기 위해 필요한 행만 추출하여 count_df 데이터프레임을 만듭니다.
    count_df = ns_book[['도서명','저자','ISBN','권','대출건수']]
    # 도서명, 저자, ISBN, 권을 기준으로 대출건수를 groupby합니다.
    loan_count = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False).sum()
    # 원본 데이터프레임에서 중복된 행을 제외하고 고유한 행만 추출하여 복사합니다.
    dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN','권'])
    unique_rows = ~dup_rows
    ns_book3 = ns_book[unique_rows].copy()
    # 도서명, 저자, ISBN, 권을 인덱스로 설정합니다.
    ns_book3.set_index(['도서명','저자','ISBN','권'], inplace=True)
    # load_count에 저장된 누적 대출건수를 업데이트합니다.
    ns_book3.update(loan_count)
    
    # 인덱스를 재설정합니다.
    ns_book4 = ns_book3.reset_index()
    # 원본 데이터프레임의 열 순서로 변경합니다.
    ns_book4 = ns_book4[ns_book.columns]
    
    return ns_book4


# In[75]:


new_ns_book4 = data_cleaning('ns_202104.csv')

ns_book4.equals(new_ns_book4)

