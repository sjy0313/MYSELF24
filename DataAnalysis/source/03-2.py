import numpy as np
import pandas as pd

ns_book4 = pd.read_csv('./data/ns_book4.csv', low_memory=False)
ns_book4.head()


ns_book4.replace({'부가기호': {np.nan: '없음'}, '발행년도': {'2021': '21'}}).head(2)

# ## 정규 표현식 (jumptopython 맨뒤에 있음)
# regular expression 패턴을 찾아서 대체하기 위한 규칙의 모음.
# In[ ]:


ns_2021 = ns_book4.replace({'발행년도': {'2021': '21'}})[100:102]

# ns_book4.replace({'발행년도': {'2021': '21'}})[100:102] # 안바뀜

# In[ ]:
# 정규표현식에서 \d의 의미는 숫자 -> \d\d\d\d 네자리 연도 -> 그룹으로 묶을 떄 ()사용
#99(99) -> (99)
#12(34) -> (34) 괄호로 묶은 첫번 쨰 그룹
# r'\1' : 괄호에 묶은 첫번 쨰 그룹
# regex -> 정규표현식을 사용한다는 의미
ns_99 = ns_book4.replace({'발행년도': {r'\d\d(\d\d)': r'\1'}}, regex=True)[100:102]


# In[ ]:
# r'\d{2}(\d{2})' : 숫자2자리, 숫자2자리(그룹1) d{2}(\d{2} = \d\d(\d\d) 같은 의미
# {} : 정규표현식에서 숫자가 여러 번 반복될 떄 사용
# r'\1' : 그룹1 if \2는 그룹 2 

ns_22 = ns_book4.replace({'발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102]


# In[ ]:

# 문자 찾기: 마침표(.) 어떤 문자에도 대응하는 표현식문자
# (*) : 임의의 문자가 0개 이상 문자가 반복됨을 알림 
# \s : 공백 space
# \( : '('
# \) : ')'
ns_22 = ns_book4.replace({'저자': {r'(.*)\s\(지은이\)(.*)\s\(옮긴이\)': r'\1\2'},
                  '발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102]
'''
	저자
100	헨리 클라우드, 존 타운센드, 김진웅
101	로런스 인그래시아, 안기순

'''

# ## 잘못된 값 바꾸기

# # In[ ]:


# 아래 코드는 오류 발생
# ns_book4.astype({'발행년도': 'int32'})


# In[ ]:
# contains()는 정규 표현식을 인식 

ns_book4['발행년도'].str.contains('1988').sum()
# 407

# In[ ]:

# 정규표현식 : \D는 \d 의 반대로 즉, 숫자가 아닌 것.  
# na매개변수를 True로 지정하여 연도가 누락된 행을 True로 표시 
# if, 발행년도'에 누락된 값이 있다면 contains()는 np.nan으로 채워서 ivalid_number
# 에 배열을 사용x
invalid_number = ns_book4['발행년도'].str.contains('\D', na=True)
print(invalid_number.sum()) # 1777
ns_book4[invalid_number].head() 
'''
         번호                       도서명  ... 대출건수        등록일자
19138  19565                      단국강토  ...  1.0  2019-12-19
19227  19736                    삼성의 역사  ...  1.0  2019-12-06
26097  26812                  배고픈 애벌레   ...  0.0  2019-08-12
29817  30586  (The) Sopranos sessions   ...  0.0  2019-06-13
29940  30709                    다음엔 너야  ...  9.0  2019-06-04
'''


# In[ ]:

# 숫자그룹 앞뒤로 * 를 묶어주어 어떤 문자가 나오더라도 모두 매칭시키기 위해.
ns_book5 = ns_book4.replace({'발행년도':r'.*(\d{4}).*'}, r'\1', regex=True)
ns_book5[invalid_number].head()


# In[ ]:

# \D 문자 인 것들과 그외에 na값들을 출력 
unkown_year = ns_book5['발행년도'].str.contains('\D', na=True)
print(unkown_year.sum())# 67
ns_book5[unkown_year].head()


# In[ ]:

# 임의로 -1로 바꾸어 준 ㅏㄷ음 
ns_book5.loc[unkown_year, '발행년도'] = '-1'
ns_book5 = ns_book5.astype({'발행년도': 'int32'})
 

# In[ ]:

# 연도가 4000이 넘는 행의 개수
# gt()는 전달된 값보다 큰 값을 찾는 매서드
ns_book5['발행년도'].gt(4000).sum() # 131


# In[ ]:

# 4000 - 2333 서기로 바꾼다음 4000이 넘는 도서찾기 
dangun_yy_rows = ns_book5['발행년도'].gt(4000)
ns_book5.loc[dangun_yy_rows, '발행년도'] = ns_book5.loc[dangun_yy_rows, '발행년도'] - 2333


# In[ ]:


dangun_year = ns_book5['발행년도'].gt(4000) 
print(dangun_year.sum()) 
ns_book5[dangun_year].head(2)


# In[ ]:


ns_book5.loc[dangun_year, '발행년도'] = -1 


# In[ ]:

# 0<발행연도<1900
old_books = ns_book5['발행년도'].gt(0) & ns_book5['발행년도'].lt(1900)
ns_book5[old_books]


# In[ ]:


ns_book5.loc[old_books, '발행년도'] = -1


# In[ ]:


ns_book5['발행년도'].eq(-1).sum() # 86


# ## 누락된 정보 채우기

# In[ ]:


na_rows = ns_book5['도서명'].isna() | ns_book5['저자'].isna() \
          | ns_book5['출판사'].isna() | ns_book5['발행년도'].eq(-1)
print(na_rows.sum())   # 5380
ns_book5[na_rows].head(2) 


# In[ ]:


# DH_KEY_TOO_SMALL 에러가 발생하는 경우 다음 코드의 주석을 제거하고 실행하세요.
# https://stackoverflow.com/questions/38015537/python-requests-exceptions-sslerror-dh-key-too-small
# import requests

# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
# try:
#     requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
# except AttributeError:
#     # no pyopenssl support used / needed / available
#     pass


# In[ ]:


import requests
from bs4 import BeautifulSoup


# In[ ]:


def get_book_title(isbn):
    # Yes24 도서 검색 페이지 URL
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져옵니다.
    r = requests.get(url.format(isbn))
    soup = BeautifulSoup(r.text, 'html.parser')   # HTML 파싱
    # 클래스 이름이 'gd_name'인 a 태그의 텍스트를 가져옵니다.
    title = soup.find('a', attrs={'class':'gd_name'}) \
            .get_text()
    return title


# In[ ]:


get_book_title(9791191266054) # '골목의 시간을 그리다'


# In[ ]:


import re

def get_book_info(row):
    title = row['도서명']
    author = row['저자']
    pub = row['출판사']
    year = row['발행년도']
    # Yes24 도서 검색 페이지 URL
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져옵니다.
    r = requests.get(url.format(row['ISBN']))
    soup = BeautifulSoup(r.text, 'html.parser')   # HTML 파싱
    try:
        if pd.isna(title):
            # 클래스 이름이 'gd_name'인 a 태그의 텍스트를 가져옵니다.
            title = soup.find('a', attrs={'class':'gd_name'}) \
                    .get_text()
    except AttributeError:
        pass

    try:
        if pd.isna(author):
            # 클래스 이름이 'info_auth'인 span 태그 아래 a 태그의 텍스트를 가져옵니다.
            authors = soup.find('span', attrs={'class':'info_auth'}) \
                          .find_all('a')
            author_list = [auth.get_text() for auth in authors]
            author = ','.join(author_list)
    except AttributeError:
        pass

    try:
        if pd.isna(pub):
            # 클래스 이름이 'info_auth'인 span 태그 아래 a 태그의 텍스트를 가져옵니다.
            pub = soup.find('span', attrs={'class':'info_pub'}) \
                      .find('a') \
                      .get_text()
    except AttributeError:
        pass

    try:
        if year == -1:
            # 클래스 이름이 'info_date'인 span 태그 아래 텍스트를 가져옵니다.
            year_str = soup.find('span', attrs={'class':'info_date'}) \
                           .get_text()
            # 정규식으로 찾은 값 중에 첫 번째 것만 사용합니다.
            year = re.findall(r'\d{4}', year_str)[0]
    except AttributeError:
        pass

    return title, author, pub, year


# In[ ]:

# 샘플테스트
# result_type = 'expand' : get_book_info()로 부터 반환 된 리턴 값을 
# 각기 다른 열로 만듬
updated_sample = ns_book5[na_rows].head(2).apply(get_book_info,
    axis=1, result_type ='expand')
updated_sample


# 아래 코드 셀은 실행하는데 시간이 오래 걸립니다. 편의를 위해 실행한 결과를 저장해 놓은 CSV 파일을 사용하겠습니다.

# In[ ]:


# ns_book5_update = ns_book5[na_rows].apply(get_book_info,
#     axis=1, result_type ='expand')

# ns_book5_update.columns = ['도서명','저자','출판사','발행년도']
# ns_book5_update.head()


# In[ ]:


gdown.download('http://bit.ly/3UJZiHw', 'ns_book5_update.csv', quiet=False)

ns_book5_update = pd.read_csv('ns_book5_update.csv', index_col=0)
ns_book5_update.head()


# In[ ]:


ns_book5.update(ns_book5_update)

na_rows = ns_book5['도서명'].isna() | ns_book5['저자'].isna() \
          | ns_book5['출판사'].isna() | ns_book5['발행년도'].eq(-1)
print(na_rows.sum())


# In[ ]:


ns_book5 = ns_book5.astype({'발행년도': 'int32'})


# In[ ]:


ns_book6 = ns_book5.dropna(subset=['도서명','저자','출판사'])
ns_book6 = ns_book6[ns_book6['발행년도'] != -1]
ns_book6.head()


# In[ ]:


ns_book6.to_csv('ns_book6.csv', index=False)


# In[ ]:


def data_fixing(ns_book4):
    """
    잘못된 값을 수정하거나 NaN 값을 채우는 함수

    :param ns_book4: data_cleaning() 함수에서 전처리된 데이터프레임
    """
    # 도서권수와 대출건수를 int32로 바꿉니다.
    ns_book4 = ns_book4.astype({'도서권수':'int32', '대출건수': 'int32'})
    # NaN인 세트 ISBN을 빈문자열로 바꿉니다.
    set_isbn_na_rows = ns_book4['세트 ISBN'].isna()
    ns_book4.loc[set_isbn_na_rows, '세트 ISBN'] = ''

    # 발행년도 열에서 연도 네 자리를 추출하여 대체합니다. 나머지 발행년도는 -1로 바꿉니다.
    ns_book5 = ns_book4.replace({'발행년도':'.*(\d{4}).*'}, r'\1', regex=True)
    unkown_year = ns_book5['발행년도'].str.contains('\D', na=True)
    ns_book5.loc[unkown_year, '발행년도'] = '-1'

    # 발행년도를 int32로 바꿉니다.
    ns_book5 = ns_book5.astype({'발행년도': 'int32'})
    # 4000년 이상인 경우 2333년을 뺍니다.
    dangun_yy_rows = ns_book5['발행년도'].gt(4000)
    ns_book5.loc[dangun_yy_rows, '발행년도'] = ns_book5.loc[dangun_yy_rows, '발행년도'] - 2333
    # 여전히 4000년 이상인 경우 -1로 바꿉니다.
    dangun_year = ns_book5['발행년도'].gt(4000)
    ns_book5.loc[dangun_year, '발행년도'] = -1
    # 0~1900년 사이의 발행년도는 -1로 바꿉니다.
    old_books = ns_book5['발행년도'].gt(0) & ns_book5['발행년도'].lt(1900)
    ns_book5.loc[old_books, '발행년도'] = -1

    # 도서명, 저자, 출판사가 NaN이거나 발행년도가 -1인 행을 찾습니다.
    na_rows = ns_book5['도서명'].isna() | ns_book5['저자'].isna() \
              | ns_book5['출판사'].isna() | ns_book5['발행년도'].eq(-1)
    # 교보문고 도서 상세 페이지에서 누락된 정보를 채웁니다.
    updated_sample = ns_book5[na_rows].apply(get_book_info,
        axis=1, result_type ='expand')
    updated_sample.columns = ['도서명','저자','출판사','발행년도']
    ns_book5.update(updated_sample)

    # 도서명, 저자, 출판사가 NaN이거나 발행년도가 -1인 행을 삭제합니다.
    ns_book6 = ns_book5.dropna(subset=['도서명','저자','출판사'])
    ns_book6 = ns_book6[ns_book6['발행년도'] != -1]

    return ns_book6

