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

gdown.download('https://bit.ly/3RhoNho', '../data/ns_202104.csv', quiet=False)
'''
기본적으로 quiet 매개변수는 True로 설정되어 있습니다. 
이는 다운로드가 진행될 때 진행 상황을 표시하지 않고, 
다운로드가 완료될 때까지 아무 메시지도 출력되지 않음을 의미합니다.
'''

# In[41]:


import pandas as pd

ns_df = pd.read_csv('./data/ns_202104.csv', low_memory=False)
ns_df.head()
'''
기본적으로 low_memory 매개변수는 True로 설정되어 있습니다. 
이는 pandas가 파일의 첫 번째 몇 줄을 살펴보고 데이터 유형을 추론하여 
메모리를 보다 효율적으로 사용하려고 시도함을 의미합니다. 
그러나 이 방법은 큰 파일을 처리할 때 정확성을 희생할 수 있습니다.

low_memory=False로 설정하면, pandas는 전체 파일을 한 번에 읽어들여 
메모리를 보다 적게 절약하고 정확성을 유지합니다. 이는 큰 CSV 파일을 처리할 때 유용할 수 있습니다. 
그러나 이 옵션은 메모리 사용량이 더 높을 수 있음을 염두에 두어야 합니다.
'''


# Unnamed: 13열은 csv파일 각 라인의 끝 ,가 있어서 자동으로 추가됨.

# In[42]:

# 인덱스 참조
# 행 : 전체(0~4)
# 열 : '번호'~'등록일자'

ns_book = ns_df.loc[:, '번호':'등록일자'] 
ns_book.head()


# In[43]:

# df의 컬럼명 추출
print(ns_df.columns)
'''
Index(['번호', '도서명', '저자', '출판사', '발행년도', 'ISBN', '세트 ISBN', '부가기호', '권',
       '주제분류번호', '도서권수', '대출건수', '등록일자', 'Unnamed: 13'],
      dtype='object')
'''

# In[44]:


print(ns_df.columns[0]) # 번호
print(ns_df.columns[-1]) # Unnamed: 13

# In[45]:

# column('Unnamed: 13')이 아닌 column은 True
# column('Unnamed: 13')인 column은 False 
# boolean array 
# !=는 비교연산자로 이렇게 반환된 결과는 numpy array넘파이 배열(==파이썬 리스트)
ns_df.columns != 'Unnamed: 13'
'''
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True, False])
'''

# In[46]:

# column('Unnamed: 13')이 아닌 column만 선택해서 데이터프레임을 생성
selected_columns = ns_df.columns != 'Unnamed: 13' 
ns_book = ns_df.loc[:, selected_columns]  #True인 열만 선택. 
ns_book.head()
# Unnamed: 13 제거됨.

# In[47]:
#column('부가기호')을 제외

selected_columns = ns_df.columns != '부가기호'
ns_book = ns_df.loc[:, selected_columns]
ns_book.head()


# In[48]:

# drop()매서드를 이용해서 열을 삭제
# axis : 0(행), 1(열)

ns_book = ns_df.drop('Unnamed: 13', axis=1)
ns_book.head()


# In[49]:

# Deleting multiple columns -> 리스트에 컬럼 목록을 지정
# 원본에 변화는 없었고 ns_book에 리턴값만 존재하였다.
ns_book = ns_df.drop(['부가기호','Unnamed: 13'], axis=1)
ns_book.head()


# In[50]:

# inplace=True -> 원본 데이터프레임을 변경 
# 리턴 : None
ndf = ns_book.drop('주제분류번호', axis=1, inplace=True)
ns_book.head()

'''
이미 없어진 컬럼을 지우려할 떄 발생
KeyError: "['주제분류번호'] not found in axis
'''
#%%

try:
    ndf = ns_book.drop('주제분류번호', axis=1, inplace=True)
    ns_book.head()
except KeyError as e:
    colname = '주제분류번호'
    print(f"존재하지 않는 컬럼을 삭제하려 했습니다.: 컬럼({colname})")
          
          
# In[51]:

# 열에 하나라도 nan이 포함되어 있으면 칼럼을 삭제
ns_book = ns_df.dropna(axis=1)
ns_book.head()

ns_df_col_len = len(ns_df.columns) # 14
ns_book_col_len = len(ns_book.columns) # 13 # nan값이 포함된 열
ns_book_len = len(ns_book.columns) # 5  # nan값이 제외된 후의 열 



'''
   번호           ISBN  도서권수  대출건수        등록일자
0   1  9788937444319     1     0  2021-03-19
1   2  9791190123969     1     0  2021-03-19
2   3  9788968332982     1     0  2021-03-19
3   4  9788970759906     1     0  2021-03-19
4   5  9788934990833     1     0  2021-03-19
'''

# In[52]:

# 칼럼의 모든 데이터가 nan이면 칼럼을 삭제
ns_book = ns_df.dropna(axis=1, how='all')
# dropna() 매서드도 inplace=True 를 지정하여 현재 dataframe을 수정할 수 있다.
ns_book.head()
ns_book_len1 = len(ns_book.columns) # 13

# ## 행 삭제하기

# In[53]:

# 행의 인덱스 0,1 삭제
# axis : 0(행), 기본값
ns_book2 = ns_book.drop([0,1])
ns_book2.head()


# In[54]:
# 슬라이싱
# 행선택: 2행부터 끝까지

ns_book2 = ns_book[2:]
ns_book2.head() # 401680


# In[55]:

# 슬라이스는 끝 번호가 포함되지 않음: 0,1 행 선택
ns_book2 = ns_book[0:2]
ns_book2.head()


# In[56]:

# column('출판사')의 값이 '한빛미디어'인 행을 선택: boolean array
# 결과 : series(True, False) 
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

#%%
#중복된 행 찾기
# DataFrame.duplicated()메서드 
# - 중복된 행 중에서 처음 행을 제외한 나머지 행을 True
# - 그 외에 중복(x) 모든 행을 False
# 전체 칼럼을 기준으로 중복되는 행
'''
subset: 중복을 검사할 때 고려해야 할 열 또는 열의 목록입니다. 이 매개변수를 사용하면 
특정 열 또는 열의 조합에서 중복을 찾을 수 있습니다.

keep: 중복된 행을 처리하는 방법을 지정합니다. 가능한 옵션은 다음과 같습니다:
# keep=first/last/False/inplace
'first': 처음 발견된 행을 유지하고 나머지는 제거합니다.
'last': 마지막으로 발견된 행을 유지하고 나머지는 제거합니다.
False: 모든 중복된 행을 제거합니다.
inplace: 기본값은 False이며, 이 경우 중복 제거된 결과를 반환합니다.
 inplace=True로 설정하면 DataFrame이나 Series 자체가 변경됩니다.
sum(ns_book.duplicated()) # 0
'''

# In[60]:

# 칼럼이 '도서명','저자','ISBN'에서 중복되는 행
dup_rowsT = sum(ns_book.duplicated(subset=['도서명','저자','ISBN']))

# 22096
#%%
# index : 13456, 89933  
    
bklst = [13456, 89933]
dulst = ['번호','도서명','저자','ISBN']
ns_book.loc[bklst, dulst]
'''
    번호       도서명           저자           ISBN
13456  13457   인조이 칭다오   정태관.전현진 지음  9791161658834
89933  89934  #진로스타그램   청년기획단 너랑 지음  9791157232703
'''


           

# In[61]:
# - 중복된 행 중에서 처음 행을 제외한 나머지 행을 True
# - 그 외에 중복(x) 모든 행을 False
# keep=False 중복된 행을 모두 True로 표시한 boolean

# dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN'], keep=True)
# ValueError: keep must be either "first", "last" or False

dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN'], keep=False)
ns_book3 = ns_book[dup_rows]
ns_book3.head()
# subset 즉 해당하는 열 목록안에 중복된 것만 추출

# In[62]:


count_df = ns_book[['도서명','저자','ISBN','권','대출건수']]


# In[63]:
# groupby()
# by : 그룹핑을 할 컬럼 ,['도서명','저자','ISBN','권'] (행을 합칠 떄 기준이 되는 열지정)
# dropna : NaN 포함유무
# 결과 : DataFrameGroupBy의 객체
# dropna=False : NaN이 있는 행을 유지

group_df = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False)
loan_count = group_df.sum()


# In[64]:

# head()매서드로 df출력하면 기준인 인덱스 열(즉 by값)은 굵게 표시됨.
loan_count = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False).sum()
loan_count.head()
# loan_count df는 네개의 인덱스이고 각 책의 대출건수를 더한 결과가 대출건수 열에 저장.

# In[65]:

# 1. duplicated()로 boolean array 를 생성(중복된 행은 True 표시)
dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN','권'])
unique_rows = ~dup_rows # 2. ~연산자는 boolean array를 반전 시킬 떄 사용 -> 중복되지
# 않은 고유의 행을 True표시
ns_book3 = ns_book[unique_rows].copy() # 2에서 구한 array를 사용해 원본배열에서 고유한 행만 선택.


# In[66]:


sum(ns_book3.duplicated(subset=['도서명','저자','ISBN','권'])) # 0


# In[67]:


ns_book3.set_index(['도서명','저자','ISBN','권'], inplace=True) # 4개열을 index로 지정
ns_book3.head() 


# In[68]:

# 다른 df를 사용해 원본df의 값을 업데이트 할 떄 
ns_book3.update(loan_count)
ns_book3.head()


# In[69]:


ns_book4 = ns_book3.reset_index()
ns_book4.head()


# In[70]:


sum(ns_book['대출건수']>100) # 2311


# In[71]:


sum(ns_book4['대출건수']>100) #  2550


# In[72]:


ns_book4 = ns_book4[ns_book.columns]
ns_book4.head()


# In[73]:


ns_book4.to_csv('./data/ns_book4.csv', index=False)


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

#위의 순차적으로 처리한 결과와 함수 data_cleaning()를 활용하여 처리한 값의 결과가 같아 True 값 린턴
new_ns_book4 = data_cleaning('./data/ns_202104.csv')

ns_book4.equals(new_ns_book4) # True

