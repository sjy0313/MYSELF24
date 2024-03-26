# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:08:51 2024

@author: Shin
"""

# ## 8.3 RSS 피드 데이터 가져오기

# ### 8.3.1 RSS 문서의 구조 및 데이터 추출

# [8장: 353페이지]

# In[ ]:


rss_simple_document = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>파이썬 웹 스크레이핑 홈페이지</title>
  <link>https://www.python_web_scraping.com</link>
  <description>파이썬 웹 스크레이핑 설명</description>
  <pubDate>Sat, 30 Apr 2022 15:39:19 GMT</pubDate>
  <lastBuildDate>Sat, 30 Apr 2022 17:50:21 GMT</lastBuildDate>
  <item>
    <title>1장. 웹 스크레이핑</title>
    <link>https://www.python_web_scraping.com/web_scraping.html</link>
    <description>웹 스크레이핑 기본에 관한 교육</description>
    <pubDate>Sat, 30 Apr 2022 00:30:00 GMT</pubDate>
  </item>
  <item>
    <title>2장. 웹 API 교육</title>
    <link>https://www.python_web_scraping.com/web_api.html</link>
    <description>웹 API에 관한 교육</description>
    <pubDate>Sat, 30 Apr 2022 09:45:12 GMT</pubDate>
  </item>
</channel>

</rss>"""


# [8장: 355페이지]
# RSS(Really Simple Syndication, Rich Site Summary) : 
# 사이트에 신규로 등록되는 최신 콘텐츠에 대한 요약된 정보를 빠르게 제공하기 위한 포맷
# parsing : 텍스트나 데이터를 해석하고 분석하는 과정을 가리킵니다.
# 이 용어는 특히 프로그래밍에서 파일이나 문서 등의 구조화되지 않은 데이터를 읽고 
# 이해하는 과정을 설명하는 데 사용(데이터 추출)
# In[ ]:

# pip install feedparser 웹 사이트의 컨텐츠를 구독하고 새로운 콘텐츠를 읽어오는 데 사용되는 피드 형식입니다.
import feedparser
# feed = feedparser.parse(url) 피드 읽기

d = feedparser.parse(rss_simple_document) # RSS 형식의 데이터를 파싱
# d.feed.() 
d.feed.title, d.feed.link, d.feed.description, d.feed.published, d.feed.updated
'''
('파이썬 웹 스크레이핑 홈페이지',
 'https://www.python_web_scraping.com',
 '파이썬 웹 스크레이핑 설명',
 'Sat, 30 Apr 2022 15:39:19 GMT',
 'Sat, 30 Apr 2022 17:50:21 GMT')
'''

# In[ ]:

# d.feed.title, d.feed.link, d.feed.description, d.feed.published, d.feed.updated
# 위와 같음.
d["feed"]["title"], d["feed"]["link"], d["feed"]["description"], d["feed"]["published"], d["feed"]["updated"]
'''
('파이썬 웹 스크레이핑 홈페이지',
 'https://www.python_web_scraping.com',
 '파이썬 웹 스크레이핑 설명',
 'Sat, 30 Apr 2022 15:39:19 GMT',
 'Sat, 30 Apr 2022 17:50:21 GMT')
'''

# [8장: 356페이지]

# In[ ]:


d.entries[0].title, d.entries[0].link, d.entries[0].description, d.entries[0].published
'''
('1장. 웹 스크레이핑',
 'https://www.python_web_scraping.com/web_scraping.html',
 '웹 스크레이핑 기본에 관한 교육',
 'Sat, 30 Apr 2022 00:30:00 GMT')
'''
# In[ ]:


d.entries[1].title, d.entries[1].link, d.entries[1].description, d.entries[1].published


# ### 8.3.2 구글 뉴스의 검색 기사 가져오기

# [8장: 358페이지]

# In[ ]:


import feedparser

query = "머신러닝"
# RSS 서비스 주소
rss_url = f'https://news.google.com/rss/search?q={query}&&hl=ko&gl=KR&ceid=KR:ko'
rss_news = feedparser.parse(rss_url) # RSS 형식의 데이터를 파싱

title = rss_news['feed']['title']
updated = rss_news['feed']['updated']

print("['구글 뉴스' RSS 피드 제목]", title) # ['구글 뉴스' RSS 피드 제목] "머신러닝" - Google 뉴스
print("['구글 뉴스' RSS 피드 제공 일시]", updated)
# ['구글 뉴스' RSS 피드 제공 일시] Tue, 26 Mar 2024 02:15:16 GMT

# In[ ]:


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


# [8장: 359페이지]

# In[ ]:

# 2024-03-26 11:15:16
print("['구글 뉴스' RSS 피드 제공 일시]", get_local_datetime(updated))
# get_local_datetime(updated))
# ['구글 뉴스' RSS 피드 제공 일시] 2024-03-26 11:15:16

# In[ ]:


import feedparser
import pandas as pd

df_gnews = pd.DataFrame(rss_news.entries) # 구글 뉴스 아이템을 판다스 DataFrame으로 변환

selected_columns = ['title', 'published', 'link'] # 관심있는 열만 선택
df_gnews2 = df_gnews[selected_columns].copy()     # 선택한 열만 다른 DataFrame으로 복사

# published 열의 작성 일시를 한국 시간대로 변경 (KST)
df_gnews2['published'] = df_gnews2['published'].apply(get_local_datetime) 
# 컬럼명.apply 위에서부터 아래로 순회하며 kst로 apply시켜줌.
df_gnews2.columns = ['제목', '제공 일시', '링크'] # 열 이름 변경
df_gnews2.head(3)                                 # 앞의 일부만 출력


# [8장: 360페이지]

# In[ ]:


from IPython.display import HTML

df = df_gnews2.head(5) # DataFrame 데이터의 일부 열과 행을 선택
# df = df_gnews2       # DataFrame 데이터 전체를 선택

html_table = df.to_html(escape=False, render_links=True) # DataFrame 데이터를 HTML 코드로 변환
HTML(html_table)  # HTML 코드의 내용을 웹 브라우저처럼 보여줌


# [8장: 361페이지]


# In[ ]:


from datetime import datetime, timedelta

google_news_datetime_KST = get_local_datetime(updated) # 한국 날짜와 시간으로 변경 
df.gnews2 = df_gnews2.sort_values(by='제공 일시', ascending=False) # 날짜 순으로 나열
df = df_gnews2.head() # DataFrame 데이터 앞의 일부
# df = df_gnews2 # DataFrame 데이터 전체

# DataFrame 데이터를 HTML 코드로 변환 (justify='center' 옵션을 이용해 열 제목을 중간에 배치)
html_table = df.to_html(justify='center', escape=False, render_links=True) 

# HTML 기본 구조를 갖는 HTML 코드
html_code = '''
<!DOCTYPE html>
<html>
  <head>
    <title>구글 뉴스 검색</title>
  </head>
  <body>
    <h1>{0}</h1>
    <h3> *검색 날짜 및 시각: {1}</h3>
    {2}
  </body>
</html>    
'''.format(title, google_news_datetime_KST, html_table)

file_name = r"D:\WORKSPACE(SHIN)\Python\WebScraping\Web-API\output.html" # 생성할 HTML 파일 이름 지정
with open(file_name, 'w', encoding="utf-8") as f:
    f.write(html_code)

#역슬래시 \를 사용할 때 문자열 리터럴 앞에 r을 붙여 raw 문자열로 처리하는 것이 좋습니다.
#그렇지 않으면 백슬래시가 이스케이프 문자로 처리될 수 있습니다.
#마지막으로, 파일 이름에 HTML 파일의 확장자인 .html을 추가하는 것이 좋습니다.

print("생성한 파일:", file_name)
