# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:08:03 2024

@author: Shin
"""

n/env python
# coding: utf-8

# # 6장 웹 스크레이핑

# ## 6.1 웹 스크레이핑을 위한 기본 지식

# ### 6.1.1 웹 스크레이핑의 과정

# ### 6.1.2 웹 스크레이핑 시 주의 사항

# #### 주요 주의 사항

# #### 웹 사이트 이용 규약

# ### 6.1.3 웹 데이터의 요청과 응답 과정

# ### 6.1.4 웹 페이지 언어(HTML) 구조

# [6장: 215페이지]

# Visual studio code 에서 나만의 html 만들기
# 새파일 만들기 
# ! enter
# body에 내용 추가 <h1>큰 글꼴<h1> 
# 나의 ip주소 알아보기 
# ipconfig 
#  IPv4 주소 . . . . . . . . . : 192.168.71.233

# HTML 개념
# https://developer.mozilla.org/ko/docs/Web/HTML

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\data\\ch06\\HTML_example.html', '<!doctype html>\n<html>\n <head>\n  <meta charset="utf-8">\n  <title>이것은 HTML 예제</title>\n </head>\n <body>\n  <h1>출간된 책 정보</h1>\n  <p id="book_title">이해가 쏙쏙 되는 파이썬</p>\n  <p id="author">홍길동</p>\n  <p id="publisher">위키북스 출판사</p>\n  <p id="year">2018</p>\n </body>\n</html>\n')


# [6장: 216페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/data/ch06/HTML_example2.html', '<!doctype html>\n<html>\n <head>\n  <meta charset="utf-8">\n  <title>이것은 HTML 예제</title>\n </head>\n <body>\n  <h1>출간된 책 정보</h1>\n  <p>이해가 쏙쏙 되는 파이썬</p>\n  <p>홍길동</p>\n  <p>위키북스 출판사</p>\n  <p>2018</p>\n  </body>\n</html>\n')


# ### 6.1.5 웹 페이지의 소스 가져오기

# #### 웹 브라우저로 웹 페이지 소스 보기

# ####  requests 라이브러리 활용

# ####  GET 메서드로 웹 사이트의 소스 가져오기

# [6장: 220페이지]

# In[ ]:

# 웹 사이트 소스 가져오기
import requests
# r = Response
r = requests.get("https://www.google.co.kr")
r # <Response [200]>
# get(url: Union[Text, bytes]

# In[ ]:
# https://developer.mozilla.org/ko/docs/Web/HTTP/Status
# HTTP 상태코드
r.status_code # 200 # 요청이 성공적으로 되었습니다.
# 500 서버애러 / # 400 보안애러(인증)

# 전화
# TCP (전송 제어 프로토콜)**은 두 개의 호스트를 연결하고 
#데이터 스트림을 교환하게 해주는 중요한 네트워크 프로토콜

#우편
# 사용자 데이터그램 프로토콜 (User Datagram Protocol, UDP) 은 
#보안과 신뢰성보다 전송 속도와 효율성이 더 중요한 경우 데이터를 
#전송하기 위해 IP과 함께 오래 사용된 프로토콜

# [6장: 221페이지]

# In[ ]:


r.text[0:100]
# '<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"
# lang="ko"><head><meta content'

# In[ ]:


r.headers


# In[ ]:


import requests

html = requests.get("https://www.google.co.kr").text
html[0:100]


# ### 6.1.6 웹 페이지의 소스 분석하고 처리하기

# #### 데이터 찾고 추출하기

# [6장: 222페이지]

# In[ ]:


from bs4 import BeautifulSoup
# pip install bs4 
# pip install lxml
# 테스트용 html 소스
# </a> hyperlink 
html = """<html><body><div><span>\
        <a href=http://www.naver.com>naver</a>\
        <a href=https://www.google.com>google</a>\
        <a href=http://www.daum.net/>daum</a>\
        </span></div></body></html>""" 

# BeautifulSoup를 이용해 HTML 소스를 파싱
soup = BeautifulSoup(html, 'lxml') 
soup


# In[ ]:


print(soup.prettify())
'''
<html>
 <body>
  <div>
   <span>
    <a href="http://www.naver.com">
     naver
    </a>
    <a href="https://www.google.com">
     google
    </a>
    <a href="http://www.daum.net/">
     daum
    </a>
   </span>
  </div>
 </body>
</html>
'''

# [6장: 224페이지]

# In[ ]:

# 태그찾기 : 첫 번쨰 태그리턴(속성값 접근)
a1 = soup.find('a') # <a href="http://www.naver.com">naver</a>
print(type(a1),a1) #<class 'bs4.element.Tag'>
print(a1['href']) # http://www.naver.com
print(a1.get('href')) # http://www.naver.com
# In[ ]:


soup.find('a').get_text() # 'naver'


# In[ ]:


soup.find('a')['href'] # soup.find('a').get('href') 도 동일


# [6장: 225페이지]

# In[ ]:


soup.find_all('a')
'''
[<a href="http://www.naver.com">naver</a>,
 <a href="https://www.google.com">google</a>,
 <a href="http://www.daum.net/">daum</a>]
'''

# In[ ]:

# 모든 테그('a')의 텍스트를 리스트 객체로 생성 
[x.get_text() for x in soup.find_all('a')]
['naver', 'google', 'daum']

# In[ ]:


from bs4 import BeautifulSoup

# 테스트용 HTML 코드
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
  </body>
</html>
""" 

soup2 = BeautifulSoup(html2, "lxml")


# [6장: 226페이지]

# In[ ]:


soup2.title # <title>작품과 작가 모음</title>


# In[ ]:


soup2.body
'''
<body>
<h1>책 정보</h1>
<p id="book_title">토지</p>
<p id="author">박경리</p>
<p id="book_title">태백산맥</p>
<p id="author">조정래</p>
<p id="book_title">감옥으로부터의 사색</p>
<p id="author">신영복</p>
</body>
'''

# [6장: 227페이지]

# In[ ]:


soup2.body.h1 # <h1>책 정보</h1>


# In[ ]:

# 요소가 여러 개라면 첫번 쨰 태그의 요소로 반환한다. 
soup2.p # <p id="book_title">토지</p>


# In[ ]:


soup2.find_all('p')
'''
[<p id="book_title">토지</p>,
 <p id="author">박경리</p>,
 <p id="book_title">태백산맥</p>,
 <p id="author">조정래</p>,
 <p id="book_title">감옥으로부터의 사색</p>,
 <p id="author">신영복</p>]
'''

# [6장: 228페이지]

# In[ ]:


soup2.find('p', {"id":"book_title"}) # <p id="book_title">토지</p>


# In[ ]:

# id-author 속성을 갖는 첫 번쨰 요소만 반환
soup2.find('p', {"id":"author"}) # <p id="author">박경리</p>


# In[ ]:


soup2.find_all('p', {"id":"book_title"})


# In[ ]:


soup2.find_all('p', {"id":"author"})


# In[ ]:


from bs4 import BeautifulSoup

soup2 = BeautifulSoup(html2, "lxml")

book_titles = soup2.find_all('p', {"id":"book_title"})
authors = soup2.find_all('p', {"id":"author"})
# tile하고 저자를 하나로 묶어서 택스트만 리턴
for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())

'''
토지/박경리
태백산맥/조정래
감옥으로부터의 사색/신영복
'''

# [6장: 230페이지]
# 셀렉터(selector) : CSS 선택자
# soup.select_one() : 처음 만나는 요소
# soup.select() : 모든 요소
'''
Cascading 단계별 구성 상위-> 하위로 세분화
 CSS(Cascading Style Sheet)는 HTML로 만들어진 콘텐츠에 레이아웃과 디자인요소를 정의하는 기술로
 잘 설계된 css 는 재활용이 가능하며 나아가 테마, 템플릿의 형태로 확장할 수 있습니다. 
 또한 자바스크립트와 연계해 콘텐츠의 내용이나 디자인을 동적으로 처리할 경우에도 유용하게 사용됩니다.

'''

# In[ ]:

# body의 하위 요소 가운데 최초의 h1 태그
soup2.select_one('body h1') # body 내의 h1 태그를 갖는 최초의 요소 찾기


# In[ ]:


soup2.select('body h1') # body 내의 h1 태그를 갖는 모든 요소 찾기 
#  [<h1>책 정보</h1>]

# In[ ]:


soup2.select_one('body p') # <p id="book_title">토지</p>


# In[ ]:

 # 모든 요소
soup2.select('body p')
'''
[<p id="book_title">토지</p>,
 <p id="author">박경리</p>,
 <p id="book_title">태백산맥</p>,
 <p id="author">조정래</p>,
 <p id="book_title">감옥으로부터의 사색</p>,
 <p id="author">신영복</p>]
'''
#%%
#!/usr/bi

# In[ ]:


soup2.select('p')


# [6장: 231페이지]

# In[ ]:


soup2.select('p#book_title')


# In[ ]:


soup2.select('p#author')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/data/ch06/HTML_example_my_site.html', '<!doctype html>\n<html>\n  <head>\n    <meta charset="utf-8">\n    <title>사이트 모음</title>\n  </head>\n  <body>\n    <p id="title"><b>자주 가는 사이트 모음</b></p>\n    <p id="contents">이곳은 자주 가는 사이트를 모아둔 곳입니다.</p>\n    <a href="http://www.naver.com" class="portal" id="naver">네이버</a> <br>\n    <a href="https://www.google.com" class="search" id="google">구글</a> <br>\n    <a href="http://www.daum.net" class="portal" id="daum">다음</a> <br>\n    <a href="http://www.nl.go.kr" class="government" id="nl">국립중앙도서관</a>\n  </body>\n</html>\n')


# [6장: 232페이지]

# In[ ]:


f = open('C:/myPyScraping/data/ch06/HTML_example_my_site.html', encoding='utf-8')

html3 = f.read()
f.close()

soup3 = BeautifulSoup(html3, "lxml")


# In[ ]:


soup3.select('a')


# [6장: 233페이지]

# In[ ]:


soup3.select('a.portal')


# In[ ]:


soup3.select_one('a').get_text()


# In[ ]:


[x.get_text() for x in soup3.select('a')]


# #### 웹 브라우저의 요소 검사

# [6장: 235페이지]

# In[ ]:


soup3.select('a')


# In[ ]:


soup3.select('a.portal')


# [6장: 236페이지]

# In[ ]:


soup3.select('a#naver')


# In[ ]:


soup3.select('a#naver.portal')


# In[ ]:


soup3.select('a.portal#naver')


# ### 6.1.7 웹 사이트 주소에 부가 정보 추가하기

# #### 웹 사이트 주소에 경로 추가하기

# [6장: 237페이지]

# In[ ]:


base_url = "https://api.github.com/"
sub_dir = "events"
url = base_url + sub_dir
print(url)


# In[ ]:


import requests

base_url = "https://api.github.com/"
sub_dirs = ["events", "user", "emails"]

for sub_dir in sub_dirs:
    url_dir = base_url + sub_dir
    r = requests.get(url_dir)
    print(r.url)


# #### 웹 사이트 주소에 매개변수 추가하기

# [6장: 238페이지]

# In[ ]:


import requests

where_value = 'nexearch' 
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'utf8'
query_value = 'python'

base_url = "https://search.naver.com/search.naver"
parameter = "?where={0}&sm={1}&fbm={2}&ie={3}&query={4}".format(where_value, sm_value, fbm_value, ie_value, query_value)
url_para = base_url + parameter
r = requests.get(url_para)

print(r.url)


# [6장: 239페이지]

# In[ ]:


import requests  

where_value = 'nexearch' 
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'utf8'
query_value = 'python'

url = "https://search.naver.com/search.naver"
parameters = {"where":where_value, "sm":sm_value, "fbm":fbm_value, "ie":ie_value, "query":query_value}
r = requests.get(url, params=parameters)
print(r.url)


# ## 6.2 웹 사이트에서 데이터 가져오기

# ### 6.2.1 날씨 정보 가져오기

# #### 웹 사이트 분석해 날씨 정보 가져오기

# [6장: 241페이지]

# In[ ]:


import requests  
from bs4 import BeautifulSoup 

location = "서울시 종로구 청운동"
search_query = location + " 날씨"
search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
url = search_url + search_query

html_weather = requests.get(url).text
soup_weather = BeautifulSoup(html_weather, "lxml")
print(url)

