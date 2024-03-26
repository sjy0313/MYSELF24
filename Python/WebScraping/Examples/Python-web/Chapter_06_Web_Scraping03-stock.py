
# ### 6.2.3 환율 정보 가져오기

# #### 현재의 환율 정보 가져오기

# [6장: 259페이지]

# In[ ]:

from bs4 import BeautifulSoup

# Specify the parser explicitly

# Assuming 'html_content' contains your HTML content
html_content = "<html><body><p>Hello, world!</p></body></html>"

soup = BeautifulSoup(html_content, 'html5lib')

import pandas as pd

# 환율  query = 환율 (임을 인지)
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'

# url에서 표 데이터를 추출해 DataFrame 데이터의 리스트로 반환
dfs = pd.read_html(url)
dfs


# [6장: 260페이지]

# In[ ]:


len(dfs)


# In[ ]:


dfs[0]


# In[ ]:


exchange_rate_df = dfs[0].replace({'전일대비상승': '▲', 
                                   '전일대비하락': '▼'}, regex=True)
exchange_rate_df


# [6장: 262페이지]

# In[ ]:
import requests
import pandas as pd

# 네이버 금융의 환율 정보 웹 사이트 주소
url = 'https://finance.naver.com/marketindex/exchangeList.nhn' 
# url의 f12 source code에서 charset에 encoding을 확인하고 읽어올 떄 명시해
pd.read_html(url, encoding='euc-kr')

# 웹 사이트의 표 데이터에서 두 번째 줄을 DataFrame 데이터의 columns로 선택
dfs = pd.read_html(url, header=1, encoding='euc-kr') 

dfs[0].head() # 전체 데이터 중 앞의 일부분만 표시
'''
             통화명    매매기준율     사실 때     파실 때    보내실 때    받으실 때  미화환산율
0         미국 USD  1339.50  1362.94  1316.06  1352.60  1326.40  1.000
1       유럽연합 EUR  1450.41  1479.27  1421.55  1464.91  1435.91  1.083
2  일본 JPY (100엔)   884.51   899.98   869.04   893.17   875.85  0.660
3         중국 CNY   184.39   193.60   175.18   186.23   182.55  0.138
4         홍콩 HKD   171.34   174.71   167.97   173.05   169.63  0.128
'''

# #### 과거의 환율 정보 가져오기

# [6장: 264페이지]

# In[ ]:


import pandas as pd

base_url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn"
currency_code = "FX_USDKRW" # 통화 코드
page_num = 1
# https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?&page=1
url = f"{base_url}?marketindexCd={currency_code}&page={page_num}"
dfs = pd.read_html(url, header=1, encoding='euc-kr' )

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6): 
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(dfs[0])
    
# ?: 문자열 구분자. 
# &: 파라미터 구분자.

# [6장: 265페이지]

# In[ ]:


import pandas as pd
import time

# 날짜별 환율 데이터를 반환하는 함수
# - 입력 인수: currency_code(통화코드), last_page_num(페이지 수)
# - 반환: 환율 데이터
def get_exchange_rate_data(currency_code, last_page_num):
    base_url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn"

    df = pd.DataFrame()
# df와 dfs의 concat
    for page_num in range(1, last_page_num+1):
        url = f"{base_url}?marketindexCd={currency_code}&page={page_num}"
        dfs = pd.read_html(url, header=1, encoding='euc-kr')

        if dfs[0].empty: # 통화 코드가 잘못 지정됐거나 마지막 페이지의 경우 for 문을 빠져나오기 위한 코드
            if (page_num==1):
                print(f"통화 코드({currency_code})가 잘못 지정됐습니다.")
            else:
                print(f"{page_num}가 마지막 페이지입니다.")
            break

        df = pd.concat([df, dfs[0]], ignore_index=True) # page별로 가져온 DataFrame 데이터 연결
        time.sleep(0.1) # 0.1초간 멈춤
        
    return df


# [6장: 266페이지]

# In[ ]:


df_usd = get_exchange_rate_data('FX_USDKRW', 2)

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6):
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(df_usd)
    '''
 날짜   매매기준율  전일대비  ...     파실 때   보내실 때   받으실 때
0   2024.03.22  1338.5   7.0  ...  1315.08  1351.6  1325.4
1   2024.03.21  1331.5   9.0  ...  1308.20  1344.5  1318.5
..         ...     ...   ...  ...      ...     ...     ...
18  2024.02.26  1332.0   0.5  ...  1308.69  1345.0  1319.0
19  2024.02.23  1332.5   3.5  ...  1309.19  1345.5  1319.5
'''
# [6장: 267페이지]

# In[ ]:


df_eur = get_exchange_rate_data('FX_EURKRW', 1)

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6):
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(df_eur.head())


