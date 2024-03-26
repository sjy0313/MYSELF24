# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:02:48 2024

@author: Shin
"""

# ## 8.5 야후 파이낸스에서 주식 데이터 가져오기

# ### 8.5.1 설치 및 기본 사용법

# ### 8.5.2 미국 주식 데이터 가져오기

# [8장: 411페이지]

# In[ ]:


import yfinance as yf

ticker_symbol = "TSLA" # 테슬라 주식 심볼
ticker_data = yf.Ticker(ticker_symbol)

# 해당 종목의 정보 가져오기
# ticker_data.info

df = ticker_data.history(period='5d') # 5일분의 데이터
df


# [8장: 412페이지]

# In[ ]:

# 한 달 데이터를 일 단위로      #month       # day
df = ticker_data.history(period='1mo', interval='1d',start='2022-04-18', end='2022-04-22')
df


# [8장: 413페이지]

# In[ ]:


df = ticker_data.history(start='2022-04-18', end='2022-04-23') # start와 end 모두 지정
# df = ticker_data.history(start='2022-04-18') # start만 지정
df


# In[ ]:


import datetime

start_p = datetime.datetime(2021,5,24) # 시작일 지정
end_p = datetime.datetime(2021,5,29)   # 종료일 지정

df = ticker_data.history(start=start_p, end=end_p) # start와 end 모두 지정
df


# ### 8.5.3 국내 주식 데이터 가져오기

# [8장: 414페이지]

# In[ ]:


import pandas as pd

#----------------------------------------------------
# 한국 주식의 종목 이름과 종목 코드를 가져오는 함수
#----------------------------------------------------
def get_stock_info(maket_type=None):
    # 한국거래소(KRX)에서 전체 상장법인 목록 가져오기
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&marketType=kosdaqMKT"
   
    method = "download"
    if maket_type == 'kospi':
        marketType = "stockMkt"  # 주식 종목이 코스피인 경우
    elif maket_type == 'kosdaq':
        marketType = "kosdaqMkt" # 주식 종목이 코스닥인 경우
    elif maket_type == None:
        marketType = ""
    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)
# ch6 webscraping03-stock line63 참조
    df = pd.read_html(url, header=0, encoding='euc-kr')[0]
    
    # 종목코드 열을 6자리 숫자로 표시된 문자열로 변환
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}") 
    
    # 회사명과 종목코드 열 데이터만 남김
    df = df[['회사명','종목코드']]
    
    return df


# [8장: 415페이지]

# In[ ]:


def get_ticker_symbol(company_name, maket_type):
    """
    ----------------------------------------------------
      yfinance에 이용할 Ticker 심볼을 반환하는 함수
    ----------------------------------------------------
    """
    df = get_stock_info(maket_type)
    code = df[df['회사명']==company_name]['종목코드'].values
    code = code[0]
    
    if maket_type == 'kospi':
        ticker_symbol = code +".KS" # 코스피 주식의 심볼
    elif maket_type == 'kosdaq':
        ticker_symbol = code +".KQ" # 코스닥 주식의 심볼
    
    return ticker_symbol


# In[ ]:


import yfinance as yf

ticker_symbol = get_ticker_symbol("삼성전자", "kospi") # 삼성전자, 주식 종류는 코스피로 지정
ticker_data = yf.Ticker(ticker_symbol)

df = ticker_data.history(start='2022-06-13', end='2022-06-18') # 시작일과 종료일 지정
# df = ticker_data.history(period='5d') # 기간을 지정


df
#%%
# 인덱스 날짜 포멧 조정 
from datetime import datetime
'''
df = df.reset_index() # 인덱스를 칼럼으로 이동
df['Date'] = df['Date'].dt.strftime("%Y-%m-%d")
df = df.set_index("Date") # 칼럼을 인덱스로 이동
'''
# S02-Web_API-RSS.py line120 참조
ndf = df.reset_index()
print(ndf)
sr = ndf.iloc[:,0]
sr
'''
0   2022-06-13 00:00:00+09:00
1   2022-06-14 00:00:00+09:00
2   2022-06-15 00:00:00+09:00
3   2022-06-16 00:00:00+09:00
4   2022-06-17 00:00:00+09:00
Name: Date, dtype: datetime64[ns, Asia/Seoul]
'''
date = sr.loc[0]
date #  Timestamp('2022-06-13 00:00:00+0900', tz='Asia/Seoul')
dl = date.strftime("%Y-%m-%d")
dl = '2022-06-13' 

# sr.split()[0] split() method는 string class의 메서드로서 활용가능하므로 
# strftime()를 활용하여 string으로 변환시킨 뒤 split을 활용할 수 있다.

nx = 0 
dl = '2022-06-13' 
dx2= dl.split('-')[0]
dx1= dl.split('-')[1]
dx = dl.split('-')[2]

dy = print(f"{dx2}-{dx1}-{dx}")

def get_local_date(day):
    # 주어진 날짜 문자열을 datetime 객체로 변환
    dt = datetime.strptime("2022-06-{}".format(day), "%Y-%m-%d")
    # datetime 객체를 원하는 포맷으로 변환하여 반환
    formatted_date = dt.strftime("%Y-%m-%d")
    return formatted_date

# 함수 호출
formatted_date = get_local_date(18)
print(formatted_date)


'''
ndf = df.reset_index()
ndf['Date'] = ndf['Date'].apply(get_local_date)

'''

from datetime import datetime, timedelta

# RSS 피드 제공 일시를 한국 날짜와 시간으로 변경 하는 함수
def get_local_datetime(rss_datetime):
    # 전체 값 중에서 날짜와 시간만 문자열로 추출
    date_time_str = ' '.join(rss_datetime.split()[1:5])
# debug(break)ing 통한 추적 F12    
    # 문자열의 각 자리에 의미를 부여해 datetime 객체로 변경
    date_time_GMT = datetime.strptime(date_time_str, '%d %b %Y %H:%M:%S')
    
    # GMT에 9시간을 더해 한국 시간대로 변경
    date_time_KST = date_time_GMT + timedelta(hours=9)
    
    return date_time_KST # 변경된 시간대의 날짜와 시각 반환

# [8장: 416페이지]

# In[ ]:


excel_file_name = "D:\WORKSPACE(SHIN)\Python\WebScraping\Web-API\your_excel_file.xlsx" # 엑셀 파일 이름 지정
df.to_excel(excel_file_name)
# 파일위치 + \원하는 액셀 파일 이름.xlsx
print("생성 파일:", excel_file_name)


# ### 8.5.4 여러 주식 데이터 가져오기

# [8장: 417페이지]

# In[ ]:


ticker_symbols = "MSFT" # 마이크로소프트 주식 심볼
# ticker_symbols = ["MSFT"] # 리스트도 지정해도 됨
df = yf.download(ticker_symbols, start="2020-01-01", end="2022-01-01")
df.tail()


# In[ ]:


# 그래프 그리기
import matplotlib.pyplot as plt

df['Close'].plot(grid=True, figsize=(15, 5), title="Microsoft")
plt.show()


# [8장: 418페이지]

# In[ ]:


ticker_symbols = ["GOOG", "AAPL"] # 주식 심볼 리스트(구글, 애플)
df = yf.download(ticker_symbols,  start="2020-01-01", end="2022-01-01")
df.tail()


# In[ ]:


# 그래프 그리기
import matplotlib.pyplot as plt

df['Close'].plot(grid=True, figsize=(15, 5))
plt.show()


# [8장: 419페이지]

# In[ ]:


# 그래프 그리기
df['Close'].plot(grid=True, figsize=(15, 5), subplots=True, layout=(2,1))
plt.show()


# ## 8.6 정리